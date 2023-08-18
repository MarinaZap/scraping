import requests
from bs4 import BeautifulSoup
import csv
import json


def get_html(url):
    r = requests.get(url)
    return r.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')

    bloks = soup.find_all(class_="product-item__link")
    #print(len(bloks))

    for blok in bloks:
        if blok:
            articul  = blok.find('p', class_="product-item__articul").text
        else:
            articul = ''
        #print(articul)

        if blok:
            price = blok.find("p", class_="product-item__price").text.lstrip("руб.")
        else:
            price = ''
        #print(price)
        data = {'articul': articul,
                'price': price}
        write_csv(data)

def write_csv(data):
    with open("casio.csv", 'a', encoding='utf-8') as file:
        order = ['articul', 'price']
        writer = csv.DictWriter(file, fieldnames=order)

        writer.writerow(data)


def main():
    #url = "https://shop.casio.ru/catalog/g-shock/filter/gender-is-male/apply/"
    #pettern = "https://shop.casio.ru/catalog/g-shock/filter/gender-is-male/apply/catalog/g-shock/filter/gender-is-male/apply/?PAGEN_1={}"
    #get_data(get_html(url))

    pattern = "https://shop.casio.ru/catalog/g-shock/filter/gender-is-male/apply/?PAGEN_1={}"

    for i in range(0, 5):
        url = pattern.format(str(i))
        #print(url)
        get_data(get_html(url))


if __name__ == '__main__':
    main()


