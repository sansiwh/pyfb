#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : premier_threesix_page.py
# @Author: sansi
# Python版本：3.6.5 
# @Date  : 2017/11/17

from selenium import webdriver
import time

# options = webdriver.ChromeOptions()
# options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"')
# options.add_argument('Host="www.bet365.com"')
# options.add_argument('Referer="https://www.bet365.com/"')
# options.add_argument('Cookie="aaat=am=0&at=00000000-0000-0000-0000-000000000000&ts=14-11-2017 02:21:26&v=2; bs=bt=1&mo=0&fs=0||&; session=processform=0&id=%7B4C37722F%2D0539%2D48CC%2D9096%2DC57356D1CB9A%7D; pstk=CBA025928D124ED8AF20329A6BB4C3A6000003; aps03=tzi=27&cg=0&ltwo=False&ao=1&cst=114&v=1&hd=Y&lng=10&cf=E&ct=42&oty=2&bst=1; rmbs=3; usdi=uqid=33465139%2DD6AC%2D4A63%2DA81B%2DFCBC35377EF2"')

browser = webdriver.Chrome()
browser.get('https://www.bet365.com/')
#点击简体中文
browser.find_element_by_css_selector("a[class=\"lpdgl\"]").click()
#点击足球
time.sleep(15)

browser.switch_to_window(browser.window_handles[0])
browser.find_element_by_css_selector("div.wn-FavouritesContainer  ~ div").click()

html = browser.page_source
#browser.close()
print(html)