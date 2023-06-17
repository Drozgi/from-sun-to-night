import requests
from bs4 import BeautifulSoup
from lxml import html
import json
import sqlite3

url = 'https://quotes.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')

tags = soup.find_all("div", class_="tags")

for tag in tags:
    print(tag.text.split()[1:])

conn = sqlite3.connect("data_from_web.db")
cursor = conn.cursor()


SQL = '''INSERT INTO quotes (author, quote, tags)
VALUES (?, ?, ?)'''
for i in range(len(quotes)):
    author = authors[1].text
    quote = quotes[1].text
    tag = ', '.join(tags[i].text.split()[1:])
    cursor.execute(SQL, [author, quote, tag])
    conn.commit()

