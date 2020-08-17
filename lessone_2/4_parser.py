from bs4 import BeautifulSoup
import requests

response = requests.get('https://yandex.ru/')

if response.status_code == 200:
    html_doc = BeautifulSoup(response.text, features='html.parser')
    list_of_values = html_doc.find_all('span', {'class': 'inline-stocks__value_inner'})
    list_of_name = html_doc.find_all('a', {'class': 'home-link home-link_black_yes inline-stocks__link'})

    for names, values in zip(list_of_name, list_of_values):
        print(names.text, values.text)
