import requests
from bs4 import BeautifulSoup

url1 = 'https://rozetka.com.ua/ua/krupy/c4628397/sort=rank;vid-225787=grechka/'
url2 = 'https://auchan.zakaz.ua/uk/categories/buckwheat-auchan/'
url3 = 'https://novus.zakaz.ua/uk/categories/buckwheat/'


def get_products():
    d = []

    r1 = requests.get(url1)
    r2 = requests.get(url2)
    r3 = requests.get(url3)
    soup1 = BeautifulSoup(r1.text, 'html.parser')
    soup2 = BeautifulSoup(r2.text, 'html.parser')
    soup3 = BeautifulSoup(r3.text, 'html.parser')

    for i in range(10):
        product = soup1.find_all(class_='goods-tile__title')[i].get_text()
        price = soup1.find_all(class_='goods-tile__price-value')[i].get_text()
        link = soup1.find_all(class_='goods-tile__heading')[i]['href']

        d.append({
            'title': product,
            'price': price,
            'link': link
        })

    for j in range(10):
        product = soup2.find_all(class_='jsx-725860710 product-tile__title')[j].get_text()
        price = soup2.find_all(class_='jsx-3642073353 Price__value_caption')[j].get_text()
        link = soup2.find_all(class_='jsx-725860710 product-tile')[j]['href']
        link = 'https://auchan.zakaz.ua' + link

        d.append({
            'title': product,
            'price': price,
            'link': link
        })

    for k in range(10):
        product = soup3.find_all(class_='jsx-725860710 product-tile__title')[k].get_text()
        price = soup3.find_all(class_='jsx-3642073353 Price__value_caption')[k].get_text()
        link = soup3.find_all(class_='jsx-725860710 product-tile')[k]['href']
        link = 'https://novus.zakaz.ua' + link

        d.append({
            'title': product,
            'price': price,
            'link': link
        })

    return d
