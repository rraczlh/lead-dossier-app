import streamlit as st
import glob
import frontmatter
import pandas as pd
import os
import plotly.express as px


# 1. Setup Page
st.set_page_config(layout="wide", page_title="Localhost Lead Intelligence")

# --- PATH CORRECTION ---
# Ensure we are running from the script's directory for consistent relative paths
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# 2. Capability Matrix definition
CAPABILITY_MATRIX = {
    # Programming Languages
    "Python": ("Programming Languages", "Core"),
    "Java": ("Programming Languages", "Core"),
    "C#": ("Programming Languages", "Core"),
    "C": ("Programming Languages", "Core"),
    "C++": ("Programming Languages", "Core"),
    "JavaScript": ("Programming Languages", "Core"),
    "TypeScript": ("Programming Languages", "Core"),
    "Swift": ("Programming Languages", "Core"),
    "Kotlin": ("Programming Languages", "Core"),
    "Go": ("Programming Languages", "Core"),
    "Ruby": ("Programming Languages", "Core"),
    "PHP": ("Programming Languages", "Core"),
    "HTML/CSS": ("Programming Languages", "Core"),
    "Scala": ("Programming Languages", "Core"),
    "Power Fx": ("Programming Languages", "Core"),

    # Cloud Platforms
    "AWS": ("Cloud Platforms", "Providers"),
    "Azure": ("Cloud Platforms", "Providers"),
    "GCP": ("Cloud Platforms", "Providers"),
    "Firebase": ("Cloud Platforms", "Providers"),
    "OpenShift": ("Cloud Platforms", "Providers"),
    "Heroku": ("Cloud Platforms", "Providers"),
    "AWS Lambda": ("Cloud Platforms", "Core Services"),
    "AWS IoT Core": ("Cloud Platforms", "Core Services"),
    "Azure Functions": ("Cloud Platforms", "Core Services"),
    "Azure OpenAI": ("Cloud Platforms", "Core Services"),

    # DevOps & Infra
    "Terraform": ("DevOps & Infra", "IaC & Config"),
    "Ansible": ("DevOps & Infra", "IaC & Config"),
    "Puppet": ("DevOps & Infra", "IaC & Config"),
    "CloudFormation": ("DevOps & Infra", "IaC & Config"),
    "CDK": ("DevOps & Infra", "IaC & Config"),
    "Bicep": ("DevOps & Infra", "IaC & Config"),
    "Kubernetes": ("DevOps & Infra", "Containers"),
    "Docker": ("DevOps & Infra", "Containers"),
    "GitHub Actions": ("DevOps & Infra", "CI/CD"),
    "Azure DevOps": ("DevOps & Infra", "CI/CD"),
    "Jenkins": ("DevOps & Infra", "CI/CD"),
    "GitLab": ("DevOps & Infra", "CI/CD"),
    "Bitbucket": ("DevOps & Infra", "CI/CD"),
    "Grafana": ("DevOps & Infra", "Monitoring"),
    "Prometheus": ("DevOps & Infra", "Monitoring"),
    "Dynatrace": ("DevOps & Infra", "Monitoring"),
    "AppDynamics": ("DevOps & Infra", "Monitoring"),
    "CloudWatch": ("DevOps & Infra", "Monitoring"),
    "Datadog": ("DevOps & Infra", "Monitoring"),

    # Application Development
    ".NET Core": ("Application Dev", "Backend"),
    "Node.js": ("Application Dev", "Backend"),
    "Django": ("Application Dev", "Backend"),
    "FastAPI": ("Application Dev", "Backend"),
    "Spring Boot": ("Application Dev", "Backend"),
    "Ruby on Rails": ("Application Dev", "Backend"),
    "Hibernate": ("Application Dev", "Backend"),
    "React": ("Application Dev", "Frontend"),
    "Next.js": ("Application Dev", "Frontend"),
    "Angular": ("Application Dev", "Frontend"),
    "Vue.js": ("Application Dev", "Frontend"),
    "Tailwind CSS": ("Application Dev", "Frontend"),
    "Bootstrap": ("Application Dev", "Frontend"),
    "React Native": ("Application Dev", "Mobile"),
    "Flutter": ("Application Dev", "Mobile"),
    "SwiftUI": ("Application Dev", "Mobile"),
    "Jetpack Compose": ("Application Dev", "Mobile"),
    "Ionic": ("Application Dev", "Mobile"),
    "Android": ("Application Dev", "Mobile"),
    "iOS": ("Application Dev", "Mobile"),
    "GraphQL": ("Application Dev", "APIs & Integration"),
    "REST API": ("Application Dev", "APIs & Integration"),
    "RabbitMQ": ("Application Dev", "APIs & Integration"),
    "Apache Kafka": ("Application Dev", "APIs & Integration"),
    "OAuth 2.0": ("Application Dev", "APIs & Integration"),
    "Nginx": ("Application Dev", "APIs & Integration"),

    # Data & AI
    "PostgreSQL": ("Data & AI", "Databases"),
    "MySQL": ("Data & AI", "Databases"),
    "SQL Server": ("Data & AI", "Databases"),
    "Oracle Database": ("Data & AI", "Databases"),
    "MongoDB": ("Data & AI", "Databases"),
    "DynamoDB": ("Data & AI", "Databases"),
    "CosmosDB": ("Data & AI", "Databases"),
    "Cassandra": ("Data & AI", "Databases"),
    "Redis": ("Data & AI", "Databases"),
    "Snowflake": ("Data & AI", "Databases"),
    "Elasticsearch": ("Data & AI", "Databases"),
    "Databricks": ("Data & AI", "Big Data"),
    "Spark": ("Data & AI", "Big Data"),
    "PySpark": ("Data & AI", "Big Data"),
    "Hadoop": ("Data & AI", "Big Data"),
    "Airflow": ("Data & AI", "Big Data"),
    "Pandas": ("Data & AI", "Data Science"),
    "NumPy": ("Data & AI", "Data Science"),
    "Scikit-learn": ("Data & AI", "Data Science"),
    "PyTorch": ("Data & AI", "Data Science"),
    "TensorFlow": ("Data & AI", "Data Science"),
    "Keras": ("Data & AI", "Data Science"),
    "OpenAI": ("Data & AI", "Generative AI"),
    "LangChain": ("Data & AI", "Generative AI"),
    "HuggingFace": ("Data & AI", "Generative AI"),
    "Amazon SageMaker": ("Data & AI", "Generative AI"),
    "Microsoft Power BI": ("Data & AI", "Generative AI"),

    # Tools & Productivity
    "Jira": ("Tools & Productivity", "General"),
    "Confluence": ("Tools & Productivity", "General"),
    "Microsoft 365": ("Tools & Productivity", "General"),
    "Microsoft Teams": ("Tools & Productivity", "General"),
    "SharePoint": ("Tools & Productivity", "General"),
    "Slack API": ("Tools & Productivity", "General"),
    "Selenium": ("Tools & Productivity", "Testing"),
    "Playwright": ("Tools & Productivity", "Testing"),
    "Appium": ("Tools & Productivity", "Testing"),
    "Postman": ("Tools & Productivity", "Testing"),
    "Figma": ("Tools & Productivity", "Design"),
    "Salesforce": ("Tools & Productivity", "Platforms"),
    "ServiceNow": ("Tools & Productivity", "Platforms"),
    "Microsoft Power Platform": ("Tools & Productivity", "Platforms"),
    "Microsoft Entra": ("Tools & Productivity", "Platforms"),
    "WordPress": ("Tools & Productivity", "Platforms"),
    "Unity": ("Tools & Productivity", "Game Dev"),
    "Unreal Engine": ("Tools & Productivity", "Game Dev")
}

# 3. Load Data Function
@st.cache_data
def load_dossiers():
    data = []
    
    # Robust path check
    analysis_dir = os.path.join(os.getcwd(), "analysis")
    
    if not os.path.exists(analysis_dir):
        st.error(f"❌ Analysis directory not found at: {analysis_dir}")
        st.write(f"Current Working Directory: {os.getcwd()}")
        st.write(f"Files in CWD: {os.listdir(os.getcwd())}")
        return pd.DataFrame()

    files = glob.glob(os.path.join(analysis_dir, "*.md"))
    
    if not files:
        st.warning("⚠️ No Markdown files found in 'analysis' directory.")
        st.write(f"Looking in: {analysis_dir}")
        try:
            st.write(f"Files found: {os.listdir(analysis_dir)}")
        except Exception as e:
            st.error(f"Could not list directory: {e}")
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
    required_cols = ['company_name', 'verified_revenue_usd', 'verified_revenue_text', 'detected_tech', 'overlap_tech', 'country']
    for col in required_cols:
        if col not in df.columns:
            df[col] = None 
            
    # --- DATA CLEANING ---
    df['ID'] = df['filename'].apply(lambda x: x.split('_')[0] if '_' in x else '0000')
    df['detected_tech'] = df['detected_tech'].apply(lambda x: x if isinstance(x, list) else [])
    
    # DYNAMIC OVERLAP CALCULATION (Override dossier YAML)
    def compute_overlap(row):
        detected = row['detected_tech']
        return [t for t in detected if t in CAPABILITY_MATRIX]
        
    df['overlap_tech'] = df.apply(compute_overlap, axis=1)
    
    df['missing_tech'] = df.apply(lambda x: list(set(x['detected_tech']) - set(x['overlap_tech'])), axis=1)
    df['overlap_count'] = df['overlap_tech'].apply(len)
    df['total_count'] = df['detected_tech'].apply(len)
    df['verified_revenue_usd'] = pd.to_numeric(df['verified_revenue_usd'], errors='coerce').fillna(0).astype(int)
    df['Company Name'] = df.apply(lambda x: x['company_name'] if pd.notna(x['company_name']) else x['filename'], axis=1)
    df['Match Ratio'] = df.apply(lambda x: f"{x['overlap_count']} / {x['total_count']}", axis=1)
    df['Country'] = df['country'].fillna('Unknown') 

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
    
    max_rev_data = int(df['verified_revenue_usd'].max()) if not df.empty else 1000
    abs_max = max_rev_data + 100
    
    # Initialize session state for revenue
    if 'rev_range' not in st.session_state:
        st.session_state.rev_range = (0, abs_max)
    if 'min_rev' not in st.session_state:
        st.session_state.min_rev = 0
    if 'max_rev' not in st.session_state:
        st.session_state.max_rev = abs_max

    # 1. Helper to sync from Slider to Number Inputs
    def sync_from_slider():
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
    all_techs = sorted(list(set([item for sublist in df['overlap_tech'] for item in sublist])))
    selected_tech = st.sidebar.multiselect("Tech Stack Match", all_techs)
    
    # Country Filter
    all_countries = sorted(list(set(df['Country'].unique())))
    selected_country = st.sidebar.multiselect("Country", all_countries)

    min_score = st.sidebar.slider("Min. Overlap Count", 0, 20, 0)
    
    # --- APPLY FILTERS ---
    filtered_df = df[
        (df['overlap_count'] >= min_score) & 
        (df['verified_revenue_usd'] >= min_rev_final) & 
        (df['verified_revenue_usd'] <= max_rev_final)
    ]
    
    if selected_tech:
        filtered_df = filtered_df[filtered_df['overlap_tech'].apply(lambda x: any(item in selected_tech for item in x))]
        
    if selected_country:
        filtered_df = filtered_df[filtered_df['Country'].isin(selected_country)]

    # --- MAIN TABS ---
    tab1, tab2, tab3 = st.tabs(["Lead Explorer", "Tech Insights", "Capability Alignment"])

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
                    'Country': 'Location',
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
                    key="lead_table",
                    column_config={
                        "ID": st.column_config.TextColumn("ID", width="small"),
                        "Location": st.column_config.TextColumn("Country", width="medium"),
                        "Company": st.column_config.TextColumn("Company", width="medium"),
                        "Revenue ($M)": st.column_config.NumberColumn("Revenue ($M)", format="$%d"),
                        "Ratio": st.column_config.TextColumn("Ratio", width="small"),
                        "Matched Tech": st.column_config.ListColumn("Matched Tech", width="large"),
                        "Missing Tech": st.column_config.ListColumn("Missing Tech", width="large"),
                    }
                )

                # Update selection from dataframe interaction
                # selection.selection.rows is populated ONLY on the rerun triggered by a click
                if selection.selection.rows:
                    selected_index = selection.selection.rows[0]
                    st.session_state.selected_company_id = display_df.iloc[selected_index]['ID']
                elif 'lead_table' in st.session_state and st.session_state.lead_table.selection.rows:
                    # Fallback to key-based session state if available
                    selected_index = st.session_state.lead_table.selection.rows[0]
                    st.session_state.selected_company_id = display_df.iloc[selected_index]['ID']
                else:
                    st.session_state.selected_company_id = None

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
                
                st.header(f"{selected_row['ID']} - {selected_row['Company Name']}")
                st.caption(f"Revenue: ${selected_row['verified_revenue_usd']:,}M | Tech Match: {selected_row['Match Ratio']}")
                
                # --- TECH SUMMARY BADGES ---
                st.markdown("#### Tech Landscape")
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
                
                # --- HIDE YAML DATA ---
                full_content = selected_row['content']
                if "```yaml" in full_content and "```" in full_content.split("```yaml", 1)[1]:
                    parts = full_content.split("```yaml", 1)
                    before_yaml = parts[0]
                    rest = parts[1].split("```", 1)
                    yaml_block = "```yaml" + rest[0] + "```"
                    after_yaml = rest[1]
                    
                    if before_yaml.strip():
                        st.markdown(before_yaml)
                    
                    with st.expander("📄 View Batch Metadata", expanded=False):
                        st.markdown(yaml_block)
                        
                    st.markdown(after_yaml)
                else:
                    st.markdown(full_content)

    # --- TAB 2 AND TAB 3 DATA PREP ---
    # Using the global CAPABILITY_MATRIX

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
        viz_df = viz_df.sort_values(by='Status') # Ensures 'Matched' (Ma) is before 'Missing' (Mi)
        
        if not viz_df.empty:
            # 2. Treemap (Plotly)
            fig = px.treemap(
                viz_df, 
                path=['Status', 'Technology'], 
                values='Count',
                color='Status',
                color_discrete_map={'Matched': '#2ecc71', 'Missing': '#95a5a6'},
                hover_data=['Count']
            )
            
            # Prevent Plotly from re-sorting by value, preserving our 'Status' sort
            fig.update_traces(sort=False)
            
            fig.update_layout(margin=dict(t=30, l=10, r=10, b=10))
            st.plotly_chart(fig, width="stretch", height=chart_height)
        else:
            st.info("No technology data available for the current filters.")

    with tab3:
        st.subheader("Capability Alignment (Localhost Matrix)")
        
        # Expand overlap_tech into rows with Silo and Category
        silo_data = []
        for tech_list in filtered_df['overlap_tech']:
            for tech in tech_list:
                if tech in CAPABILITY_MATRIX:
                    silo, category = CAPABILITY_MATRIX[tech]
                    silo_data.append({'Silo': silo, 'Category': category, 'Technology': tech})
        
        silo_df = pd.DataFrame(silo_data)
        
        if not silo_df.empty:
            # Count occurrences per Tech/Category/Silo
            silo_viz = silo_df.groupby(['Silo', 'Category', 'Technology']).size().reset_index(name='Count')
            
            fig_silo = px.treemap(
                silo_viz,
                path=['Silo', 'Category', 'Technology'],
                values='Count',
                color='Silo',
                color_discrete_sequence=px.colors.qualitative.Alphabet,
                hover_data=['Count']
            )
            
            fig_silo.update_layout(margin=dict(t=30, l=10, r=10, b=10))
            st.plotly_chart(fig_silo, width="stretch", height=chart_height)
            
            st.caption("This chart displays ONLY matched technologies aligned with our Capability Matrix silos.")
        else:
            st.info("No alignment found. Filter for companies with matches in our Capability Matrix.")

else:
    st.warning("No files found in 'analysis' folder.")