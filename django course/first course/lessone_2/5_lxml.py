import lxml.html
import requests

# get html
time_response = requests.get('https://www.utctime.net/')
# convert to tree
html_tree = lxml.html.document_fromstring(time_response.text)
# Ищем по шаблону
list_of_matches = html_tree.xpath('//*[@id="time2"]')
print(list_of_matches[0].text)
