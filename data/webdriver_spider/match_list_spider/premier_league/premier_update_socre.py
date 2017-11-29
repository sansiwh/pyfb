#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : premier_update_socre.py
# @Author: sansi
# Python版本：3.6.5 
# @Date  : 2017/11/23

import re
from selenium import webdriver
from bs4 import BeautifulSoup
from common_tool.mysql_tool.mysql_tool import *

browser = webdriver.Firefox()
browser.get("https://soccer.hupu.com/schedule/England.html")
soup = BeautifulSoup(browser.page_source, "html.parser")
text = soup.find(text="vs")
turn = ""
for j in text.parent.parent.previous_siblings:
    jsoup = BeautifulSoup(str(j), "html.parser")
    if jsoup.font is not None:
        turn = jsoup.font.get_text()
        break
turn_str = turn.replace("\t", "").replace("\n", "").replace(" ", "")
turn_str = re.findall(r"第(.+?)轮",turn_str)[0]

gid = get_snowflake_gid()
#sql = "insert into common_config (gid,key,'value',des,create_time) values ("+str(gid)+",'premier_turn',"+turn_str+",'',NOW())"
sql="update common_config set update_time = NOW(), `value` = " + turn_str
update(sql)
#print(sql)
browser.close()