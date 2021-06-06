import requests
from bs4 import BeautifulSoup

class problem(object):
    def __init__(self, number):
        URL_base = 'https://projecteuler.net/problem='
        URL = URL_base + str(number)
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')

        self.info = soup.find(id='content').find('h2').text
        self.title = soup.find(id='problem_info').find('h3').text