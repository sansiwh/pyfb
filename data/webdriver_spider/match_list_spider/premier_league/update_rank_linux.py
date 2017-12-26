#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : update_rank_linux.py
# @Author: sansi
# Python版本：3.6.5
# @Date  : 2017/12/05

import re
from pyvirtualdisplay import Display
from selenium import webdriver
from bs4 import BeautifulSoup
from common_tool.mysql_tool.mysql_tool import *

display = Display(visible=0, size=(800,600))
display.start()
browser = webdriver.Firefox()

def update_rank():
    browser.get("https://soccer.hupu.com/table/England.html")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    trs = soup.find(attrs={'id':'main_table'}).find("tbody").find_all("tr")

    #查询积分表最大比赛场次，与轮数对比，如果最大比赛场次大于已有记录最大轮次，则抓取所有做插入操作
    #如果最大比赛场次等于已有记录最大轮次，则对该轮进行更新操作
    match_list = []
    for i in trs :
        tr = BeautifulSoup(str(i), "html.parser")
        match_num = tr.find_all("td")[3].get_text()
        match_list.append(int(match_num))
    current_turn = max(match_list)

    #查询当前rank表最大轮数
    sql = "select turn from league_rank_info ORDER BY turn desc LIMIT 1"
    result = query(sql)
    db_turn  = result[0][0]

    if current_turn > db_turn : #抓取轮数大于数据库最大轮数则全部添加
        insert_all_rank(trs,current_turn)
    else:#轮数相等则更新
        update_all_rank(trs,current_turn)

def insert_all_rank(trs,current_turn):
    for i in trs :
        tr = BeautifulSoup(str(i), "html.parser")
        gid = get_snowflake_gid()
        league_gid = "375414018631794688"
        team_str = tr.find_all("td")[2].find("a").get_text()
        team_gid = get_team_info_by_name(team_str)
        rank_num = tr.find_all("td")[0].get_text()
        win_num = tr.find_all("td")[4].get_text()
        tie_num = tr.find_all("td")[5].get_text()
        lose_num = tr.find_all("td")[6].get_text()
        win_goal = tr.find_all("td")[7].get_text()
        lose_goal = tr.find_all("td")[8].get_text()
        point = tr.find_all("td")[14].get_text()
        match_num = tr.find_all("td")[3].get_text()
        turn = current_turn

        sql = "insert into league_rank_info (gid,league_gid,team_gid,rank_num,win_num,tie_num,lose_num,win_goal,lose_goal,point,turn,match_num) values " \
              "("+str(gid)+","+str(league_gid)+","+str(team_gid)+","+str(rank_num)+","+str(win_num)+","+str(tie_num)+","+str(lose_num)+","+str(win_goal)+","+\
              str(lose_goal)+","+str(point)+","+str(turn)+","+str(match_num)+")"
        insert(sql)

def update_all_rank(trs,current_turn):
    for i in trs :
        tr = BeautifulSoup(str(i), "html.parser")
        team_str = tr.find_all("td")[2].find("a").get_text()
        team_gid = get_team_info_by_name(team_str)
        rank_num = tr.find_all("td")[0].get_text()
        win_num = tr.find_all("td")[4].get_text()
        tie_num = tr.find_all("td")[5].get_text()
        lose_num = tr.find_all("td")[6].get_text()
        win_goal = tr.find_all("td")[7].get_text()
        lose_goal = tr.find_all("td")[8].get_text()
        point = tr.find_all("td")[14].get_text()
        match_num = tr.find_all("td")[3].get_text()

        sql = "update league_rank_info set rank_num = " + str(rank_num) + ",win_num = " + str(win_num) + ",tie_num = " + str(tie_num) + ",lose_num = "+\
        str(lose_num)+",win_goal = " + str(win_goal) + ",lose_goal = " + str(lose_goal) + ",point = "+str(point) + ",match_num = " + str(match_num) +\
              " where turn="+str(current_turn)+" and  team_gid = " + str(team_gid)

        update(sql)


try:
    update_rank()
    browser.close()
    display.stop()
except:
    browser.close()
    display.stop()