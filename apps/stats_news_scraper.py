import requests
from bs4 import BeautifulSoup

def get_news(symbol):
    url = f'https://stockanalysis.com/quote/pse/{symbol}/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-US,en;q=0.9",
    }
    response = requests.get(url, headers=headers)
    html_response = response.text
    soup = BeautifulSoup(html_response, 'html.parser')    
    try:
        # news_block = {}
        print("Fetching news...")
        news_image = soup.find_all('img', class_='w-full rounded object-cover')
        if news_image:
            news_image_link = news_image
        news_title = soup.find_all('a', class_='text-default hover:text-blue-brand_sharp dark:text-neutral-300 dark:hover:text-blue-darklink')
        news_date = soup.find_all('div', class_='mt-1 text-sm text-faded sm:order-1 sm:mt-0')
        news_summary = soup.find_all('p', class_='overflow-auto text-[0.95rem] text-light sm:order-3')
        news_link = soup.find_all('a', class_='sm:mt-1')
        if news_link:
            news_link_formatted = news_link
        
        # news_block['img'] = 
        # news_block['title'] = news_title[0].text
        # news_block['date'] = 
        # news_block['summary'] = 
        # news_block['news_link'] = 
        
        return {
            'date': news_date[0].text,
            'title': news_title[0].text,
            'summary': news_summary[0].text,
            'img': news_image_link[0].get('src', 'no image available'),
            'news_link': news_link_formatted[0].get('href', 'no news link.')
        }
    except:
        print('no news result')


name='AC'
test = get_news(name)
print(test)