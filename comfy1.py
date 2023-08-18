import csv

import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
            'authority': 'comfy.ua',
            'method': 'GET',
            'path': '/ua/smartfon/brand__samsung/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'uk-UA,uk;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6',
            'cache-control': 'max-age=0'}

def write_csv(data):
    with open("comfy_samsung.csv", 'a', encoding='utf-8') as file:
        order = ['href', 'name', 'price']
        writer = csv.DictWriter(file, fieldnames=order)

        writer.writerow(data)

def get_html(url):
    # r = requests.get(url, headers=headers)

    # with open("comfy.html", "w", encoding="utf-8") as file:
    #     file.write(r.text)
    with open("comfy.html", encoding="utf-8") as file:
        src = file.read()

    s = BeautifulSoup(src, 'lxml')
    # blok = s.find_all(div, class_="products-list-item products-catalog-grid__item products-list-item--wide-grid")
    # print(blok)
    infos = s.find_all(class_="products-list-item__info")
    #print(info)

    for info in infos:
        if info:
            href = info.find('a').get('href')
        else:
            href = ""
        #print(href)

        if info:
            name = info.find(class_="products-list-item__name").text
        else:
            name = ""
        #print(name)

        if info:
            price = info.find(class_="products-list-item__actions-price-current").text.strip()
        else:
            price = ""
        #print(price)

        data = {"href": href,
                "name": name,
                "price": price}
        write_csv(data)



def main():
    url = 'https://comfy.ua/ua/smartfon/brand__samsung/'
    #url = 'https://comfy.ua/api/products/list?storeId=5&cityId=506'

    #get_html(url)

    pattern = 'https://comfy.ua/ua/smartfon/brand__samsung/?p={}'


    for i in range(0, 5):
        url = pattern.format(str(i))
        #print(url)
    get_html(url)




if __name__=='__main__':
    main()