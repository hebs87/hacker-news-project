import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# Use BeautifulSoup to get the response text and parse it into a HTML object which we can interact with
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)
