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
            
            # --- STEP 1: PARSING (Find the data) ---
            # We look for the first "---" to start parsing the YAML
            # This ignores the Timestamp and ```yaml lines at the top for the DATA extraction
            start_index = raw_content.find("---")
            
            if start_index != -1:
                # Create a temporary "clean" version just for the parser
                clean_content_for_parser = raw_content[start_index:]
                post = frontmatter.loads(clean_content_for_parser)
                
                row = post.metadata
                
                # --- STEP 2: DISPLAY (Keep the original) ---
                # Crucial: We store 'raw_content' (the full file) instead of 'post.content'
                # This ensures the Timestamp and original formatting are preserved in the view.
                row['content'] = raw_content 
                row['filename'] = file
                data.append(row)
            else:
                # If no YAML found, we still load the file but with empty data
                row = {'content': raw_content, 'filename': file}
                data.append(row)
                
        except Exception as e:
            st.error(f"Error reading {file}: {e}")
            
    df = pd.DataFrame(data)
    
    # --- SAFETY FIX: Ensure columns exist ---
    required_cols = ['company_name', 'verified_revenue', 'overlap_score', 'tech_overlap']
    for col in required_cols:
        if col not in df.columns:
            df[col] = None 
            
    # Data Cleaning
    df['tech_overlap'] = df['tech_overlap'].apply(lambda x: x if isinstance(x, list) else [])
    df['overlap_score'] = df['overlap_score'].fillna(0).astype(int)
    
    # Fallback: If company_name is missing, use filename
    df['display_name'] = df.apply(lambda x: x['company_name'] if pd.notna(x['company_name']) else x['filename'], axis=1)

    return df

# 3. Load Data
df = load_dossiers()

if not df.empty:
    # --- SIDEBAR ---
    st.sidebar.header("Filter Leads")
    
    # Calculate unique techs safely
    all_techs = sorted(list(set([item for sublist in df['tech_overlap'] for item in sublist])))
    
    selected_tech = st.sidebar.multiselect("Tech Stack Match", all_techs)
    min_score = st.sidebar.slider("Min. Overlap Score", 0, 10, 0)
    
    # Apply Filters
    filtered_df = df[df['overlap_score'] >= min_score]
    if selected_tech:
        filtered_df = filtered_df[filtered_df['tech_overlap'].apply(lambda x: any(item in selected_tech for item in x))]

    # --- MAIN VIEW ---
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader(f"Matches Found: {len(filtered_df)}")
        
        if not filtered_df.empty:
            selected_display_name = st.selectbox("Select Company", filtered_df['display_name'])
            
            # Show the table
            st.dataframe(
                filtered_df[['display_name', 'verified_revenue', 'overlap_score', 'tech_overlap']], 
                use_container_width=True,
                hide_index=True
            )
        else:
            selected_display_name = None
            st.info("No companies match these filters.")

    with col2:
        if selected_display_name:
            st.markdown("---")
            row = filtered_df[filtered_df['display_name'] == selected_display_name].iloc[0]
            
            # Header
            st.title(row['display_name'])
            
            # Content (This will now include the Timestamp at the top)
            st.markdown(row['content'])
else:
    st.warning("No files found in 'analysis' folder.")