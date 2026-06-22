import streamlit as st
import pandas as pd

st.title("Self-Learning Visualization Tool")

uploaded_file = st.file_uploader("Upload CSV File")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write(df.head())
    st.write(df.describe())
