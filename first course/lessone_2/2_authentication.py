import requests


class MyAuth(requests.auth.AuthBase):
    def __call__(self, r):
        # r.headers['MyAuth'] = '123'
        return r


URL = 'https://httpbin.org/get'
response = requests.get(URL, auth=MyAuth())
print(response.text)
