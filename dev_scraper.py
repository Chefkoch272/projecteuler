import requests
from bs4 import BeautifulSoup

prob_n = 123

URL_base = 'https://projecteuler.net/problem='
URL = URL_base + str(prob_n)
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

prob_title = soup.find(id='problem_info').find('h3').text
prob_info = soup.find(id='content').find('h2').text
# Todo: Find solution to display special formats, e.g. superscript, correctly.
# prob_description = soup.find(class_='problem_content').text

print(prob_title)
print(prob_info)
# print(prob_description)