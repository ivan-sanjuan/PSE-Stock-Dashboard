from bs4 import BeautifulSoup
import requests

def get_stats(e):
    url = f'https://stockanalysis.com/quote/pse/{e}/statistics/'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    company_name = soup.find('div', class_='mb-0 text-2xl font-bold text-default sm:text-[26px]').text
    price_today = soup.find_all('div', class_='text-4xl font-bold transition-colors duration-300 inline-block')[0].text
    change = soup.find_all('div', class_='mb-5 flex flex-row items-end space-x-2 xs:space-x-3 bp:space-x-5')[0].text.split(maxsplit=2)[1]
    date_of_change = soup.find_all('div', class_='mb-5 flex flex-row items-end space-x-2 xs:space-x-3 bp:space-x-5')[0].text.split(maxsplit=2)[2]
    stats = {}
    valuation_column = soup.find_all('table', class_='w-full')[3]
    pe_ratio = None
    for row in valuation_column.find_all('tr', class_='border-y border-gray-200 odd:bg-gray-50 dark:border-dark-700 dark:odd:bg-dark-775'):
        if 'PE Ratio' in row.text:
            result_pe = row.text
            pe_ratio = result_pe.split()[2]
            
    ps_ratio = None        
    for row in valuation_column.find_all('tr', class_='border-y border-gray-200 odd:bg-gray-50 dark:border-dark-700 dark:odd:bg-dark-775'):
        if 'PS Ratio' in row.text:
            result_ps = row.text
            ps_ratio = result_ps.split()[2]
    peg_ratio = None        
    for row in valuation_column.find_all('tr', class_='border-y border-gray-200 odd:bg-gray-50 dark:border-dark-700 dark:odd:bg-dark-775'):
        if 'PEG Ratio' in row.text:
            result_peg = row.text
            peg_ratio = result_peg.split()[2]

    efficiency_column = soup.find_all('table', class_='w-full')[6]
    roe = None
    for row in efficiency_column.find_all('tr', class_='border-y border-gray-200 odd:bg-gray-50 dark:border-dark-700 dark:odd:bg-dark-775'):
        if 'Return on Equity (ROE)' in row.text:
            result_roe = row.text
            roe = result_roe.split()[4]
    
    stats['Company Name'] = company_name        
    stats['Price Today'] = price_today
    stats['Change'] = change
    stats['Date Change'] = date_of_change
    stats['PE Ratio'] = pe_ratio
    stats['PS Ratio'] = ps_ratio
    stats['PEG Ratio'] = peg_ratio
    stats['Return on Equity'] = roe
    print("Fetching data...")

    return stats