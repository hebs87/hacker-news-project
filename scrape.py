import pprint
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# Use BeautifulSoup to get the response text and parse it into a HTML object which we can interact with
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# Use the select() method to get the relevant element, class or ID
links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')
# Combine the two pages
mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_vote(hn_list):
    """
    Called by the create_custom_hn function to order the items based on vote score (highest to lowest)
    """
    return sorted(hn_list, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    """
    Scrape the data to pull the title, link href and vote value for each item in the Hacker News page
    Converts the vote value to an int and filters items that only have a vote value of over 99
    """
    hn = []

    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace('points', ''))

        if points > 99:
            hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_vote(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
