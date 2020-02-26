#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:19:50 2020

@author: pandeniidhenga
"""

#Find the price of any security

ticker = input("Input ticker: ")

import bs4
import requests
from bs4 import BeautifulSoup

#insert stock here
r=requests.get('https://finance.yahoo.com/quote/%'+ ticker)
soup=bs4.BeautifulSoup(r.text,"html.parser")

def parsePrice():
    r=requests.get('https://finance.yahoo.com/quote/'+ ticker)
    soup=bs4.BeautifulSoup(r.text,"html.parser")
    price=soup.find('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text
    return price

while True:
    print('The current price is ' + str(parsePrice()))