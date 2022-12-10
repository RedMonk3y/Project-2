from bs4 import BeautifulSoup
from PIL import Image
from urllib import request
import requests
from csv import *
url= 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2047675.m570.l1311&_nkw=crocs+classic+clog+lightning+mcqueen&_sacat=0'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_ = 's-item__wrapper clearfix')
# imagelists = soup.find_all('div', class_ = 's-item__image-wrapper image-treatment')
with open('shoes.csv', 'w', encoding='utf8', newline= '') as f:
    pen = writer(f)
    header = ['Price', 'Shipping', 'Photo']
    pen.writerow(header)
    count=1
    for list in lists: 
        exception = list.find('span', class_ = 'BOLD BOLD')
        try:
            if list.find('span', class_ = 'BOLD BOLD').text.replace('\n', '') == 'Authenticity Guarantee':
                count +=1
                try:
                    price = list.find('span', class_ = 's-item__price').text.replace('\n', '')
                    print(price)
                except:
                    price = None
                try:
                    shipping = list.find('span', class_ = 's-item__shipping s-item__logisticsCost').text.replace('\n', '')
                    print(shipping)
                except:
                    shipping = None
                if shipping == None:
                    shipping = 'Free shipping'

                link = list.find('img', class_='s-item__image-img')
                img_url = link['src']
                img_name = 'Crocs' + str(count) + '.jpg'
                print(img_name)
                request.urlretrieve(img_url, img_name)
                #get(img_url).content
                
                picture = Image.open(img_name)
                info = [str(price), str(shipping), str(img_name)]
                pen.writerow(info)
        except:
            exception == None
    # for img in imagelists:
    #     link = imagelists.find('img', class_='s-item__image-img')
    #     print(img['src'])