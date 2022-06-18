import requests
from bs4 import BeautifulSoup


web_url = 'https://www.imdb.com'
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

tbody = soup.find('tbody', {'class': 'lister-list'})
trow = tbody.findAll('tr')


with open('list_of_movie.txt', 'w') as file:
    for data in trow:
        movie = data.find('td', {'class': 'titleColumn'})
        movie_name = movie.a.string.replace(',', '')
        movie_url = f"{web_url}{movie.a['href']}"
        rating_column = data.find('td', {'class': 'ratingColumn imdbRating'})
        rating = rating_column.strong.string
        file.write(f'{movie_name}  ({rating})\n{movie_url}\n')
    file.close()
    print('Success.............')
