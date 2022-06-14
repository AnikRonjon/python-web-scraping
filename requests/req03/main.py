# Pagination request

import requests

for i in range(1, 20):
    url = f'https://quotes.toscrape.com/page/{i}/'
    response = requests.get(url)
    print(response.url)
    if response.status_code == 200:
        html = response.text
        with open('list_of_header.txt', 'a', encoding=response.encoding) as file:
            for line in html.split('\n'):
                if '<span class="text" itemprop="text">' in line:
                    line = line.replace('<span class="text" itemprop="text">“', '').replace('”</span>', '').strip()
                    file.write(line)
                    file.write('\n')

    else:
        print(f'{response.url} not located..')


