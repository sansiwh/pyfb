#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : premier_home_page.py
# @Author: sansi
# Python版本：3.6.5 
# @Date  : 2017/11/16

from selenium import webdriver
from bs4 import BeautifulSoup
from data.webdriver_spider.wsocred_spider.premier_league.premier_data_mysql import *
import time

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

def get_head_to_head_json(html):
    turn = get_current_turn()
    head_to_head = {}
    # 获取球队11
    soup = BeautifulSoup(html, "html.parser")
    team_list = soup.find(class_="match-header").find_all("a")
    #根据英文名获取球队ID
    home_team_gid = get_team_info_by_name(team_list[0].get_text().replace("\n", ""))
    away_team_gid = get_team_info_by_name(team_list[1].get_text().replace("\n", ""))

    match_date_flag = soup.find(class_="match-header").find_all("dd")
    date_flag = match_date_flag[1].get_text()

    #根据主客队id和日期标记判断是否添加数据
    if_insert_ = if_insert(home_team_gid,away_team_gid,date_flag)
    if if_insert_ == 0:
        # 获取交手记录
        load=soup.find(id="previous-meetings-grid-wrapper").find(class_="loading-text")
        if load is None:#是否有交手记录
            fight_record = soup.find(id="previous-meetings-grid-wrapper").find_all("tr")
            for i in range(len(fight_record)):
                figth_match_obj = {}
                figth_match_obj["tournament"] = fight_record[i].find(class_="tournament").a.get_text()
                figth_match_obj["date"] = fight_record[i].find(class_="date").get_text()

                if fight_record[i].find(class_="team home winner") is None:
                    figth_match_obj["home"] = fight_record[i].find(class_="team home").a.get_text().replace("\n", "")
                else:
                    figth_match_obj["home"] = fight_record[i].find(class_="team home winner").a.get_text().replace("\n", "")

                figth_match_obj["result"] = fight_record[i].find(class_="result").get_text().replace("\n", "").replace(" ", "")

                if fight_record[i].find(class_="team away winner") is None:
                    figth_match_obj["away"] = fight_record[i].find(class_="team away").a.get_text().replace("\n", "")
                else:
                    figth_match_obj["away"] = fight_record[i].find(class_="team away winner").a.get_text().replace("\n", "")

                figth_match_obj["date_flag"] = date_flag
                insert_fight(figth_match_obj)

        # 获取近6场战绩 主队
        home_six_record = soup.find(id="team-fixtures-content-home-matches").find_all("tr")
        for i in range(len(home_six_record)):
            home_six_record_obj = {}
            home_six_record_obj["tournament"] = home_six_record[i].find(class_="tournament-link").get_text()

            if home_six_record[i].find(class_="team home") is None:
                home_six_record_obj["home"] = home_six_record[i].find(class_="team home winner").a.get_text()
            else:
                home_six_record_obj["home"] = home_six_record[i].find(class_="team home").a.get_text()

            home_six_record_obj["result"] = home_six_record[i].find(class_="result").a.get_text().replace("\n", "").replace(
                " ", "")
            home_six_record_obj["date"] = home_six_record[i].find(class_="date ta-right").get_text()

            if home_six_record[i].find(class_="team away") is None:
                home_six_record_obj["away"] = home_six_record[i].find(class_="team away winner").a.get_text()
            else:
                home_six_record_obj["away"] = home_six_record[i].find(class_="team away").a.get_text()

            if home_six_record[i].find(class_=" box w") is None:
                if home_six_record[i].find(class_=" box d") is None:
                    if home_six_record[i].find(class_=" box l") is None:
                        home_six_record_obj["wol"] = "u"
                    else:
                        home_six_record_obj["wol"] = home_six_record[i].find(class_=" box l").get_text()
                else:
                    home_six_record_obj["wol"] = home_six_record[i].find(class_=" box d").get_text()
            else:
                home_six_record_obj["wol"] = home_six_record[i].find(class_=" box w").get_text()

            home_six_record_obj["turn"] = turn
            insert_nearly_six(home_six_record_obj)

        # 获取近6场战绩 客队
        away_six_record = soup.find(id="team-fixtures-content-away-matches").find_all("tr")
        for i in range(len(away_six_record)):
            away_six_record_obj = {}
            away_six_record_obj["tournament"] = away_six_record[i].find(class_="tournament-link").get_text()

            if away_six_record[i].find(class_="team home") is None:
                away_six_record_obj["home"] = away_six_record[i].find(class_="team home winner").a.get_text()
            else:
                away_six_record_obj["home"] = away_six_record[i].find(class_="team home").a.get_text()

            away_six_record_obj["result"] = away_six_record[i].find(class_="result").a.get_text().replace("\n", "").replace(
                " ", "")
            away_six_record_obj["date"] = away_six_record[i].find(class_="date ta-left").get_text()

            if away_six_record[i].find(class_="team away") is None:
                away_six_record_obj["away"] = away_six_record[i].find(class_="team away winner").a.get_text()
            else:
                away_six_record_obj["away"] = away_six_record[i].find(class_="team away").a.get_text()

            if away_six_record[i].find(class_=" box w") is None:
                if away_six_record[i].find(class_=" box d") is None:
                    if away_six_record[i].find(class_=" box l") is None:
                        away_six_record_obj["wol"] = "u"
                    else:
                        away_six_record_obj["wol"] = away_six_record[i].find(class_=" box l").get_text()
                else:
                    away_six_record_obj["wol"] = away_six_record[i].find(class_=" box d").get_text()
            else:
                away_six_record_obj["wol"] = away_six_record[i].find(class_=" box w").get_text()

            away_six_record_obj["turn"] = turn
            insert_nearly_six(away_six_record_obj)
    return "插入完成"

if __name__ == '__main__':
    # 1 主页
    html = getPageInfo("https://www.whoscored.com/Regions/252/Tournaments/2/England-Premier-League")
    # 2 比赛列表
    preview_list = soup_data(html)
    #比赛headtohead页面
    for i in preview_list:
        html_detail = getPageInfo('https://www.whoscored.com'+i)
        json_result = get_head_to_head_json(html_detail)
        print(json_result)
        time.sleep(10)
