import requests
from bs4 import BeautifulSoup
import csv
import lxml
import json
import re

url1 = 'https://www.bankofengland.co.uk/news/prudential-regulation?NewsTypes=65d34b0d42784c6bb1dd302c1ed63653&Taxonomies=b0e4487511a44c31b3c239c3d6470f42&InfiniteScrolling=False&Direction=Latest'
url2 = 'https://www.bankofengland.co.uk/_api/News/RefreshPagedNewsList'

headers1 = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'cache-control': 'max-age=0',
            'accept-language': 'uk-UA,uk;q=0.9,ru;q=0.8,en-US;q=0.7,en;q=0.6',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

headers2 = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
            'content-type': 'application/json; charset=utf-8',
            'content-encoding': 'gzip',
            'path': '/_api/News/RefreshPagedNewsList',
            'accept-encoding': 'gzip, deflate, br'}

data2 = {'Id': '{CE377CC8-BFBC-418B-B4D9-DBC1C64774A8}',
        'PageSize': '30',
        'NewsTypesAvailable': '65d34b0d42784c6bb1dd302c1ed63653',
        'Taxonomies': 'b0e4487511a44c31b3c239c3d6470f42',
        'Page': '1',
        'Direction': '1',
        'Grid': 'false',
        'InfiniteScrolling': 'false'}

def get_html():
    #запити з сайта апі
    req2 = requests.post(url=url2, headers=headers2, data=str(data2))

    soup2 = str(BeautifulSoup(req2.content, 'html.parser'))
    # #print(soup2)
    json_file2 = json.loads(soup2)
    #print(json_file2)
    info1 = json_file2.get('Results')
    #print(info1)

    info2 = BeautifulSoup(info1, 'lxml')
    #print(info2)
    material = info2.find_all('a')
    #print(material)

    project = []

    for zag in material:
        if zag:
            href = url2+zag.get('href')
            #print(href)
        else:
            href = ""
        if zag:
            name = zag.find(class_="release-date").text
            print(name)
        else:
            name = ""


def get_pages():
    req2 = requests.post(url=url2, headers=headers2, data=str(data2))

    soup2 = str(BeautifulSoup(req2.content, 'html.parser'))
    js1 = json.loads(soup2)
    page_link = js1.get('href')
    downlurl = 'https://www.bankofengland.co.uk/-/media/boe/files/prudential-regulation/supervisory-statement/2022/may/ss122.pdf?la=en&hash=45BC0CE3D296875D6FDACFE5755BE43F977D6560'
    r = requests.qet(downlurl)
    #print(r.content)


def main():
    get_html()


    # url1 = 'https://www.bankofengland.co.uk/news/prudential-regulation?NewsTypes=65d34b0d42784c6bb1dd302c1ed63653&Taxonomies=b0e4487511a44c31b3c239c3d6470f42&InfiniteScrolling=False&Direction=Latest'
    # url2 = 'https://www.bankofengland.co.uk/_api/News/RefreshPagedNewsList'



if __name__ == '__main__':
    main()