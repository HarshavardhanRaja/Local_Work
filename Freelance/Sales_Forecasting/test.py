import pandas as pd

s1 = pd.read_excel('Sales-Forecasting/2 years data.xlsx', sheet_name='Planilha1')
s2 = pd.read_excel('Sales-Forecasting/2 years data.xlsx', sheet_name='Price increase dates')
s3 = pd.read_excel('Sales-Forecasting/2 years data.xlsx', sheet_name='Mandatory vacation dates')

print(s1.head())