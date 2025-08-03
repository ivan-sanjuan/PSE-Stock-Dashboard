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
            headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept-Language": "en-US,en;q=0.9",
            }
            response = requests.get(url, headers=headers)
            html_data = response.text
            soup = BeautifulSoup(html_data,'html.parser')
            
            try:
                content_column = soup.find_all('table')[1]
                company_name = soup.find_all('div', class_='compInfo')[0].text.strip()
                latest_date = soup.find_all('span', style='margin-left:1em;')[0].text
                initial_data = {}
                table_headers = content_column.find_all('th')
                value = content_column.find_all('td')
                
                for i, th in enumerate(table_headers):
                    if 'Open' in th.text:
                        open_value = value[i].get_text()
                        break
                        
                for i, th in enumerate(table_headers):
                    if 'Last Traded Price' in th.text:
                        last_traded_value = value[i].get_text()
                        break
                    
                for i, th in enumerate(table_headers):
                    if 'High' in th.text:
                        high_value = value[i].get_text()
                        break
                    
                for i, th in enumerate(table_headers):
                    if 'Low' in th.text:
                        low_value = value[i].get_text()
                        break

                for i, th in enumerate(table_headers):
                    if '52-Week High' in th.text:
                        week_high_value = value[i].get_text()
                        break
                    
                for i, th in enumerate(table_headers):
                    if '52-Week Low' in th.text:
                        week_low_value = value[i].get_text()
                        break

                for i, th in enumerate(table_headers):
                    if 'Previous Close and Date' in th.text:
                        current_value = value[i].get_text().strip().split(maxsplit=2)[0]
                        break
                
                initial_data['Company Name'] = company_name
                initial_data['Current Price'] = current_value
                initial_data['Latest Date'] = latest_date
                initial_data['Open' ] = open_value
                initial_data['Close'] = last_traded_value
                initial_data['High'] = high_value
                initial_data['Low'] = low_value
                initial_data['wk-high'] = week_high_value
                initial_data['wk-low'] = week_low_value
                
            except Exception as e:
                print(f'An error has occured: {e}')
                
            except UnboundLocalError:
                print(f'No initial records found for {symbol}')
            
            return initial_data


