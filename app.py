import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Scientific & Data-Driven Dashboard",
    page_icon="🔬",
    layout="wide"
)

st.title("🔬 Scientific Data Analysis Dashboard")
st.markdown("Interactive analysis workspace powered by Python, FastAPI, and Streamlit.")

# Sidebar controls
st.sidebar.header("Configuration")
num_points = st.sidebar.slider("Number of Data Points", min_value=100, max_value=5000, value=1000, step=100)
noise_level = st.sidebar.slider("Noise Level", min_value=0.0, max_value=1.0, value=0.2, step=0.05)

# Generate sample scientific dataset (e.g., simulated sensor or channel amplitudes)
np.random.seed(42)
x = np.linspace(0, 50, num_points)
y = np.sin(x) + np.random.normal(0, noise_level, num_points)

df = pd.DataFrame({"Time / Channel": x, "Amplitude": y})

# Layout: Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Samples", len(df))
col2.metric("Peak Amplitude", f"{df['Amplitude'].max():.2f}")
col3.metric("Mean Value", f"{df['Amplitude'].mean():.2f}")

# Data Visualizations
st.subheader("Signal Amplitude Distribution")
st.line_chart(df.set_index("Time / Channel"))

st.subheader("Raw Data Preview")
st.dataframe(df.head(10), use_container_width=True)