import requests
from bs4 import BeautifulSoup
import pprint
import pandas as pd
from io import StringIO

def get_revenue(symbol):
    url=f'https://stockanalysis.com/quote/pse/{symbol}/revenue/'
    response = requests.get(url)
    html_data = response.text
    soup = BeautifulSoup(html_data, 'html.parser')
    figures_revenue = soup.find('div', class_='my-5 grid grid-cols-2 gap-3 px-1 text-base xs:mt-6 bp:mt-7 bp:text-lg sm:grid-cols-3 sm:gap-6 sm:px-4 sm:text-xl')
    
    revenue_report = {}
    
    revenue = None
    for line in figures_revenue:
        if 'Revenue (ttm) ' in line:
            for value in line:
                revenue = value.text
    
    rev_growth = None            
    for line in figures_revenue:
        if 'Revenue Growth ' in line:
            for value in line:
                rev_growth = value.text
                
    rev_per_employee = None            
    for line in figures_revenue:
        if 'Revenue / Employee ' in line:
            for value in line:
                rev_per_employee = value.text
                
    total_employees = None            
    for line in figures_revenue:
        if 'Employees ' in line:
            for value in line:
                total_employees = value.text
    
    market_cap = None            
    for line in figures_revenue:
        if 'Employees ' in line:
            for value in line:
                market_cap = value.text
    
    revenue_report['Total Revenue'] = revenue
    revenue_report['Revenue Growth'] = rev_growth
    revenue_report['Revenue per Employee'] = rev_per_employee
    revenue_report['Total Employees'] = total_employees
    revenue_report['Market Cap'] = market_cap
    print('getting revenue summary...')
    return revenue_report


def get_revenue_history(symbol):
    url = f'https://stockanalysis.com/quote/pse/{symbol}/revenue/'
    response = requests.get(url)
    html_data = response.text
    tables = StringIO(html_data)
    df = pd.read_html(tables)[0]
    df_deprecated = df.head(5)
    print('getting revenue 5-Year history...')
    
    return df_deprecated

# name='BPI'
# test = get_revenue_history(name)
# pprint.pprint(test)
