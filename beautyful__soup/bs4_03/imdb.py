import requests
from bs4 import BeautifulSoup


url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

tbody = soup.find('tbody', {'class': 'lister-list'})
trow = tbody.findAll('tr')

with open('imdb.csv', 'w') as file:
    for data in trow:
        title_column = data.find('td', {'class': 'titleColumn'})
        title = title_column.a.string.replace(',', '')
        rating_column = data.find('td', {'class': 'ratingColumn imdbRating'})
        rating = rating_column.strong.string
        file.write(f'{title},{rating}\n')
    file.close()
    print('Success')
