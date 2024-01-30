import pandas as pd

df=pd.read_excel(
    io="taxi.xlsx",
    engine="openpyxl",
    sheet_name="Лист1",
    skiprows=0,
    usecols="A:D",
    nrows=16
)
print(df)
