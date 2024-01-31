import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Excel Plotter")
st.title("Excel Plotter 📈")
st.subheader("Feed with your Excel file")

uploaded_file = st.file_uploader("Выберете XLSX-файл", type="xlsx")
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)