from selenium import webdriver
from time import sleep

url = 'https://www.instagram.com'

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows10; Intel Mac OS X 10_15_7)")

driver = webdriver.Chrome(
    executable_path='./chromedriver',
    options=options,
)

try:
    driver.get(url)
    sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
