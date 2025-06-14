import streamlit as st
from screener import screen_stocks

st.title("📈 Stock Screener App")
st.write("Filter stocks based on PE Ratio and Moving Averages.")

results = screen_stocks()
st.dataframe(results)
