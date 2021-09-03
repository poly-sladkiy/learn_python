# from selenium import webdriver
from time import sleep
from seleniumwire import webdriver

from proxy_auth_data import login, password, ip, port

url = 'https://www.instagram.com'

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows10; Intel Mac OS X 10_15_7)")
options.add_argument("--proxy-server=PROXY")

proxy_options = {
    "proxy": {
        "https": f"http://{login}:{password}@{ip}:{port}"
    }
}

driver = webdriver.Chrome(
    executable_path='./chromedriver',
    seleniumwire_options=proxy_options,
)

try:
    driver.get("https://2ip.ru")
    sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
