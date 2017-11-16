#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : premier_home_page.py
# @Author: sansi
# Python版本：3.6.5 
# @Date  : 2017/11/16

from selenium import webdriver
from bs4 import BeautifulSoup

def getPageInfo(url):
    browser = webdriver.Chrome()
    browser.get(url)

    html = browser.page_source
    browser.close()
    return html

#获取已有priview比赛的列表111
def soup_data(html):
    #open(mainpage.html)
    soup = BeautifulSoup(html, "html.parser")
    match_list_html = soup.find_all(class_="result-4 rc")
    #有preview的列表
    preview_list=[]
    for i in match_list_html:
        try:
            preview_list.append(i["href"])
            print(i["href"])
        except:
            print("")

    return preview_list

def get_head_to_head_url(html):
    print(html)

if __name__ == '__main__':
    #主页
    html = getPageInfo("https://www.whoscored.com/Regions/252/Tournaments/2/England-Premier-League")
    #比赛列表
    preview_list = soup_data(html)
    #比赛headtohead页面
    for i in preview_list:
        html_detail = getPageInfo('https://www.whoscored.com'+i)