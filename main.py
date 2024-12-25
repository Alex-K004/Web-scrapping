
import requests
import bs4
import json


response = requests.get('https://habr.com/ru/articles/')
soup = bs4.BeautifulSoup(response.text, features= 'lxml' )
articles_list = soup.select_one('div.tm-article-snippet')
articles = articles_list.select('h2.tm-title tm-title_h2')

parsed_data = []
for article in articles:
    link = 'https://habr.com/ru/' + article.select_one('a.tm-title__link')['href']
    article_response = requests.get(link)
    article_soup = bs4.BeautifulSoup(article_response.text, features= 'lxml')
    header = article_soup.select_one('h1').txt
    time = article_soup.select('time')['datetime']
    print(time)

