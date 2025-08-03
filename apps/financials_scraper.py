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
    soup = BeautifulSoup(html_data, 'html.parser')
    tables = StringIO(html_data)
    df = pd.read_html(tables)
    header = df[0]
    rows = df[1:]
    df_formatted = pd.DataFrame(rows,columns=header)

    return df_formatted

# name = 'BPI'
# test = get_company_financials(name)
# pprint.pprint(test)
# print(type(test))