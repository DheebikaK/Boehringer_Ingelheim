import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="Boehringer Ingelheim Annual Highlights",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Dark Background and Premium Look
st.markdown("""
    <style>
    body {
        background-color: #0d1117;
        color: white;
    }
    .stButton>button {
        background-color: #6a0dad;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: bold;
    }
    .stMetric {
        background-color: #161b22;
        padding: 10px;
        border-radius: 12px;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Sample data for each year
data = {
    '2020': {
        'metrics': {
            'Total Revenue': "€19.6B",
            'R&D Investment': "€3.7B",
            'Operating Income': "€4.6B",
        },
        'trend': {
            'Year': [2017, 2018, 2019, 2020],
            'Revenue': [18.1, 17.5, 19.0, 19.6],
            'R&D Expenses': [3.2, 3.5, 3.6, 3.7],
        }
    },
    '2021': {
        'metrics': {
            'Total Revenue': "€20.6B",
            'R&D Investment': "€4.1B",
            'Operating Income': "€4.7B",
        },
        'trend': {
            'Year': [2018, 2019, 2020, 2021],
            'Revenue': [17.5, 19.0, 19.6, 20.6],
            'R&D Expenses': [3.5, 3.6, 3.7, 4.1],
        }
    },
    '2022': {
        'metrics': {
            'Total Revenue': "€24.1B",
            'R&D Investment': "€5.0B",
            'Operating Income': "€5.0B",
        },
        'trend': {
            'Year': [2019, 2020, 2021, 2022],
            'Revenue': [19.0, 19.6, 20.6, 24.1],
            'R&D Expenses': [3.6, 3.7, 4.1, 5.0],
        }
    },
    '2023': {
        'metrics': {
            'Total Revenue': "€26.8B",
            'R&D Investment': "€5.2B",
            'Operating Income': "€4.9B",
        },
        'trend': {
            'Year': [2020, 2021, 2022, 2023],
            'Revenue': [19.6, 20.6, 24.1, 26.8],
            'R&D Expenses': [3.7, 4.1, 5.0, 5.2],
        }
    },
    '2024': {
        'metrics': {
            'Total Revenue': "€TBD",
            'R&D Investment': "€TBD",
            'Operating Income': "€TBD",
        },
        'trend': {
            'Year': [2021, 2022, 2023, 2024],
            'Revenue': [20.6, 24.1, 26.8, 28.0],
            'R&D Expenses': [4.1, 5.0, 5.2, 5.4],
        }
    }
}

# App Title
st.title("💊 Boehringer Ingelheim Annual Highlights (2020–2024)")

# Year Selection
year = st.selectbox("Select Year", list(data.keys()), index=3)

# Get selected year data
selected = data[year]

# KPI Cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", selected['metrics']['Total Revenue'])
col2.metric("R&D Investment", selected['metrics']['R&D Investment'])
col3.metric("Operating Income", selected['metrics']['Operating Income'])

st.markdown("---")

# Trend Line - Revenue and R&D Investment
fig_trend = go.Figure()
fig_trend.add_trace(go.Scatter(x=selected['trend']['Year'], y=selected['trend']['Revenue'],
                               mode='lines+markers', name='Revenue (Billion €)', line=dict(color='cyan')))
fig_trend.add_trace(go.Scatter(x=selected['trend']['Year'], y=selected['trend']['R&D Expenses'],
                               mode='lines+markers', name='R&D Investment (Billion €)', line=dict(color='magenta')))
fig_trend.update_layout(
    title="📈 Revenue and R&D Investment Trends",
    xaxis_title="Year",
    yaxis_title="Billion €",
    template="plotly_dark",
)
st.plotly_chart(fig_trend, use_container_width=True)

# Bubble Chart - Product Revenue Impact
st.markdown("### 🚀 Products Driving Revenue Growth")
products_df = pd.DataFrame({
    'Product': ['JARDIANCE®', 'OFEV®', 'TRADJENTA®', 'SPIRIVA®', 'ACTILYSE®'],
    'Revenue': [8.3, 3.7, 1.6, 1.0, 0.6],
    'Growth': [13.2, 7.3, -5.0, -17.7, 10.7]
})
fig_bubble = px.scatter(products_df, x="Product", y="Revenue", size="Growth", color="Growth",
                        size_max=60, template="plotly_dark",
                        title="Top Products by Revenue and Growth Impact")
st.plotly_chart(fig_bubble, use_container_width=True)

# Moving text ticker (Marquee style using HTML)
st.markdown("""
    <marquee behavior="scroll" direction="left" style="color:cyan;font-size:18px;">
    🔥  Boehringer Ingelheim driving breakthroughs in Human Pharma, Animal Health, Biopharma Innovation, Sustainability!
    </marquee>
""", unsafe_allow_html=True)

# Plan of Actions (from extracted report points)
st.markdown("### 📋 Strategic Plan of Action (2020–2024)")
actions = [
    "Expand R&D investment into Cardiovascular, Oncology, Immunology, CNS and Retinal Health.",
    "Strengthen Human Pharma and Animal Health synergies to drive next-gen therapies.",
    "Accelerate digital transformation through AI, Quantum Computing (Google Partnership).",
    "Commit to Sustainable Development Goals - Achieve Carbon Neutrality by 2030.",
    "Enhance access to healthcare across emerging markets and underserved populations."
]
for action in actions:
    st.success(f"✅ {action}")

# Footer
st.markdown("---")
st.caption("Boehringer Ingelheim • Powered by Streamlit 🚀 | 2020–2024 Annual Insights")

