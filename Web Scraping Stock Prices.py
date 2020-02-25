#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 12:32:54 2020

@author: pandeniidhenga
"""

import bs4
import requests
from bs4 import BeautifulSoup

#run file
#r=requests.get('string web link here')
r=requests.get('https://finance.yahoo.com/quote/FB?p=FB')
#soup=bs4.BeautifulSoup(r.text,"xml")
soup=bs4.BeautifulSoup(r.text,"html.parser")
#if later steps don't work use html.parser instead of xml
#check out soup 
soup

#use inspect element to find the div and class of the stock price, 
#copy and paste into soup.find_all
soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})
#find out where the price is using inspect element, here it's "span"
soup.find('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span')
#to find the price only add ".text to the end"
soup.find('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text

#FINAL VERSION:
import bs4
import requests
from bs4 import BeautifulSoup

#insert stock here
r=requests.get('https://finance.yahoo.com/quote/FB?p=FB')
soup=bs4.BeautifulSoup(r.text,"html.parser")


def parsePrice():
    r=requests.get('https://finance.yahoo.com/quote/FB?p=FB')
    soup=bs4.BeautifulSoup(r.text,"html.parser")
    price=soup.find('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'}).find('span').text 
    return price

while True:
    print('The current price is ' + str(parsePrice()))