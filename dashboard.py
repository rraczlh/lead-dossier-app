import streamlit as st
import glob
import frontmatter
import pandas as pd

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
            
            # --- PARSING ---
            start_index = raw_content.find("---")
            
            if start_index != -1:
                clean_content_for_parser = raw_content[start_index:]
                post = frontmatter.loads(clean_content_for_parser)
                row = post.metadata
                row['content'] = raw_content 
                row['filename'] = file
                data.append(row)
            else:
                row = {'content': raw_content, 'filename': file}
                data.append(row)
                
        except Exception as e:
            st.error(f"Error reading {file}: {e}")
            
    df = pd.DataFrame(data)
    
    # --- SAFETY FIX: Ensure columns exist ---
    required_cols = ['company_name', 'verified_revenue_usd', 'verified_revenue_text', 'overlap_score', 'total_stack_count', 'tech_overlap']
    for col in required_cols:
        if col not in df.columns:
            df[col] = None 
            
    # --- DATA CLEANING & CALCULATIONS ---
    
    # 1. Ensure lists are lists
    df['tech_overlap'] = df['tech_overlap'].apply(lambda x: x if isinstance(x, list) else [])
    
    # 2. FORCE RE-CALCULATION OF SCORE (Python counts the list, ignoring the AI's number)
    df['overlap_score'] = df['tech_overlap'].apply(lambda x: len(x))
    
    # 3. Handle Total Stack Count (Trust AI or fallback to overlap count if missing)
    df['total_stack_count'] = df['total_stack_count'].fillna(0).astype(int)
    # Logic: If total count is smaller than overlap (AI error), fix it to be at least the overlap count
    df['total_stack_count'] = df.apply(lambda x: max(x['total_stack_count'], x['overlap_score']), axis=1)
    
    # 4. Revenue Cleaning
    df['verified_revenue_usd'] = pd.to_numeric(df['verified_revenue_usd'], errors='coerce').fillna(0).astype(int)

    # 5. Fallback Name
    df['Company Name'] = df.apply(lambda x: x['company_name'] if pd.notna(x['company_name']) else x['filename'], axis=1)
    
    # 6. Create "X out of Y" String
    df['Match Ratio'] = df.apply(lambda x: f"{x['overlap_score']} / {x['total_stack_count']}", axis=1)

    return df

# 3. Load Data
df = load_dossiers()

if not df.empty:
    # --- SIDEBAR FILTERS ---
    st.sidebar.header("Filter Leads")
    
    # 1. Tech Filter
    all_techs = sorted(list(set([item for sublist in df['tech_overlap'] for item in sublist])))
    selected_tech = st.sidebar.multiselect("Tech Stack Match", all_techs)
    
    # 2. Revenue Filter
    max_rev = int(df['verified_revenue_usd'].max()) if not df.empty else 1000
    rev_range = st.sidebar.slider("Revenue Range (Millions USD)", 0, max_rev + 100, (0, max_rev + 100))
    
    # 3. Score Filter
    min_score = st.sidebar.slider("Min. Overlap Score", 0, 20, 0)
    
    # --- APPLY FILTERS ---
    filtered_df = df[
        (df['overlap_score'] >= min_score) & 
        (df['verified_revenue_usd'] >= rev_range[0]) & 
        (df['verified_revenue_usd'] <= rev_range[1])
    ]
    
    if selected_tech:
        filtered_df = filtered_df[filtered_df['tech_overlap'].apply(lambda x: any(item in selected_tech for item in x))]

    # --- MAIN VIEW ---
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader(f"Matches Found: {len(filtered_df)}")
        
        if not filtered_df.empty:
            selected_company = st.selectbox("Select Company", filtered_df['Company Name'])
            
            # RENAME COLUMNS FOR DISPLAY
            display_cols = {
                'Company Name': 'Company',
                'verified_revenue_text': 'Revenue',
                'Match Ratio': 'Tech Match',
                'tech_overlap': 'Stack'
            }
            
            # Show the table
            st.dataframe(
                filtered_df[display_cols.keys()].rename(columns=display_cols), 
                use_container_width=True,
                hide_index=True
            )
        else:
            selected_company = None
            st.info("No companies match these filters.")

    with col2:
        if selected_company:
            st.markdown("---")
            row = filtered_df[filtered_df['Company Name'] == selected_company].iloc[0]
            
            # Header
            st.title(row['Company Name'])
            st.caption(f"Revenue: {row['verified_revenue_text']} | Tech Match: {row['Match Ratio']}")
            
            # Content
            st.markdown(row['content'])
else:
    st.warning("No files found in 'analysis' folder.")