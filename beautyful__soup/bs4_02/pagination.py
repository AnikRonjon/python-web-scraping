import requests
from bs4 import BeautifulSoup


# Request an url to get response.
for i in range(1, 10):
    url = f'https://quotes.toscrape.com/page/{i}/'
    response = requests.get(url)

    # Parse response data using beautifulsoup
    soup = BeautifulSoup(response.content, 'html.parser')

    with open('title.txt', 'a') as file:
        for title in soup.findAll('span', {'class': 'text'}):
            title = title.string.replace('“', '').replace('”', '')
            file.write(f'{title}\n')
            print(f"{title}")
        print('success')