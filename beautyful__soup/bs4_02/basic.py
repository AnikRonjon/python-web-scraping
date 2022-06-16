import requests
from bs4 import BeautifulSoup


# Request an url to get response.
url = 'https://quotes.toscrape.com/'
response = requests.get(url)


# Parse response data using beautifulsoup
soup = BeautifulSoup(response.content, 'html.parser')

with open('title.txt', 'w') as file:
    for title in soup.findAll('span', {'class': 'text', 'itemprop': 'text'}):
        file.write(f'{title.string}\n')
    file.close()
    print('success')




