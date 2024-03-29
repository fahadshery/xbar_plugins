#!/usr/bin/python3
# DO NOT USE IT AFTER MACBOOKS UPDATE /opt/homebrew/bin/python3
# -*- coding: utf-8 -*-
# <xbar.title>GBP Currency Tracker</xbar.title>
# <xbar.version>1.0</xbar.version>
# <xbar.author>Fahad Usman</xbar.author>
# <xbar.author.github>fahadshery</xbar.author.github>
# <xbar.desc>Keep an eye on GBP currency exchange rates</xbar.desc>
# <xbar.dependencies>python3</xbar.dependencies>

import requests
from bs4 import BeautifulSoup
# from urllib.request import Request
# from urllib.request import urlopen
import json

################## Bank of England Base Rate % #############################
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(
    'https://www.bankofengland.co.uk/boeapps/database/Bank-Rate.asp', headers=headers).text

# soup = BeautifulSoup(response, 'html.parser')
# rates = soup.find("span", id="srate")
soup = BeautifulSoup(response, 'lxml')
# rates = str(soup.find('p', class_='stat-figure'))
value = soup.select_one('p[class="stat-figure"]').get_text()
print(f"BoE%: {value}")
# print(value)
# result = float(rates.split("<")[0])
# print(rates)

################## UBL #############################
# source = requests.get('https://www.ubluknetremit.com/', headers=headers).text
# soup = BeautifulSoup(source, 'lxml')
# f = open( 'ubl_value.txt', 'w' )
# f.write( source )
# f.close()
# print(soup.prettify())
# rates = soup.find_all('span', id='pkr_rate')
# print(rates)
# print(f"UBL: {rates[0].text}")

################## Google ##########################

response = requests.get(
    'https://gbp.fxexchangerate.com/pkr/1-currency-rates.html', headers=headers).text

# soup = BeautifulSoup(response, 'html.parser')
# rates = soup.find("span", id="srate")
soup = BeautifulSoup(response, 'lxml')
rates = str(soup.find('span', id='srate')).split(">")[1]
result = float(rates.split("<")[0])
# print(rates)


# soup = BeautifulSoup(response, 'lxml')
# print(soup)
# rates = soup.find_all("div", {"class": "fxtoday"})
# print(rates.next_sibling())
# print(rates[0])
# print(type(rates))
# rates_str = str(rates).split()[1]
# result = float(rates.text.split())
# result = float(rates[0].text.split()[1][4:])
# print(rates_str)
print(f"GGL: {result:.2f}")

################## XE ##########################

source = requests.get(
    'https://www.xe.com/currencyconverter/convert/?Amount=1&From=PKR&To=GBP', headers=headers).text

soup = BeautifulSoup(source, 'lxml')
# f = open( 'xe.txt', 'w' )
# f.write( str(source) )
# f.close()
# print(soup.prettify)
rates = soup.find_all(class_='unit-rates___StyledDiv-sc-1dk593y-0 iGxfWX')
# print(rates)
# print(str(rates[0]).split(">"))
split_array_value = str(rates[0]).split(">")[2]
# print(split_array_value)
extracted_rate = split_array_value.split("<")[0].split("=")[1].split(" ")[1]
# print(extracted_rate)
# print(split_array_value[1].split("<")[0])
print(f"XE: {extracted_rate}")

################## Remitly ##########################
source = requests.get('https://www.remitly.com/gb/en/pakistan').text
soup = BeautifulSoup(source, 'lxml')
rates = soup.find_all('h2', class_='f1xrk329')
# print(rates)
print(f"RM: {rates[2].text[:-3]}")

################## TRANSFERWISE ##########################

# TRANSFERWISE_KEY = "dad99d7d8e52c2c8aaf9fda788d8acdc"

# # Replace with desired currencies
# currency_from = 'GBP'
# currency_to = 'PKR'

# url = f"https://transferwise.com/api/v1/payment/calculate?amount=1&amountCurrency=source&hasDiscount=false&isFixedRate=false&isGuaranteedFixedTarget=false&sourceCurrency={currency_from}&targetCurrency={currency_to}"

# req = Request(url)
# print(req)
# req.add_header('X-Authorization-key', TRANSFERWISE_KEY)
# print(json.loads(urlopen(req).read()))
# result = json.loads(urlopen(req).read())
# print(result)
# print(f"TW: {result:.2f}")
# print("---")
# print(f"From: {currency_from}")

################## WESTERNUNINION ##########################

# west_url = 'https://www.westernunion.com/gb/en/web/send-money/start?ReceiveCountry=PK&ISOCurrency=PKR&SendAmount=1&FundsOut=BA&FundsIn=WUPay'
# response = requests.get(west_url, headers=headers)
# print(response.text())
# soup = BeautifulSoup(response, 'html.parser')
# rates = soup.find("span", id="smoExchangeRate")

# # soup = BeautifulSoup(response, 'lxml')
# # print(soup)
# # rates = soup.find('span', id='smoExchangeRate')
# print(rates)
