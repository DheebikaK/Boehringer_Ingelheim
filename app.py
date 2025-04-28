import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Page Config
st.set_page_config(
    page_title="Boehringer Ingelheim Highlights",
    page_icon="📈",
    layout="wide"
)

# --- Background Styling ---
st.markdown("""
<style>
body {background: linear-gradient(135deg, #f0f4f8, #d9e2ec);}
.main {background: transparent;}
[data-testid="stHeader"] {background: transparent;}
[data-testid="stSidebar"] {background: linear-gradient(135deg, #c3cfe2, #f5f7fa);}
[data-testid="stToolbar"] {right: 2rem;}
div.stButton > button {
    color: white;
    background: linear-gradient(to right, #5B247A, #1BCEDF);
    border: none;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    font-size: 1rem;
    font-weight: bold;
    margin-top: 10px;
    box-shadow: 0px 4px 8px rgba(0,0,0,0.2);
    transition: 0.3s;
}
div.stButton > button:hover {
    background: linear-gradient(to right, #1BCEDF, #5B247A);
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown("""
<marquee behavior="scroll" direction="left" scrollamount="8" style="color: #5B247A; font-size: 1.5rem; padding: 10px; background-color: #d9e2ec; border-radius: 10px; margin-bottom: 20px;">
    📈 Boehringer Ingelheim | 2020 ➡️ 2023 ➡️ 2024: Growth in Motion 🚀
</marquee>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background: linear-gradient(135deg, #5B247A, #1BCEDF); padding: 3rem 2rem; border-radius: 20px; text-align: center; color: white; margin-bottom: 2rem;">
    <h1 style="font-size: 3rem; margin-bottom: 0.5rem;">Boehringer Ingelheim</h1>
    <h3 style="font-weight: normal;">Transforming Lives for Generations</h3>
    <p style="margin-top: 1rem; font-size: 1.1rem;">Annual Highlights, Financial Performance, and Strategic Vision</p>
</div>
""", unsafe_allow_html=True)

# --- Company Overview ---
st.subheader("🏢 About Boehringer Ingelheim")
st.markdown("""
**Boehringer Ingelheim** is one of the world’s largest family-owned pharmaceutical companies, dedicated to improving human and animal health for over 140 years.

- **Founded:** 1885, Germany  
- **Global Presence:** 130+ markets, ~54,500 employees  
- **Revenue 2024:** €26.8 billion (↑5%)  
- **Top Sectors:** Human Pharma, Animal Health, Biopharma Manufacturing
""")

st.markdown("---")

# --- Data Definitions ---
data = {
    "2024": {"metrics": {"Total Revenue": "€26.8B (+5%)", "R&D Investment": "€6.2B (+8%)", "Operating Income": "€4.9B (+10.7%)"},
        "business_units": pd.DataFrame({'Business Unit': ['Human Pharma', 'Animal Health', 'Other Sales'], 'Revenue (Million EUR)': [21928, 4749, 119]}),
        "regions": pd.DataFrame({'Region': ['Americas', 'Europe', 'Asia/Australia/Africa'], 'Share (%)': [46, 35, 19]}),
        "human_pharma": pd.DataFrame({'Product': ['JARDIANCE® family', 'OFEV®', 'TRAJENTA®/JENTADUETO®', 'SPIRIVA®'], 'Revenue (Million EUR)': [8357, 3766, 1621, 1062], 'Growth (%)': [13.2, 7.3, -5.0, -17.7]}),
        "trend": pd.DataFrame({'Year': ['2020', '2021', '2022', '2023', '2024'], 'Revenue (Billion EUR)': [19.5, 22.0, 24.1, 25.6, 26.8], 'R&D Expenses (Billion EUR)': [3.7, 4.1, 5.0, 5.8, 6.2]}),
        "initiatives": ["Sustainable Development Goals Focus", "Digital Healthcare Innovation", "R&D Excellence", "Global Market Expansion"]},
    "2023": {"metrics": {"Total Revenue": "€25.6B (+6%)", "R&D Investment": "€5.8B (+14%)", "Operating Income": "N/A"},
        "business_units": pd.DataFrame({'Business Unit': ['Human Pharma', 'Animal Health', 'Other Sales'], 'Revenue (Million EUR)': [20774, 4724, 113]}),
        "regions": pd.DataFrame({'Region': ['Americas', 'Europe', 'Asia/Australia/Africa'], 'Share (%)': [48, 32, 20]}),
        "human_pharma": pd.DataFrame({'Product': ['JARDIANCE® family', 'OFEV®', 'TRAJENTA®/JENTADUETO®', 'SPIRIVA®'], 'Revenue (Million EUR)': [7382, 3510, 1706, 1290], 'Growth (%)': [26.6, 8.8, 0.2, -17.3]}),
        "trend": pd.DataFrame({'Year': ['2020', '2021', '2022', '2023'], 'Revenue (Billion EUR)': [19.5, 22.0, 24.1, 25.6], 'R&D Expenses (Billion EUR)': [3.7, 4.1, 5.0, 5.8]}),
        "initiatives": ["Launch 25 New Human Pharma Treatments by 2030", "R&D Focus on Mental Health and Oncology", "Expansion in Cardio-Renal-Metabolic Space"]},
    "2020": {"metrics": {"Total Revenue": "€19.566B (+3%)", "R&D Investment": "€3.696B (+7%)", "Operating Income": "€4.624B (+22%)"},
        "business_units": pd.DataFrame({'Business Unit': ['Human Pharma', 'Animal Health', 'Biopharma CM', 'Discontinued Operations'], 'Revenue (Million EUR)': [14468, 4084, 771, 243]}),
        "regions": pd.DataFrame({'Region': ['Americas', 'Europe', 'Asia/Australia/Africa'], 'Share (%)': [45, 30, 25]}),
        "human_pharma": pd.DataFrame({'Product': ['JARDIANCE®', 'OFEV®', 'SPIRIVA®', 'TRAJENTA®/JENTADUETO®'], 'Revenue (Million EUR)': [2480, 2055, 1793, 1512], 'Growth (%)': [15, 38, -13, -3]}),
        "trend": pd.DataFrame({'Year': ['2018', '2019', '2020'], 'Revenue (Billion EUR)': [17.5, 19.0, 19.566], 'R&D Expenses (Billion EUR)': [3.2, 3.4, 3.696]}),
        "initiatives": ["Strengthened Cardiovascular Research", "Increased Biopharma Manufacturing Capacity", "Accelerated Digital Transformation"]}
}

# --- Year Selector ---
year = st.sidebar.selectbox("Select Year", ("2024", "2023", "2020"))
if st.sidebar.button("🔄 Reset Dashboard"):
    st.experimental_rerun()

selected = data[year]

# --- KPI Cards ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", selected['metrics']['Total Revenue'])
col2.metric("R&D Investment", selected['metrics']['R&D Investment'])
col3.metric("Operating Income", selected['metrics']['Operating Income'])

st.markdown("---")

# --- Bubble Chart: Human Pharma Products ---
st.subheader("🧬 Top Human Pharma Products (Bubble Chart)")
fig_bubble = px.scatter(selected['human_pharma'], x='Product', y='Revenue (Million EUR)', size='Revenue (Million EUR)', color='Growth (%)', color_continuous_scale="RdYlGn", size_max=60)
fig_bubble.update_layout(height=500)
st.plotly_chart(fig_bubble, use_container_width=True)

# --- Trend Line Chart: Revenue vs R&D ---
st.subheader("📈 Revenue and R&D Investment Trend")
fig_trend = go.Figure()
fig_trend.add_trace(go.Scatter(x=selected['trend']['Year'], y=selected['trend']['Revenue (Billion EUR)'], name="Revenue (€B)", mode="lines+markers", line=dict(color="royalblue", width=4)))
fig_trend.add_trace(go.Scatter(x=selected['trend']['Year'], y=selected['trend']['R&D Expenses (Billion EUR)'], name="R&D Investment (€B)", mode="lines+markers", line=dict(color="green", width=4, dash='dash')))
fig_trend.update_layout(yaxis_title="Billion EUR", xaxis_title="Year", legend_title="Legend", height=450)
st.plotly_chart(fig_trend, use_container_width=True)

# --- Strategic Initiatives ---
st.subheader("🌟 Strategic Focus Areas")
for initiative in selected['initiatives']:
    st.success(f"{initiative}")

st.markdown("---")

# --- Download Button ---
st.subheader("📥 Download Dashboard")
if st.button("Download Charts Summary (Coming Soon)"):
    st.info("Download functionality coming soon! 📄✨ Stay tuned.")

st.caption("Data source: Boehringer Ingelheim Annual Reports 2020, 2023, 2024")
