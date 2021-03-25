import requests
from bs4 import BeautifulSoup

URL = 'https://projecteuler.net/problem=8'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='problem_info')

print(results.prettify())