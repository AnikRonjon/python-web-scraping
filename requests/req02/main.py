import requests


url = 'https://quotes.toscrape.com/'
response = requests.get(url)
html = response.text

with open('author.txt', 'w') as file:
    for line in html.split('\n'):
        if '<small class="author" itemprop="author">' in line:
            line = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>', '').strip()
            file.write(line)
            file.write('\n')

