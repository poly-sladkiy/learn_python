import requests

response = requests.get('https://httpbin.org/basic-auth/user/passwd', auth='user', 'passwd')
print(f'Тело ответа {response.content}')
print(f'Код состояния {response.status_code}')
