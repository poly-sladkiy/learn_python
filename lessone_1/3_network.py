import requests


print(f'{"get":-^25}')
headers = {
    'name': 'Konstantin',
    'github': 'polySladkiy',
}
response_with_header = requests.get('https://httpbin.org/get', headers=headers)
print(f'Ответ сервера с переданными заголовками: {response_with_header.text}\n')


print(f'{"post":-^25}')
data = {
    'fjdslkf': 123123,
}
response_with_data = requests.post('https://httpbin.org/post', data=data)
print(f'Ответ сервера с нашими данными: {response_with_data.text}')
print(f'Посмотреть заголовки ответа: {response_with_data.headers}\n')


print(f'{"redirect":-^25}')
response_with_redirect = requests.get('https://vk.com/im')
print(f'В итоге перекинуло на {response_with_redirect.url}')
print(f'Итоговый код состояния {response_with_redirect.status_code}')
print(f'История редиректов {response_with_redirect.history}\n')


print(f'{"without redirect":-^25}')
response_without_redirect = requests.get('https://vk.com/im', allow_redirects=False)
print(f'В итоге перекинуло на {response_without_redirect.url}')
print(f'Итоговый код состояния {response_without_redirect.status_code}')
print(f'История редиректов {response_without_redirect.history}\n')
