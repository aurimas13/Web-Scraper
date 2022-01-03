import requests
from bs4 import BeautifulSoup

# URL where to search
URL = "https://pythonjobs.github.io/"
# Getting a website
page = requests.get(URL)
html_doc = "python"

# Implementing BeautifySoup
soup = BeautifulSoup(page.content, "html.parser")

# Printing the available job positions
for row in soup.find_all('h1', a=False, href=False, class_=False):
    if row.text != 'Most Recent Jobs':
        for url in row.find_all('a'):
            print(row.text + ' | ' + url.get('href'))
