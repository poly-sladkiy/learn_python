from selenium import webdriver
from auth_vk_data import login, password
from time import sleep

url = 'https://www.vk.com'
driver = webdriver.Chrome(executable_path='./chromedriver')

try:
    driver.get(url)
    email_input = driver.find_element_by_id("index_email")
    email_input.clear()
    email_input.send_keys(f"{login}")

    pass_input = driver.find_element_by_id("index_pass")
    pass_input.clear()
    pass_input.send_keys(f"{password}")

    button = driver.find_element_by_id("index_login_button").click()
    # news = driver.find_element_by_id("l_nwsf").click()

    sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
