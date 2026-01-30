import streamlit as st
import glob
import frontmatter
import pandas as pd
import osa

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
                row['filename'] = os.path.basename(file) # Just the filename, not path
                data.append(row)
            else:
                row = {'content': raw_content, 'filename': os.path.basename(file)}
                data.append(row)
                
        except Exception as e:
            st.error(f"Error reading {file}: {e}")
            
    df = pd.DataFrame(data)
    
    # --- NORMALIZATION (Handle Old vs New Prompt Keys) ---
    # We map old keys (stack) to new keys (tech) if the new ones don't exist
    if 'detected_tech' not in df.columns and 'detected_stack' in df.columns:
        df['detected_tech'] = df['detected_stack']
    if 'overlap_tech' not in df.columns and 'tech_overlap' in df.columns:
        df['overlap_tech'] = df['tech_overlap']

    # --- SAFETY FIX: Ensure columns exist ---
    required_cols = ['company_name', 'verified_revenue_usd', 'verified_revenue_text', 'detected_tech', 'overlap_tech']
    for col in required_cols:
        if col not in df.columns:
            df[col] = None 
            
    # --- DATA CLEANING & CALCULATIONS ---
    
    # 1. Extract ID from Filename (Assumes format: 0001_name.md)
    # Splits by '_' and takes the first part.
    df['ID'] = df['filename'].apply(lambda x: x.split('_')[0] if '_' in x else '0000')
    
    # 2. Ensure lists are lists
    df['detected_tech'] = df['detected_tech'].apply(lambda x: x if isinstance(x, list) else [])
    df['overlap_tech'] = df['overlap_tech'].apply(lambda x: x if isinstance(x, list) else [])
    
    # 3. Calculate "Missing Tech" (Detected - Overlap)
    # We use sets to subtract, then convert back to list
    df['missing_tech'] = df.apply(lambda x: list(set(x['detected_tech']) - set(x['overlap_tech'])), axis=1)
    
    # 4. Recalculate Scores (Trust Python, not AI)
    df['overlap_count'] = df['overlap_tech'].apply(len)
    df['total_count'] = df['detected_tech'].apply(len)
    
    # 5. Revenue Cleaning
    df['verified_revenue_usd'] = pd.to_numeric(df['verified_revenue_usd'], errors='coerce').fillna(0).astype(int)

    # 6. Fallback Name
    df['Company Name'] = df.apply(lambda x: x['company_name'] if pd.notna(x['company_name']) else x['filename'], axis=1)
    
    # 7. Create "X out of Y" String
    df['Match Ratio'] = df.apply(lambda x: f"{x['overlap_count']} / {x['total_count']}", axis=1)

    return df

# 3. Load Data
df = load_dossiers()

if not df.empty:
    # --- SIDEBAR FILTERS ---
    st.sidebar.header("Filter Leads")
    
    # 1. Tech Filter
    all_techs = sorted(list(set([item for sublist in df['overlap_tech'] for item in sublist])))
    selected_tech = st.sidebar.multiselect("Tech Stack Match", all_techs)
    
    # 2. Revenue Filter (Formatted)
    max_rev = int(df['verified_revenue_usd'].max()) if not df.empty else 1000
    # format="%dM" makes it display as "1000M"
    rev_range = st.sidebar.slider("Revenue Range (USD)", 0, max_rev + 100, (0, max_rev + 100), format="$%dM")
    
    # 3. Score Filter
    min_score = st.sidebar.slider("Min. Overlap Count", 0, 20, 0)
    
    # --- APPLY FILTERS ---
    filtered_df = df[
        (df['overlap_count'] >= min_score) & 
        (df['verified_revenue_usd'] >= rev_range[0]) & 
        (df['verified_revenue_usd'] <= rev_range[1])
    ]
    
    if selected_tech:
        filtered_df = filtered_df[filtered_df['overlap_tech'].apply(lambda x: any(item in selected_tech for item in x))]

    # --- MAIN VIEW ---
    col1, col2 = st.columns([1.5, 1]) # Made left column slightly wider for the extra data

    with col1:
        st.subheader(f"Matches Found: {len(filtered_df)}")
        
        if not filtered_df.empty:
            # Sort by ID
            filtered_df = filtered_df.sort_values(by='ID')
            
            selected_company = st.selectbox("Select Company", filtered_df['Company Name'])
            
            # RENAME COLUMNS FOR DISPLAY
            display_cols = {
                'ID': 'ID',
                'Company Name': 'Company',
                'verified_revenue_text': 'Revenue',
                'Match Ratio': 'Ratio',
                'overlap_tech': 'Matched Tech',
                'missing_tech': 'Missing Tech'
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
            st.title(f"{row['ID']} - {row['Company Name']}")
            st.caption(f"Revenue: {row['verified_revenue_text']} | Tech Match: {row['Match Ratio']}")
            
            # Content
            st.markdown(row['content'])
else:
    st.warning("No files found in 'analysis' folder.")