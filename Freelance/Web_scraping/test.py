from os import link
from bs4 import BeautifulSoup
import requests
import datetime
import time
import pandas as pd
import json


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
bankUrl = 'https://www.connexuscu.org/'
bankName = 'efirstflight'
bankID = 12345678


loanType = 'Mortage Loan'
link = 'https://www.efirstflight.com/rates/lending-rates/#'    
    
# Get data from website into a dataframe using beautiful soup
html_text = requests.get(link, headers=headers).text
soup  = BeautifulSoup(html_text, 'html.parser')
mortgage_loan_table = soup.find_all('table', attrs = {'id':"tablepress-6"})
df = pd.read_html(str(mortgage_loan_table))[0]

# Clean dataframe
df.drop(df.tail(1).index,inplace = True)
df['APR1'] = df['APR1'].str.replace('%', '')
df['APR1'] = df['APR1'].astype(float)
# df['Term'] = df['Term'].str.replace(' Months', '')
# df['Term'] = df['Term'].astype(int)/12

df1 = df.iloc[0:3]
df2 = df.iloc[3:5]
df3 = df.iloc[5:8]

df1['Term'] = df1['Term'].str.replace('-year fixed', '')
df1['Term'] = df1['Term'].astype(int)

df2['Term'] = df2['Term'].str.replace(' ARM', '')

df3['Term'] = df3['Term'].str.replace('-year fixed / Rapid Refi', '')
df3['Term'] = df3['Term'].astype(int)


mortgage_loan_list = []

# fixed rate
fixed_rate = {}
fixed_rate['type'] = 'purchase'
fixed_rate['urlLink'] = link
fixed_rate['minPeriod'] = df1['Term'].min()
fixed_rate['maxPeriod'] = df1['Term'].max()
fixed_rate['rateFrom'] = str(df1['APR1'].min()) #
fixed_rate['rateTo'] = str(df1['APR1'].max())
fixed_rate['maxAmount'] = ''
fixed_rate['variableAPR'] = False
fixed_rate['fixedAPR'] = True
mortgage_loan_list.append(fixed_rate)


# variable rate
variable_rate = {}
variable_rate['type'] = 'purchase'
variable_rate['urlLink'] = link
variable_rate['minPeriod'] = df2.iloc[0]['Term']
variable_rate['maxPeriod'] = df2.iloc[1]['Term']
variable_rate['rateFrom'] = str(df2['APR1'].min()) #
variable_rate['rateTo'] = str(df2['APR1'].max())
variable_rate['maxAmount'] = ''
variable_rate['variableAPR'] = True
variable_rate['fixedAPR'] = False
mortgage_loan_list.append(variable_rate)


# Refinance fixed rate
refinance_fixed_rate = {}
refinance_fixed_rate['type'] = 'refinance'
refinance_fixed_rate['urlLink'] = link
refinance_fixed_rate['minPeriod'] = df3['Term'].min()
refinance_fixed_rate['maxPeriod'] = df3['Term'].max()
refinance_fixed_rate['rateFrom'] = str(df3['APR1'].min()) #
refinance_fixed_rate['rateTo'] = str(df3['APR1'].max())
refinance_fixed_rate['maxAmount'] = ''
refinance_fixed_rate['variableAPR'] = False
refinance_fixed_rate['fixedAPR'] = True
mortgage_loan_list.append(refinance_fixed_rate)

mortgage_loan_dict  = { "bankName":bankName, 
                         "bankID":bankID, 
                         "date":time.strftime("%m-%d-%Y"), 
                         "timestamp":time.strftime("%m-%d-%Y %H:%M:%S"),
                         "bankUrl":bankUrl, 
                         "bankDetails": {"loanType": loanType, 
                                          "itemType":mortgage_loan_list}
                          }
                         
return mortgage_loan_dict 

