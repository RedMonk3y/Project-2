from bs4 import BeautifulSoup
import requests
from csv import writer

url= 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2047675.m570.l1311&_nkw=crocs+classic+clog+lightning+mcqueen&_sacat=0'
page = requests.get(url)

print(page)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_ = 's-item__details clearfix')

with open('shoes.csv', 'w', encoding='utf8', newline= '') as f:
    pen = writer(f)
    header = ['Price', 'Shipping']
    pen.writerow(header)
    for list in lists: 
        price = list.find('span', class_ = 's-item__price').text.replace('\n', '')
        shipping = list.find('span', class_ = 's-item__shipping s-item__logisticsCost').text.replace('\n', '')
        info = [price, shipping]
        pen.writerow(info)