# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    target = 'http://bwf.tournamentsoftware.com/player-profile/39ec811a-3bdf-4e29-93e9-cd1f0bd65990/tournaments/2019'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html)
    matchGroup = bf.find_all('li', class_='match-group__item')
    print(matchGroup[0])
