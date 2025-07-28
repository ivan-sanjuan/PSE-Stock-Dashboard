import requests
from bs4 import BeautifulSoup
import json

def get_initial_data(symbol):   
    with open(r'utils/stock_directory.json', 'r') as file:
        stock_directory = json.load(file)
    for stock in stock_directory:
        if symbol == stock.get('stock_symbol'):    
            cmpy_id = stock.get('cmpy_id')
            url = f'https://edge.pse.com.ph/companyPage/stockData.do?cmpy_id={cmpy_id}'
            response = requests.get(url)
            html_data = response.text
            soup = BeautifulSoup(html_data,'html.parser')
            content_column = soup.find_all('table')[1]
            initial_data = {}
            headers = content_column.find_all('th')
            value = content_column.find_all('td')

            for i, th in enumerate(headers):
                if 'Open' in th.text:
                    open_value = value[i].get_text()
                    break
                    
            for i, th in enumerate(headers):
                if 'Last Traded Price' in th.text:
                    last_traded_value = value[i].get_text()
                    break
                
            for i, th in enumerate(headers):
                if 'High' in th.text:
                    high_value = value[i].get_text()
                    break
                
            for i, th in enumerate(headers):
                if 'Low' in th.text:
                    low_value = value[i].get_text()
                    break

            for i, th in enumerate(headers):
                if '52-Week High' in th.text:
                    week_high_value = value[i].get_text()
                    break
                
            for i, th in enumerate(headers):
                if '52-Week Low' in th.text:
                    week_low_value = value[i].get_text()
                    break
            
            initial_data['Open' ] = open_value
            initial_data['Close'] = last_traded_value
            initial_data['High'] = high_value
            initial_data['Low'] = low_value
            initial_data['wk-high'] = week_high_value
            initial_data['wk-low'] = week_low_value
            
            return initial_data
        

