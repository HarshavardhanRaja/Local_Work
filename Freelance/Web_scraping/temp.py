
"""
Personal Loan
Auto Loan
Student Loan
Mortage Loan
"""


from os import link
from bs4 import BeautifulSoup
import requests
import datetime
import time
import pandas as pd
import json


# Global variables
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
bankUrl = 'https://www.connexuscu.org/'
bankName = 'Connexus CU'
bankID = 123456




def auto_Loan():
    """

    """
    # Local Variables
    loanType = 'Auto Loan'
    link = 'https://www.connexuscu.org/loans/cars/refinance/'
    
    
    # Get data from website into a dataframe using beautiful soup
    html_text = requests.get(link, headers=headers).text
    soup  = BeautifulSoup(html_text, 'html.parser')
    auto_loan_table = soup.find_all('table', attrs = {'id':"tablepress-52"})
    df = pd.read_html(str(auto_loan_table))[0]

    # Clean dataframe
    df.drop(df.tail(1).index,inplace = True)
    df.loc[(df['Model Year'] == df['Model Year'][0]), 'Model Year'] = 'new'
    df.loc[(df['Model Year'] == df['Model Year'][len(df)-1]), 'Model Year'] = 'used'
    df['Term'] = df['Term'].str.replace(' months', '')
    df['Term'] = df['Term'].astype(int)/12
    df['APR1 As Low As'] = df['APR1 As Low As'].str.replace('%', '')
    df['APR1 As Low As'] = df['APR1 As Low As'].astype(float)


    auto_loan_list = []
    for i in ['new', 'used']:
        temp = {}
        temp['type'] = i
        temp['urlLink'] = link
        temp['minPeriod'] = df[df['Model Year'] == i]['Term'].min()
        temp['maxPeriod'] = df[df['Model Year'] == i]['Term'].max()
        temp['rateFrom'] = str(df[df['Model Year'] == i]['APR1 As Low As'].min()) #
        temp['rateTo'] = str(df[df['Model Year'] == i]['APR1 As Low As'].max())
        temp['maxAmount'] = ''
        auto_loan_list.append(temp)


    auto_loan_dict  = { "bankName":bankName, 
                        "bankID":bankID, 
                        "date":time.strftime("%m-%d-%Y"), 
                        "timestamp":time.strftime("%m-%d-%Y %H:%M:%S"),
                        "bankUrl":bankUrl, 
                        "bankDetails": {"loanType": loanType, 
                                        "itemType":auto_loan_list}
                        }
    return auto_loan_dict



def personal_Loan():
    """
    """
    loanType = 'Personal Loan'
    link = 'https://www.connexuscu.org/loans/personal/'    
        
    # Get data from website into a dataframe using beautiful soup
    html_text = requests.get(link, headers=headers).text
    soup  = BeautifulSoup(html_text, 'html.parser')
    personal_loan_table = soup.find_all('table', attrs = {'id':"tablepress-49"})
    df = pd.read_html(str(personal_loan_table))[0]

    # Clean dataframe
    df.drop(df.tail(1).index,inplace = True)
    df['Term'] = df['Term'].str.replace(' Months', '')
    df['Term'] = df['Term'].astype(int)/12
    df['Rate'] = df['Rate'].str.replace('%', '')
    df['Rate'] = df['Rate'].astype(float)


    personal_loan_list = []
    temp = {}
    temp['type'] = 'Unsecured Loan'
    temp['urlLink'] = link
    temp['minPeriod'] = df['Term'].min()
    temp['maxPeriod'] = df['Term'].max()
    temp['rateFrom'] = str(df['Rate'].min()) #
    temp['rateTo'] = str(df['Rate'].max())
    temp['maxAmount'] = ''
    personal_loan_list.append(temp)

    personal_loan_dict  = { "bankName":bankName, 
                            "bankID":bankID, 
                            "date":time.strftime("%m-%d-%Y"), 
                            "timestamp":time.strftime("%m-%d-%Y %H:%M:%S"),
                            "bankUrl":bankUrl, 
                            "bankDetails": {"loanType": loanType, 
                                            "itemType":personal_loan_list}
                            }
                            
    return personal_loan_dict


def mortgage_Loan():
    """
    """
    loanType = 'Mortgage Loan'
    link = 'https://www.connexuscu.org/loans/mortgage/'    
    
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
    fixed_rate['minPeriod'] = float(df1['Term'].min())
    fixed_rate['maxPeriod'] = float(df1['Term'].max())
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
    refinance_fixed_rate['minPeriod'] = float(df3['Term'].min())
    refinance_fixed_rate['maxPeriod'] = float(df3['Term'].max())
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



if __name__ == "__main__":
    autoLoan = auto_Loan()
    personalLoan = personal_Loan()
    mortgageLoan = mortgage_Loan()
    result = []
    result.append(autoLoan)
    result.append(personalLoan)
    result.append(mortgageLoan)
    
    with open('Connexus.json', 'w') as file:
     json.dump(result, file)