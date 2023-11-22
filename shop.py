import csv

import requests
from bs4 import BeautifulSoup
import re



def get_html(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    # print(soup)

    bloks = soup.find_all('div', class_="grid-view-item product-card")

    for blok in bloks:
        if blok:
            name = blok.find('a', class_="grid-view-item__link grid-view-item__image-container full-width-link").find(
                'span').text
            # print(name)
        else:
            pass
        if blok:
            link = 'https://techinstr.myshopify.com/' + blok.find('a',
                                                                  class_="grid-view-item__link grid-view-item__image-container full-width-link").get(
                'href')
            # print(link)
        else:
            pass

        # data = {'name': name,
        #         'link': link}
        # write_csv(data)


# def write_csv(data):
#     with open('shop.csv', 'a', encoding='utf-8') as file:
#         order = ['name', 'link']
#         writer = csv.DictWriter(file, fieldnames=order)
#         writer.writerow(data)


def main():
    # url = "https://techinstr.myshopify.com/collections/all"

    # pagination
    pattern = "https://techinstr.myshopify.com/collections/all?page={}"

    for i in range(1, 17):
        url = pattern.format(str(i))
        # print(url)

        get_html(url)


if __name__ == '__main__':
    main()
