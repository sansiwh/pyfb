#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : premier_threesix_page.py
# @Author: sansi
# Python版本：3.6.5 
# @Date  : 2017/11/17

from selenium import webdriver
import time
from bs4 import BeautifulSoup
from data.spider_tool.proxy import *
from selenium.webdriver.common.proxy import Proxy

browser = webdriver.Chrome()
#进入列表页
def match_list_html():
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    # }

    #ip_list_port = getIpList(headers)
    #random_ip = getRandomIp(ip_list_port)
    # chromeOptions = webdriver.ChromeOptions()
    # chromeOptions.add_argument('--proxy-server=http://147.75.208.57:20000')
    #
    # browser = webdriver.Chrome(chrome_options=chromeOptions)

    browser.get('https://www.bet365.com/')
    try:
        #点击简体中文
        browser.find_element_by_css_selector("a[class=\"lpdgl\"]").click()

        #点击足球
        time.sleep(15)

        browser.find_element_by_css_selector("div.wn-FavouritesContainer  ~ div").click()

        #点击英超联赛
        time.sleep(10)
        element = browser.find_elements("css selector",".sm-Market ")[2]
        element = element.find_elements("css selector",".sm-CouponLink_Label ")[0]
        element.click()
        time.sleep(10)

        # 英超列表首页
        elements = browser.find_elements_by_css_selector('.sl-CouponFixtureLinkParticipant ')
        loop_data(elements,0)

    except:
        print("页面异常，请检查网页是否可以正常打开")
        browser.close()

#获取每场比赛信息
def loop_data(elements,index):
    try:
        elements[index].click()
        time.sleep(10)
        print(browser.page_source)

        element = browser.find_element("css selector", ".cl-BreadcrumbTrail_BackButton ")
        element.click()
        time.sleep(10)

        elements = browser.find_elements_by_css_selector('.sl-CouponFixtureLinkParticipant ')
        loop_data(elements,index + 3)
    except:
        print("赔率抓取完成")
        browser.close()

#获取賠率信息并保存
def get_odd_info(html):
    soup = BeautifulSoup(open("mainpage.html",'rb'), "html.parser")
    print(soup)

if __name__ == '__main__':
    match_list_html()



