#!/opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
# <xbar.title>GBP Currency Tracker</xbar.title>
# <xbar.version>1.0</xbar.version>
# <xbar.author>Fahad Usman</xbar.author>
# <xbar.author.github>fahadshery</xbar.author.github>
# <xbar.desc>Keep an eye on GBP currency exchange rates</xbar.desc>
# <xbar.dependencies>python3</xbar.dependencies>

import requests
from bs4 import BeautifulSoup
from urllib.request import Request
from urllib.request import urlopen
import json


################## UBL #############################
source = requests.get('https://www.ubluknetremit.com/Home.aspx').text
soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())
rates = soup.find_all('span', id='pkr_rate')
print(f"UBL: {rates[0].text}")

################## Google ##########################
source = requests.get(
    'https://gbp.fxexchangerate.com/pkr/1-currency-rates.html').text
soup = BeautifulSoup(source, 'lxml')
rates = soup.find_all("div", {"class": "fxtoday"})
# print(rates)
result = float(rates[0].text.split()[1][4:])
# print(result)
print(f"GGL: {result:.2f}")

################## XE ##########################
source = requests.get(
    'https://www.xe.com/currencyconverter/convert/?Amount=1&From=GBP&To=PKR').text
soup = BeautifulSoup(source, 'lxml')
rates = soup.find_all('p', class_='result__BigRate-sc-1bsijpp-1 iGrAod')
# print(rates)
print(f"XE: {rates[0].text[:-19]}")

################## Remitly ##########################
source = requests.get('https://www.remitly.com/gb/en/pakistan').text
soup = BeautifulSoup(source, 'lxml')
rates = soup.find_all('h2', class_='fg6m42n')
print(f"RM: {rates[2].text[:-3]}")

################## TRANSFERWISE ##########################

TRANSFERWISE_KEY = "dad99d7d8e52c2c8aaf9fda788d8acdc"

# Replace with desired currencies
currency_from = 'GBP'
currency_to = 'PKR'

url = f"https://transferwise.com/api/v1/payment/calculate?amount=1&amountCurrency=source&hasDiscount=false&isFixedRate=false&isGuaranteedFixedTarget=false&sourceCurrency={currency_from}&targetCurrency={currency_to}"

req = Request(url)
req.add_header('X-Authorization-key', TRANSFERWISE_KEY)

result = json.loads(urlopen(req).read())['transferwiseRate']

print(f"TW: {result:.2f}")
print("---")
print(f"From: {currency_from}")
