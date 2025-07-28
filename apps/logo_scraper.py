import requests
from bs4 import BeautifulSoup
import json

def get_company_logo(symbol):
    with open(r'utils/stock_directory.json', 'r') as file:
        stock_directory = json.load(file)
    for stock in stock_directory:
        if symbol == stock.get('stock_symbol'):    
            cmpy_id = stock.get('cmpy_id')
            url = f'https://edge.pse.com.ph/companyInformation/form.do?cmpy_id={cmpy_id}'
            response = requests.get(url)
            html_data = response.text
            soup = BeautifulSoup(html_data,'html.parser')
            avatars = soup.find_all('img')[8]
            avatar_src = avatars['src']
            full_link = f'https://edge.pse.com.ph{avatar_src}'
            
            print('getting company logo...')

            return full_link