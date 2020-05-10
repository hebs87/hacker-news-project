import pprint
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
# Use BeautifulSoup to get the response text and parse it into a HTML object which we can interact with
soup = BeautifulSoup(res.text, 'html.parser')
# Use the select() method to get the relevant element, class or ID
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def create_custom_hn(links, subtext):
    hn = []

    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace('points', ''))

        if points > 99:
            hn.append({'title': title, 'link': href, 'votes': points})

    return hn


pprint.pprint(create_custom_hn(links, subtext))
