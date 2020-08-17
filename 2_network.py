import requests

# базовая аутификация
response = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=('user', 'passwd'))
print(f'Тело ответа {response.content}')
print(f'Код состояния {response.status_code}')

print(f'Тело ответа в bytes {response.content}')
print(f'Тело ответа в str {response.text}')
print(f'Тело ответа в json {response.json()}')
