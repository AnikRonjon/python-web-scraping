import requests
from bs4 import BeautifulSoup


# Request an url to get response.
url = 'https://quotes.toscrape.com/'
response = requests.get(url)

# Parse response data using beautiful soup.
soup = BeautifulSoup(response.content, 'html.parser')


print("____________________***___________________________")
print(soup.title)   # Print title tag of the page

print(soup.title.string)    # Print title of the page

print(soup.title.parent.name)    # Print parent of the title tag

print(soup.title.parent)    # Print (header), title tags parent


# List all a tag
print("____________________*List of a tag*___________________________")
for a_tag in soup.findAll('a', {'class': 'tag'}):
    print(a_tag)

# List all header of post
print("____________________*List of title of content*___________________________")
for header in soup.findAll('span', {'class': 'text', 'itemprop': 'text'}):
    print(header.string)
