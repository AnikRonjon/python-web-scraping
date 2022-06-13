import requests


url = 'https://quotes.toscrape.com/'

response = requests.get(url)
print(response.status_code)
print(response.encoding)
print(response.url)
html = response.text

with open('quotes.txt', 'w') as f:
    for line in html.split('\n'):
        if '<span class="text" itemprop="text">' in line:
            line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '')
            line = line.strip()
            f.write(line)
            f.write('\n')
