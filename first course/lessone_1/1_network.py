import urllib.request

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
top_level_url = 'https://httpbin.org/basic-auth/user/passwd'
password_mgr.add_password(None, top_level_url, 'user', 'passwd')
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)
response = opener.open(top_level_url)
print(f'Код состояния: {response.getcode()}')
print(f'Тело ответа: {response.read()}')
