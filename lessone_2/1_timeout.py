import requests

print(f'{"timeout":-^25}')
try:
    response_with_timeout = requests.get('https://github.com/polySladkiy', timeout=10)
    print('Успешное подключение')
except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout):
    print('Не успели подключиться')
