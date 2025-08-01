import requests
from bs4 import BeautifulSoup
import pprint

def get_news(symbol):
    url = f'https://stockanalysis.com/quote/pse/{symbol}/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-US,en;q=0.9",
    }
    response = requests.get(url, headers=headers)
    html_response = response.text
    soup = BeautifulSoup(html_response, 'html.parser') 
    news_blocks = soup.find_all('div', class_='gap-4 border-gray-300 bg-default p-4 shadow last:pb-1 last:shadow-none dark:border-dark-600 sm:border-b sm:px-0 sm:shadow-none sm:last:border-b-0 lg:gap-5 sm:grid sm:grid-cols-news sm:py-6')
    
    try:
        news_1 = news_blocks[0]
        news_2 = news_blocks[1]
        
        print('fetching news...')        
        news_block = {}
        news_link_1 = news_1.find('a', class_='sm:mt-1').get('href')
        news_img_1 = news_1.find('img', class_='w-full rounded object-cover').get('src')
        news_headline_1 = news_1.find('a', class_='text-default hover:text-blue-brand_sharp dark:text-neutral-300 dark:hover:text-blue-darklink').text.strip()
        news_summary_1 = news_1.find('p', class_='overflow-auto text-[0.95rem] text-light sm:order-3').text.strip()
        news_src_date_1 = news_1.find('div', class_='mt-1 text-sm text-faded sm:order-1 sm:mt-0').text.strip()
        
        news_link_2 = news_2.find('a', class_='sm:mt-1').get('href')
        news_img_2 = news_2.find('img', class_='w-full rounded object-cover').get('src')
        news_headline_2 = news_2.find('a', class_='text-default hover:text-blue-brand_sharp dark:text-neutral-300 dark:hover:text-blue-darklink').text.strip()
        news_summary_2 = news_2.find('p', class_='overflow-auto text-[0.95rem] text-light sm:order-3').text.strip()
        news_src_date_2 = news_2.find('div', class_='mt-1 text-sm text-faded sm:order-1 sm:mt-0').text.strip()
    
        news_block['news_link_1'] = news_link_1
        news_block['news_img_1'] = news_img_1
        news_block['news_headline_1'] = news_headline_1
        news_block['news_summary_1'] = news_summary_1
        news_block['news_src_date_1'] = news_src_date_1
        
        news_block['news_link_2'] = news_link_2
        news_block['news_img_2'] = news_img_2
        news_block['news_headline_2'] = news_headline_2
        news_block['news_summary_2'] = news_summary_2
        news_block['news_src_date_2'] = news_src_date_2
        
    except Exception as e:
        print(f'Error: {e}')
    
    
    return news_block
    
    
# name = 'AC'
# test = get_news(name)
# print(test)

######################### INCORPORATE THIS INTO YOUR CODE

# except Exception as e:
#     print(f"Error: {e}")
    
#########################   