import pandas as pd
import streamlit as st

st.set_page_config(page_title="Stock Portfolio", page_icon="📈", layout="wide")

st.title("📈 Stock Portfolio")

df = pd.read_csv("stock_portfolio.csv")

current_value = (df["Quantity"] * df["Current_Price"]).sum()
cost_basis = (df["Quantity"] * df["Purchase_Price"]).sum()
gain_loss = current_value - cost_basis
gain_loss_pct = (gain_loss / cost_basis) * 100

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Portfolio Value", f"${current_value:,.2f}")
col2.metric("Total Cost Basis", f"${cost_basis:,.2f}")
col3.metric(
    "Total Gain/Loss",
    f"${gain_loss:,.2f}",
    delta=f"{gain_loss_pct:.2f}%",
)
col4.metric("Number of Holdings", len(df))

st.dataframe(df, use_container_width=True)
