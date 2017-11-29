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
import datetime
from common_tool.mysql_tool.mysql_tool import *
import traceback

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

    except :
        traceback.print_exc()
        print("页面异常，请检查网页是否可以正常打开")
        browser.close()

#获取每场比赛信息
def loop_data(elements,index):
    try:
        elements[index].click()
        time.sleep(10)

        #点击全部比分
        element = browser.find_elements("css selector", ".gl-MarketGroup_BBarItem ")
        element[1].click()
        get_odd_info(browser.page_source)

        element = browser.find_element("css selector", ".cl-BreadcrumbTrail_BackButton ")
        element.click()
        time.sleep(10)

        elements = browser.find_elements_by_css_selector('.sl-CouponFixtureLinkParticipant ')
        loop_data(elements,index + 3)
    except:
        traceback.print_exc()
        print("赔率抓取完成")
        browser.close()

#获取賠率信息并保存
def get_odd_info(html):
    #soup = BeautifulSoup(open("mainpage.html",'rb'), "html.parser")
    soup = BeautifulSoup(html, "html.parser")
    match_date = soup.find(class_="cm-MarketGroupExtraData_TimeStamp ").get_text()
    three_odd_list = soup.find(class_="gl-MarketGroupContainer ").find_all("span")
    home_team = three_odd_list[0].get_text()
    away_team = three_odd_list[4].get_text()

    #根据主客队时间查询match_id
    year = datetime.datetime.now().strftime('%Y')
    month = match_date.split("月")[0]
    day_str = match_date.split("月")[1].split("日")[0]
    if len(day_str) == 2:
        day = day_str
    else:
        day = "0" + day_str
    match_date = month + "-" + day
    date = year + "-" + match_date
    param = {}
    param["home_team_name"] = home_team
    param["away_team_name"] = away_team
    param["match_date"] = date
    match_id = get_match_id_by_name(param)
    print(match_id)

    type_3 = three_odd_list[1].get_text()
    type_1 = three_odd_list[3].get_text()
    type_0 = three_odd_list[5].get_text()

    #插入胜负赔率
    gid = get_snowflake_gid()
    sql = "insert into three_odd_info (gid,match_gid,type,odd,create_time) values (" + str(gid) + "," + str(match_id) + ",3," + str(type_3)+",NOW())"
    insert(sql)

    gid = get_snowflake_gid()
    sql = "insert into three_odd_info (gid,match_gid,type,odd,create_time) values (" + str(gid) + "," + str(match_id) + ",1," + str(type_1) + ",NOW())"
    insert(sql)

    gid = get_snowflake_gid()
    sql = "insert into three_odd_info (gid,match_gid,type,odd,create_time) values (" + str(gid) + "," + str(match_id) + ",0," + str(type_0) + ",NOW())"
    insert(sql)

    win_ping_divs = soup.find_all(class_="gl-Market3 gl-Market_General gl-Market_PWidth-33-3333 ")
    #主胜赔率
    socre_odd_win = win_ping_divs[0].find_all(class_="gl-ParticipantCentered gl-Participant_General gl-ParticipantCentered_NoHandicap ")
    for i in socre_odd_win:
        gid = get_snowflake_gid()
        score = i.find(class_="gl-ParticipantCentered_Name").get_text()
        odd = i.find(class_="gl-ParticipantCentered_Odds").get_text()
        sql = "insert into score_odd_info (gid,match_gid,type,score,odd,create_time) values (" + str(gid) + "," + str(match_id) + ",3,'"+str(score)+ "','" + str(odd) + "',NOW())"
        insert(sql)

    # 平局赔率
    socre_odd_ping = win_ping_divs[1].find_all(class_="gl-ParticipantCentered gl-Participant_General gl-ParticipantCentered_NoHandicap ")
    for i in socre_odd_ping:
        gid = get_snowflake_gid()
        score = i.find(class_="gl-ParticipantCentered_Name").get_text()
        odd = i.find(class_="gl-ParticipantCentered_Odds").get_text()
        sql = "insert into score_odd_info (gid,match_gid,type,score,odd,create_time) values (" + str(gid) + "," + str(match_id) + ",1,'" + str(score) + "','" + str(odd) + "',NOW())"
        insert(sql)

    # 客胜赔率
    lose_divs = soup.find(class_="gl-Market3 gl-Market_General gl-Market_PWidth-33-3333 gl-Market_LastInRow ")
    socre_odd_lose = lose_divs.find_all(class_="gl-ParticipantCentered gl-Participant_General gl-ParticipantCentered_NoHandicap ")
    for i in socre_odd_lose:
        gid = get_snowflake_gid()
        score = i.find(class_="gl-ParticipantCentered_Name").get_text()
        odd = i.find(class_="gl-ParticipantCentered_Odds").get_text()
        sql = "insert into score_odd_info (gid,match_gid,type,score,odd,create_time) values (" + str(gid) + "," + str(match_id) + ",0,'" + str(score) + "','" + str(odd) + "',NOW())"
        insert(sql)


if __name__ == '__main__':
    match_list_html()
    #get_odd_info()



