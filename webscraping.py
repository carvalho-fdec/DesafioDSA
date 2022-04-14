# webscraping test

import urllib.request
from bs4 import BeautifulSoup


with urllib.request.urlopen('http://www.netvasco.com.br') as url:
    page = url.read()
    #print(page)
    print(url.geturl())
    print(url.info())
    print(url.getcode())

# Analise o html na variável 'page' e armazene-o no formato Beautiful Soup
soup = BeautifulSoup(page, 'html.parser')
#print(soup.prettify())

print(soup.title)
print(soup.title.string)
print(soup.title.name)
soup_a = soup.find_all('a')[:10]
for a in soup_a:
    print(a.get('href'))
    print(a.get_text())






