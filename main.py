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



st.sidebar.header("Фильтр")
city=st.sidebar.multiselect(
    "Выберете город:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Выберете тип покупателя:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique()
)

gender=st.sidebar.multiselect(
    "Выберете пол:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

branch=st.sidebar.multiselect(
    "Выберете категорию:",
    options=df["Branch"].unique(),
    default=df["Branch"].unique()
)

product_line=st.sidebar.multiselect(
    "Выберете линийку продуктов",
    options=df["Product_line"].unique(),
    default=df["Product_line"].unique()
)

df_selection = df.query(
    "City == @city & Customer_type == @customer_type & Gender == @gender & Branch == @branch & Product_line == @product_line"
)

st.dataframe(df_selection)

