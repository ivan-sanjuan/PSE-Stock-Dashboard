from bs4 import BeautifulSoup
from io import StringIO 
from selenium import webdriver
import json
import pandas as pd
import requests
import pprint


def get_company_financials(symbol):
    url = f'https://stockanalysis.com/quote/pse/{symbol}/financials/'
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept-Language": "en-US,en;q=0.9",
            }
    response = requests.get(url, headers=headers)
    html_data = response.text
    html_stringio = StringIO(html_data)
    
    try:
        df = pd.read_html(html_stringio)[0]
        csv_file_path = 'utils/fundamentals_table.csv'
        df.to_csv(csv_file_path, index=False)
        df_csv = pd.read_csv(csv_file_path)
        df = df_csv.drop('2016 - 2020', axis=1)
        
    except FileNotFoundError:
        print(f'Error: The file {csv_file_path}')
        
    except Exception as e:
        print(f'An error has occured: {e}')
        df = pd.read_csv(csv_file_path)
    
    return df

# name = 'BPI'
# test = get_company_financials(name)
# pprint.pprint(test)
# print(test)