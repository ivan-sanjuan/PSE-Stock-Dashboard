import requests
from bs4 import BeautifulSoup

def get_news(e):
    url = f'https://stockanalysis.com/quote/pse/{e}/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-US,en;q=0.9",
    }
    response = requests.get(url, headers=headers)
    html_response = response.text
    soup = BeautifulSoup(html_response, 'html.parser')
    
    news_block = {}
    news_image = soup.find_all('img', class_='w-full rounded object-cover')
    if news_image:
        news_image_link = news_image[0].get('src', 'no image available')
    news_title = soup.find_all('h3', class_='mb-2 mt-3 text-xl font-bold leading-snug sm:order-2 sm:mt-0 sm:leading-tight')[0].text
    news_date = soup.find_all('div', class_='mt-1 text-sm text-faded sm:order-1 sm:mt-0')[0].text
    news_summary = soup.find_all('p', class_='overflow-auto text-[0.95rem] text-light sm:order-3')[0].text
    news_link = soup.find_all('a', class_='sm:mt-1')
    if news_link:
        news_link_formatted = news_link[0].get('href', 'no news link.')
    
    news_block['img'] = news_image_link
    news_block['title'] = news_title
    news_block['date'] = news_date
    news_block['summary'] = news_summary
    news_block['news_link'] = news_link_formatted
    print("Fetching news...")

    
    return news_block