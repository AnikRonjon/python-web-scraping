import requests

for i in range(1, 20):
    url = f'https://quotes.toscrape.com/page/{i}/'
    response = requests.get(url)
    html = response.text
    print(response.url)

    if response.status_code == 200:
        with open('author_with_title.csv', 'a', encoding=response.encoding) as file:
            for line in html.split('\n'):
                if '<span>by <small class="author" itemprop="author">' in line:
                    author = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>', '').strip()
                    file.write(f",{author}\n")
                if '<span class="text" itemprop="text">' in line:
                    title = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '').replace(',', '')
                    title = title.strip()

                    file.write(f'{title}')
