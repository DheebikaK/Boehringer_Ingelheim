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

# --- Year Selector ---
year = st.sidebar.selectbox("Select Year", ("2024", "2023", "2020"))

if st.sidebar.button("🔄 Reset Dashboard"):
    st.experimental_rerun()

# --- Data Definitions ---
# [Your full data dictionary here as previously detailed]
# Assuming "data" dictionary is defined correctly

selected = data[year]

# --- KPI Cards ---
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", selected['metrics']['Total Revenue'])
col2.metric("R&D Investment", selected['metrics']['R&D Investment'])
col3.metric("Operating Income", selected['metrics']['Operating Income'])

st.markdown("---")

# --- Bubble Chart: Human Pharma Products ---
st.subheader("🧬 Top Human Pharma Products (Bubble Chart)")
fig_bubble = px.scatter(
    selected['human_pharma'],
    x='Product',
    y='Revenue (Million EUR)',
    size='Revenue (Million EUR)',
    color='Growth (%)',
    color_continuous_scale="RdYlGn",
    size_max=60
)
fig_bubble.update_layout(height=500)
st.plotly_chart(fig_bubble, use_container_width=True)

# --- Trend Line Chart: Revenue vs R&D ---
st.subheader("📈 Revenue and R&D Investment Trend")
fig_trend = go.Figure()
fig_trend.add_trace(go.Scatter(x=selected['trend']['Year'], y=selected['trend']['Revenue (Billion EUR)'], name="Revenue (€B)", mode="lines+markers", line=dict(color="royalblue", width=4)))
fig_trend.add_trace(go.Scatter(x=selected['trend']['Year'], y=selected['trend']['R&D Expenses
