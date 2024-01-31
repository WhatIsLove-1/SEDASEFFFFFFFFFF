import pandas as pd
import plotly_express as px
import streamlit as st

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

product_line = st.sidebar.multiselect(
    "Выберете линийку продуктов",
    options=df["Product_line"].unique(),
    default=df["Product_line"].unique()
)

df_selection = (df.iloc[199:399].query(
    "City == @city & Customer_type == @customer_type & Gender == @gender & Branch == @branch & Product_line == @product_line"
))

st.title(":bar_chart: Supermarkt")
st.markdown("##")
total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(),1)
star_rating = ":star:" * int(round(average_rating,0))
average_sale_by_transaction = round(df_selection["Total"].mean(),2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Итоговые продажи:")
    st.subheader(f"US $ {total_sales:,}")
    with middle_column:
        st.subheader("Средний объем продаж:")
        st.subheader(f"{average_rating} {star_rating}")
        with right_column:
            st.subheader("Средний объем продаж за транзакцию:")
            st.subheader(f"US $ {average_sale_by_transaction}")

            st.markdown("---")

sales_by_product_line = (
    df_selection.groupby(by=["Product_line"]).sum(numeric_only=True)[["Total"]].sort_values(by="Total")
)
fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Продажи по продуктовой линейке</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white"
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
st.plotly_chart(fig_product_sales)