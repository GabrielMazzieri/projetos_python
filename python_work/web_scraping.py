import requests
from bs4 import BeautifulSoup

link = "https://www.apple.com/br/shop/buy-iphone/iphone-15-pro"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0"}

requisicao = requests.get(link, headers=headers)
print(requisicao)


site = BeautifulSoup(requisicao.text, "html.parser")

preco = site.find('label', id='817ca4e0-c1f2-11ee-9c52-1d38823e6860_label')
print(preco)