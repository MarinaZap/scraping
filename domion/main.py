import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    bloks = soup.find_all('div', class_="row onemovie mb30")
    #print(len(bloks))

    for blok in bloks:
        if blok:
            name = blok.find('div', class_="col-xs-12 col-sm-8 col-md-9").find('h2').text.strip()
        else:
            name = ''
        #print(name)

        if blok:
            description = blok.find('div', class_="col-xs-12 col-sm-8 col-md-9").find('div').text
        else:
            description = ''
        #print(description)
        if blok:
            director = blok.find('div', class_="col-xs-12 col-sm-8 col-md-9").find('div', class_="mt10").text
        else:
            director = ''
        #print(director)
        if blok:
            actors = blok.find_all(class_="mt10")[1].text
        else:
            actors = ''
        # print(actors)
        if blok:
            info = blok.find_all(class_="mt10")[2].text
        else:
            info = ''
        # print(info)
        if blok:
            prod = blok.find_all(class_="mt10")[3].text
        else:
            prod = ''
        # print(prod)

        if blok:
            time = blok.find_all('div')[7].text
        else:
            time = ''
        # print(time)
        if blok:
            age = time = blok.find_all('div')[8].text
        else:
            age = ''
        # print(age)

        if blok:
            sesion = blok.find('div', class_="sessions").text
        else:
            sesion = ''
        # print(sesion)


    data={'name':name,
          'description': description,
          'director': director,
          'actors': actors,
          'info': info,
          'prod': prod,
          'time': time,
          'age': age,
          'sesion': sesion}

    write_csv(data)
def get_rules():
    url2 = 'domion.info/rules'
    req = requests.get(url2)
    soup2 = BeautifulSoup(req.text, 'hlml.parser')
    rules  = soup2.find('div', class_='text-justify').text
    rules_data = {
        'Rules':rules
    }
    write_csv(rules_data)

def write_csv(data):
    file_name = 'films.csv'
    if len(data)==1:
        file_name='rules_.csv'
    with open('domion.csv', 'a', encoding='utf-8') as file:
        w = csv.DictWriter(file, data.keys())
        if file.tell()==0:
            w.writeheader()
        w.writerow(data)

#order = ['name', 'description', 'director', 'actors', 'info', 'prod', 'time', 'age', 'sesion']

def main():
    url = 'http://domion.info/'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
