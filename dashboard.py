import streamlit as st
import glob
import frontmatter
import pandas as pd
import os
import plotly.express as px

# 1. Setup Page
st.set_page_config(layout="wide", page_title="Localhost Lead Intelligence")

# 2. Load Data Function
@st.cache_data
def load_dossiers():
    data = []
    files = glob.glob("analysis/*.md") 
    
    if not files:
        return pd.DataFrame()

    for file in files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                raw_content = f.read()
            
            # --- PARSING LOGIC ---
            start_index = raw_content.find("---")
            
            if start_index != -1:
                # 1. Identify what's before the YAML (e.g. Generated via line)
                prefix = raw_content[:start_index].strip()
                # Remove trailing ```yaml or ``` from prefix to avoid empty boxes
                if prefix.endswith("```yaml"):
                    prefix = prefix[:-7].strip()
                elif prefix.endswith("```"):
                    prefix = prefix[:-3].strip()
                
                # 2. Parse the Frontmatter
                clean_content_for_parser = raw_content[start_index:]
                post = frontmatter.loads(clean_content_for_parser)
                
                row = post.metadata
                
                # 3. Clean the body (post.content)
                body = post.content.strip()
                # Remove leading ``` from body if it was left over from a wrapper
                if body.startswith("```"):
                    body = body[3:].strip()
                
                row['body'] = prefix + "\n\n" + body if prefix else body
                
                # 4. Extract the YAML block itself for the dropdown
                # We want to catch the block from the first --- to the next ---
                second_dash = clean_content_for_parser.find("---", 3)
                if second_dash != -1:
                    row['yaml_block'] = clean_content_for_parser[:second_dash+3].strip()
                else:
                    row['yaml_block'] = clean_content_for_parser.strip()
                    
                row['filename'] = os.path.basename(file)
                data.append(row)
            else:
                row = {
                    'body': raw_content, 
                    'yaml_block': None, 
                    'filename': os.path.basename(file)
                }
                data.append(row)
                
        except Exception as e:
            st.error(f"Error reading {file}: {e}")
            
    df = pd.DataFrame(data)
    
    # --- SAFETY FIX ---
    required_cols = ['country', 'company_name', 'verified_revenue_usd', 'verified_revenue_text', 'detected_tech', 'body', 'yaml_block']
    for col in required_cols:
        if col not in df.columns:
            df[col] = "" if col in ['body', 'yaml_block'] else None
            
    # --- TECH PROCESSING ---
    df['ID'] = df['filename'].apply(lambda x: x.split('_')[0] if '_' in x else '0000')
    df['detected_tech'] = df['detected_tech'].apply(lambda x: x if isinstance(x, list) else [])
    df['total_count'] = df['detected_tech'].apply(len)
    df['verified_revenue_usd'] = pd.to_numeric(df['verified_revenue_usd'], errors='coerce').fillna(0).astype(int)
    df['Company Name'] = df.apply(lambda x: x['company_name'] if pd.notna(x['company_name']) else x['filename'], axis=1)

    return df

# 3. Load Data
df = load_dossiers()

if not df.empty:
    # --- SIDEBAR FILTERS ---
    st.sidebar.header("Filter Leads")
    
    # --- SIDEBAR CONFIG ---
    st.sidebar.title("Search & Filters")
    
    with st.sidebar.expander("UI Settings", expanded=False):
        layout_width = st.slider("Explorer Width Ratio", 0.3, 0.8, 0.5)
        table_height = st.slider("Table Height", 200, 1000, 500)
        chart_height = st.slider("Chart Height", 400, 1500, 800)
    
    st.sidebar.markdown("---")
    
    # --- REVENUE FILTER (Synchronized Slider + Text Box) ---
    st.sidebar.subheader("Revenue (USD Millions)")
    
    max_rev_val = df['verified_revenue_usd'].max()
    max_rev_data = int(max_rev_val) if pd.notna(max_rev_val) else 1000
    abs_max = int(max_rev_data + 100)
    
    # Initialize session state for revenue
    if 'rev_range' not in st.session_state:
        st.session_state.rev_range = (0, abs_max)
    if 'min_rev' not in st.session_state:
        st.session_state.min_rev = 0
    if 'max_rev' not in st.session_state:
        st.session_state.max_rev = abs_max

    # 1. Helper to sync from Slider to Number Inputs
    def sync_from_slider():
        if 'rev_slider' in st.session_state:
            st.session_state.min_rev = st.session_state.rev_slider[0]
            st.session_state.max_rev = st.session_state.rev_slider[1]

    # 2. Helper to sync from Number Inputs to Slider
    def sync_from_inputs():
        # Ensure min doesn't exceed max
        if st.session_state.min_rev > st.session_state.max_rev:
            st.session_state.min_rev = st.session_state.max_rev
        st.session_state.rev_range = (st.session_state.min_rev, st.session_state.max_rev)

    # A. The Slider
    slider_range = st.sidebar.slider(
        "Quick Range", 
        0, abs_max, 
        key="rev_slider",
        on_change=sync_from_slider,
        value=st.session_state.rev_range,
        format="$%dM"
    )
    
    # B. The Text Boxes (Precise Input)
    rc1, rc2 = st.sidebar.columns(2)
    with rc1:
        min_rev_input = st.sidebar.number_input(
            "Min ($M)", 
            min_value=0, 
            max_value=abs_max,
            key="min_rev",
            on_change=sync_from_inputs
        )
    with rc2:
        max_rev_input = st.sidebar.number_input(
            "Max ($M)", 
            min_value=0, 
            max_value=abs_max,
            key="max_rev",
            on_change=sync_from_inputs
        )

    # FINAL AUTHORITY: Always use the session state values which are now kept in sync
    min_rev_final = st.session_state.min_rev
    max_rev_final = st.session_state.max_rev

    # --- OTHER FILTERS ---
    all_techs = sorted(list(set([item for sublist in df['detected_tech'] for item in sublist])))
    selected_tech = st.sidebar.multiselect("Filter by Technology", all_techs)
    
    # --- APPLY FILTERS ---
    filtered_df = df[
        (df['verified_revenue_usd'] >= min_rev_final) & 
        (df['verified_revenue_usd'] <= max_rev_final)
    ]
    
    if selected_tech:
        filtered_df = filtered_df[filtered_df['detected_tech'].apply(lambda x: any(item in selected_tech for item in x))]

    # --- MAIN TABS ---
    tab1, tab2 = st.tabs(["Lead Explorer", "Tech Insights"])

    with tab1:
        # --- MAIN VIEW ---
        col1, col2 = st.columns([layout_width, 1 - layout_width])

        with col1:
            st.subheader(f"Matches Found: {len(filtered_df)}")
            
            if not filtered_df.empty:
                filtered_df = filtered_df.sort_values(by='ID').reset_index(drop=True)
                
                # Prepare Table Data
                display_df = filtered_df.copy()
                
                # Bi-directional ID persistence (ensure state exists for the lambda below)
                if 'selected_company_id' not in st.session_state:
                    st.session_state.selected_company_id = None
                
                display_cols = {
                    'ID': 'ID',
                    'Company Name': 'Company',
                    'country': 'Country',
                    'verified_revenue_usd': 'Revenue ($M)',
                    'detected_tech': 'Detected Tech'
                }
                
                table_data = display_df[display_cols.keys()].rename(columns=display_cols)
                
                # CONFIGURABLE TABLE WITH SELECTION
                selection = st.dataframe(
                    table_data,
                    height=table_height,
                    width="stretch",
                    hide_index=True,
                    on_select="rerun",
                    selection_mode="single-row",
                    key="lead_table",
                    column_config={
                        "ID": st.column_config.TextColumn("ID", width="small"),
                        "Company": st.column_config.TextColumn("Company", width="medium"),
                        "Country": st.column_config.TextColumn("Country", width="small"),
                        "Revenue ($M)": st.column_config.NumberColumn("Revenue ($M)", format="$%d"),
                        "Detected Tech": st.column_config.ListColumn("Detected Tech", width="large"),
                    }
                )

                # Robust Selection Handling
                # 1. Check direct return from st.dataframe
                selection_data = getattr(selection, "selection", selection)
                rows = selection_data.get("rows", []) if isinstance(selection_data, dict) else getattr(selection_data, "rows", [])
                
                # 2. Check session_state fallback
                if not rows and 'lead_table' in st.session_state:
                    state_val = st.session_state.lead_table
                    state_selection = getattr(state_val, "selection", state_val)
                    rows = state_selection.get("rows", []) if isinstance(state_selection, dict) else getattr(state_selection, "rows", [])

                if rows:
                    selected_index = rows[0]
                    st.session_state.selected_company_id = display_df.iloc[selected_index]['ID']

                # Resolve selected_row from session_state ID
                if st.session_state.selected_company_id:
                    # Check if the ID still exists in the filtered results
                    match = filtered_df[filtered_df['ID'] == st.session_state.selected_company_id]
                    if not match.empty:
                        selected_row = match.iloc[0]
                    else:
                        selected_row = None
                        st.session_state.selected_company_id = None
                else:
                    selected_row = None

                # Display hint if nothing selected
                if selected_row is None:
                    st.info("💡 Click a row above to view the dossier.")
            else:
                selected_row = None
                st.info("No companies match these filters.")

        with col2:
            if selected_row is not None:
                st.markdown("---")
                
                st.title(f"{selected_row['ID']} - {selected_row['Company Name']}")
                st.caption(f"Revenue: ${selected_row['verified_revenue_usd']:,}M | Tech Count: {len(selected_row['detected_tech'])}")
                
                # --- TECH SUMMARY BADGES ---
                st.markdown("### Detected Tech Stack")
                if selected_row['detected_tech']:
                    badges = " ".join([f":blue-background[{t}]" for t in selected_row['detected_tech']])
                    st.markdown(badges)
                else:
                    st.caption("No technology detected.")
                
                st.markdown("---")
                if selected_row.get('yaml_block'):
                    with st.expander("🔍 RAW DATA / YAML", expanded=False):
                        st.code(selected_row['yaml_block'], language="yaml")
                
                st.markdown(selected_row['body'])

    # --- TAB 2 DATA PREP ---

    with tab2:
        st.subheader("Global Technology Stack Insights")
        
        # Prepare Data for Treemap
        all_techs = [item for sublist in filtered_df['detected_tech'] for item in sublist]
        
        if all_techs:
            tech_counts = pd.Series(all_techs).value_counts().reset_index()
            tech_counts.columns = ['Technology', 'Count']
            
            # 2. Treemap (Plotly)
            fig = px.treemap(
                tech_counts, 
                path=['Technology'], 
                values='Count',
                color='Count',
                color_continuous_scale='Viridis',
                hover_data=['Count']
            )
            
            fig.update_layout(margin=dict(t=30, l=10, r=10, b=10))
            st.plotly_chart(fig, width="stretch", height=chart_height)
        else:
            st.info("No technology data available for the current filters.")

else:
    st.warning("No files found in 'analysis' folder.")