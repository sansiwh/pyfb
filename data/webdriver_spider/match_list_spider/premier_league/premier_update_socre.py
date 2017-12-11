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
from common_tool.log.logger import *
import traceback

browser = webdriver.Firefox()
#更新轮数
def update_turn():
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
    return turn_str

#根据轮数更新比分
def update_score(turn):
    browser.get("https://soccer.hupu.com/schedule/England.html")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    table = soup.find_all(["table"])[turn - 1]
    trs = table.find_all(attrs={'name':'tr_title'})
    for i in trs:
        tr = BeautifulSoup(str(i), "html.parser")

        # 比分
        score = tr.find_all(["td"])[4]
        score_ = BeautifulSoup(str(score), "html.parser")
        score_str = score_.find(["a"]).get_text().replace(" ", "")

        #比分不是VS就更新
        if score_str != "vs":
            #轮数
            turn_num = tr.find_all(["td"])[2]
            turn_str = str(turn_num).replace("\t", "").replace("\n", "").replace(" ", "")
            turn_str = re.findall(r"第(.+?)轮", turn_str)[0]

            #主队
            home = tr.find_all(["td"])[3]
            home_ = BeautifulSoup(str(home), "html.parser")
            home_gid = get_team_info_by_name(home_.find(["a"]).get_text())

            #客队
            away = tr.find_all(["td"])[5]
            away_ = BeautifulSoup(str(away), "html.parser")
            away_gid = get_team_info_by_name(away_.find(["a"]).get_text())

            update("update match_info set match_time = '" + str(score_str) +
                  "' where turn=" + str(turn_str) + " and main_team_gid = " +
                  str(home_gid) + " and custom_team_gid = " + str(away_gid))


try:
    turn_str = update_turn()
    update_score(int(turn_str))
    update_score(int(turn_str) - 1) #防止漏掉，把上一轮也更新一次
    browser.close()
except:
    browser.close()
    get_logger().debug(traceback.print_exc())