import requests
from bs4 import BeautifulSoup as b

URL = 'https://finance.ua/ua/crypto'
r = requests.get(URL)
soup = b(r.text, 'html.parser')
kurs = soup.find_all('td', class_='CoinsListstyles__Price-sc-1c8245s-25 fYNuHQ')
name = soup.find_all('p', class_='CoinsListstyles__Code-sc-1c8245s-24 lgioIM')
clear_kurs = [c.text for c in kurs]
clear_name = [c.text for c in name]
print (kurs)
print (name)