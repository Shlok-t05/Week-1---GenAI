import pandas as pd
import plotly.express as px
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

df["Current_Value"] = df["Quantity"] * df["Current_Price"]
df["Gain_Loss_Pct"] = (
    (df["Current_Price"] - df["Purchase_Price"]) / df["Purchase_Price"]
) * 100

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Allocation by Sector")
    sector_value = df.groupby("Sector")["Current_Value"].sum().reset_index()
    fig_pie = px.pie(
        sector_value,
        names="Sector",
        values="Current_Value",
        hole=0.3,
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with chart_col2:
    st.subheader("Gain/Loss % by Stock")
    df_sorted = df.sort_values("Gain_Loss_Pct")
    bar_colors = ["#2ecc71" if pct >= 0 else "#e74c3c" for pct in df_sorted["Gain_Loss_Pct"]]
    fig_bar = px.bar(
        df_sorted,
        x="Ticker",
        y="Gain_Loss_Pct",
    )
    fig_bar.update_traces(marker_color=bar_colors)
    fig_bar.update_layout(yaxis_title="Gain/Loss (%)")
    st.plotly_chart(fig_bar, use_container_width=True)

st.dataframe(df, use_container_width=True)
