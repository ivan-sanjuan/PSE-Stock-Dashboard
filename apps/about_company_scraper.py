import requests
from bs4 import BeautifulSoup
import io
import pandas as pd
import pprint

def get_company_profile(symbol):
    company_profile = None
    url = f'https://stockanalysis.com/quote/pse/{symbol}/company/'
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept-Language": "en-US,en;q=0.9",
            }
    response = requests.get(url, headers=headers)
    html_data = response.text
    soup = BeautifulSoup(html_data, 'html.parser')
    
    try:
        company_profile = {}
        company_profile = soup.find('div', class_='lg:float-left lg:w-[calc(100%-336px-40px)]')
        company_name = company_profile.find('h1', class_='mb-3 text-2xl font-bold').text
        company_about = company_profile.find('div', class_='mb-5 text-base md:text-lg [&>p]:mb-5').text
        
        company_profile['company_name'] = company_name
        company_profile['company_about'] = company_about
        
    except Exception as e:
        print(f'An error has occured: {e}')

    return company_profile

def get_company_profile_origin(symbol):
    url = f'https://stockanalysis.com/quote/pse/{symbol}/company/'
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept-Language": "en-US,en;q=0.9",
            }
    response = requests.get(url, headers=headers)
    html_data = response.text
    try:
        html_stringio = io.StringIO(html_data)
        df = pd.read_html(html_stringio)[0]
        print('getting about company info...')
        
    except Exception as e:
        print(f'An error occured: {e}')
        
    return df

# name = 'BDO'
# test = get_company_profile_origin(name)
# print(test)