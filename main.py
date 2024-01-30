import pandas as pd

import streamlit as  st

st.set_page_config(page_title="Supermarkt",
                   page_icon=":bar_chart:",
                   layout="wide")

df = pd.read_excel(
    io="supermarkt_sales (1).xlsx",
    engine="openpyxl",
    sheet_name="Sales",
    skiprows=3,
    usecols="B:R",
    nrows=1000
)
df_selection=(df.iloc[199:400])

st.dataframe(df_selection)
