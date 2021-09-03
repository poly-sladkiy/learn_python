from selenium import webdriver
from time import sleep

url = 'https://www.instagram.com'
driver = webdriver.Chrome(executable_path='./chromedriver')

try:
    driver.get(url)
    sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
