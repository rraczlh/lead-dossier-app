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
                clean_content_for_parser = raw_content[start_index:]
                post = frontmatter.loads(clean_content_for_parser)
                row = post.metadata
                row['content'] = raw_content 
                row['filename'] = os.path.basename(file)
                data.append(row)
            else:
                row = {'content': raw_content, 'filename': os.path.basename(file)}
                data.append(row)
                
        except Exception as e:
            st.error(f"Error reading {file}: {e}")
            
    df = pd.DataFrame(data)
    
    # --- SAFETY FIX ---
    required_cols = ['company_name', 'verified_revenue_usd', 'verified_revenue_text', 'detected_tech', 'overlap_tech']
    for col in required_cols:
        if col not in df.columns:
            df[col] = None 
            
    # --- DATA CLEANING ---
    df['ID'] = df['filename'].apply(lambda x: x.split('_')[0] if '_' in x else '0000')
    df['detected_tech'] = df['detected_tech'].apply(lambda x: x if isinstance(x, list) else [])
    df['overlap_tech'] = df['overlap_tech'].apply(lambda x: x if isinstance(x, list) else [])
    df['missing_tech'] = df.apply(lambda x: list(set(x['detected_tech']) - set(x['overlap_tech'])), axis=1)
    df['overlap_count'] = df['overlap_tech'].apply(len)
    df['total_count'] = df['detected_tech'].apply(len)
    df['verified_revenue_usd'] = pd.to_numeric(df['verified_revenue_usd'], errors='coerce').fillna(0).astype(int)
    df['Company Name'] = df.apply(lambda x: x['company_name'] if pd.notna(x['company_name']) else x['filename'], axis=1)
    df['Match Ratio'] = df.apply(lambda x: f"{x['overlap_count']} / {x['total_count']}", axis=1)

    return df

# 3. Load Data
df = load_dossiers()

if not df.empty:
    # --- SIDEBAR FILTERS ---
    st.sidebar.header("Filter Leads")
    
    # --- LAYOUT SETTINGS ---
    st.sidebar.markdown("---")
    st.sidebar.caption("Layout Settings")
    
    # 1. Table Width Slider
    layout_width = st.sidebar.slider("Table Width %", 30, 80, 60, 5) / 100
    
    # 2. Table Height Slider (New)
    table_height = st.sidebar.slider("Table Height (px)", 200, 1000, 500, 50)
    
    st.sidebar.markdown("---")
    
    # --- REVENUE FILTER (Slider + Text Box) ---
    st.sidebar.subheader("Revenue (USD Millions)")
    
    # Calculate Max Revenue for defaults
    max_rev_data = int(df['verified_revenue_usd'].max()) if not df.empty else 1000
    
    # A. The Slider (Quick Range)
    slider_range = st.sidebar.slider("Quick Range", 0, max_rev_data + 100, (0, max_rev_data + 100), format="$%dM")
    
    # B. The Text Boxes (Precise Input)
    rc1, rc2 = st.sidebar.columns(2)
    with rc1:
        min_rev_input = st.number_input("Min ($M)", min_value=0, value=slider_range[0])
    with rc2:
        max_rev_input = st.number_input("Max ($M)", min_value=0, value=slider_range[1])

    # --- OTHER FILTERS ---
    all_techs = sorted(list(set([item for sublist in df['overlap_tech'] for item in sublist])))
    selected_tech = st.sidebar.multiselect("Tech Stack Match", all_techs)
    
    min_score = st.sidebar.slider("Min. Overlap Count", 0, 20, 0)
    
    # --- APPLY FILTERS ---
    # Logic: We use the Text Inputs as the final authority (since they default to the slider anyway)
    filtered_df = df[
        (df['overlap_count'] >= min_score) & 
        (df['verified_revenue_usd'] >= min_rev_input) & 
        (df['verified_revenue_usd'] <= max_rev_input)
    ]
    
    if selected_tech:
        filtered_df = filtered_df[filtered_df['overlap_tech'].apply(lambda x: any(item in selected_tech for item in x))]

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

                display_cols = {
                    'ID': 'ID',
                    'Company Name': 'Company',
                    'verified_revenue_usd': 'Revenue ($M)',
                    'Match Ratio': 'Ratio',
                    'overlap_tech': 'Matched Tech',
                    'missing_tech': 'Missing Tech'
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
                    column_config={
                        "ID": st.column_config.TextColumn("ID", width="small"),
                        "Company": st.column_config.TextColumn("Company", width="medium"),
                        "Revenue ($M)": st.column_config.NumberColumn("Revenue ($M)", format="$%d"),
                        "Ratio": st.column_config.TextColumn("Ratio", width="small"),
                        "Matched Tech": st.column_config.ListColumn("Matched Tech", width="large"),
                        "Missing Tech": st.column_config.ListColumn("Missing Tech", width="large"),
                    }
                )

                # Determine Selected Row
                if selection.selection.rows:
                    selected_index = selection.selection.rows[0]
                    selected_row = filtered_df.iloc[selected_index]
                else:
                    selected_row = None
                    st.info("💡 Click a row above to view the dossier.")
            else:
                selected_row = None
                st.info("No companies match these filters.")

        with col2:
            if selected_row is not None:
                st.markdown("---")
                
                st.title(f"{selected_row['ID']} - {selected_row['Company Name']}")
                st.caption(f"Revenue: ${selected_row['verified_revenue_usd']:,}M | Tech Match: {selected_row['Match Ratio']}")
                
                # --- TECH SUMMARY BADGES ---
                st.markdown("### Tech Landscape")
                t_col1, t_col2 = st.columns(2)
                with t_col1:
                    st.markdown("**✅ Matched Tech**")
                    if selected_row['overlap_tech']:
                        # Use Streamlit's colored background formatting for a badge look
                        badges = " ".join([f":green-background[{t}]" for t in selected_row['overlap_tech']])
                        st.markdown(badges)
                    else:
                        st.caption("None matched")
                        
                with t_col2:
                    st.markdown("**❌ Missing Tech**")
                    if selected_row['missing_tech']:
                        badges = " ".join([f":gray-background[{t}]" for t in selected_row['missing_tech']])
                        st.markdown(badges)
                    else:
                        st.caption("None missing")
                
                st.markdown("---")
                st.markdown(selected_row['content'])

    with tab2:
        st.subheader("Technology Stack Insights")
        
        # Prepare Data for Treemap
        all_matched = [item for sublist in filtered_df['overlap_tech'] for item in sublist]
        all_missing = [item for sublist in filtered_df['missing_tech'] for item in sublist]
        
        matched_counts = pd.Series(all_matched).value_counts().reset_index()
        matched_counts.columns = ['Technology', 'Count']
        matched_counts['Status'] = 'Matched'
        
        missing_counts = pd.Series(all_missing).value_counts().reset_index()
        missing_counts.columns = ['Technology', 'Count']
        missing_counts['Status'] = 'Missing'
        
        viz_df = pd.concat([matched_counts, missing_counts]).reset_index(drop=True)
        
        if not viz_df.empty:
            # 2. Treemap (Plotly)
            fig = px.treemap(
                viz_df, 
                path=['Status', 'Technology'], 
                values='Count',
                color='Status',
                color_discrete_map={'Matched': '#2ecc71', 'Missing': '#e74c3c'},
                hover_data=['Count']
            )
            
            fig.update_layout(margin=dict(t=30, l=10, r=10, b=10))
            st.plotly_chart(fig, width="stretch")
        else:
            st.info("No technology data available for the current filters.")

else:
    st.warning("No files found in 'analysis' folder.")