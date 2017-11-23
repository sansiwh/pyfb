#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : premier_update_socre.py
# @Author: sansi
# Python版本：3.6.5 
# @Date  : 2017/11/23

from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.PhantomJS()
browser.get("https://soccer.hupu.com/schedule/England.html")
soup = BeautifulSoup(browser.page_source, "html.parser")
text = soup.find(text="vs")
turn = ""
for j in text.parent.parent.previous_siblings:
    jsoup = BeautifulSoup(str(j), "html.parser")
    if jsoup.font is not None:
        turn = jsoup.font.get_text()
        break
print(turn.replace("\t", "").replace("\n", "").replace(" ", ""))
browser.close()