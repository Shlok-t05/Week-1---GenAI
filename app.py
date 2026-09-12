import pandas as pd
import streamlit as st

st.set_page_config(page_title="Stock Portfolio", page_icon="📈", layout="wide")

st.title("📈 Stock Portfolio")

df = pd.read_csv("stock_portfolio.csv")

st.dataframe(df, use_container_width=True)
