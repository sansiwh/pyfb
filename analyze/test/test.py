#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: sansi
# Python版本：3.6.5 
# @Date  : 2017/11/16
from selenium import webdriver
from bs4 import BeautifulSoup

# browser = webdriver.Chrome()
# browser.get('https://www.whoscored.com/Matches/1190320/Show/England-Premier-League-2017-2018-Arsenal-Tottenham')
#
# html = browser.page_source
# browser.close()
# print(html)

head_to_head={}
#获取球队11
soup = BeautifulSoup(open("mainpage.html"), "html.parser")
team_list = soup.find(class_="match-header").find_all("a")
head_to_head["home_team"] = team_list[0].get_text()
head_to_head["away_team"] = team_list[1].get_text()

#获取交手记录
fight_record = soup.find(id="previous-meetings-grid-wrapper").find_all("tr")
figth_obj = []
for i in range(len(fight_record)):
    figth_match_obj={}
    figth_match_obj["tournament"] = fight_record[i].find(class_="tournament").a.get_text()
    figth_match_obj["date"] = fight_record[i].find(class_="date").get_text()

    if fight_record[i].find(class_="team home winner") is None:
        figth_match_obj["home"] = fight_record[i].find(class_="team home").a.get_text()
    else:
        figth_match_obj["home"] = fight_record[i].find(class_="team home winner").a.get_text()

    figth_match_obj["result"] = fight_record[i].find(class_="result").get_text().replace("\n","").replace(" ","")

    if fight_record[i].find(class_="team away winner") is None:
        figth_match_obj["away"] = fight_record[i].find(class_="team away").a.get_text()
    else:
        figth_match_obj["away"] = fight_record[i].find(class_="team away winner").a.get_text()

    figth_obj.append(figth_match_obj)

head_to_head["fight_record"] = figth_obj

#获取近6场战绩 主队
home_six_record = soup.find(id="team-fixtures-content-home-matches").find_all("tr")
home_six_record_list = []
for i in range(len(home_six_record)):
    home_six_record_obj = {}
    home_six_record_obj["tournament"]=home_six_record[i].find(class_="tournament-link").get_text()

    if home_six_record[i].find(class_="team home") is None:
        home_six_record_obj["home"] = home_six_record[i].find(class_="team home winner").a.get_text()
    else:
        home_six_record_obj["home"] = home_six_record[i].find(class_="team home").a.get_text()

    home_six_record_obj["result"] = home_six_record[i].find(class_="result").a.get_text().replace("\n","").replace(" ","")
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

    home_six_record_list.append(home_six_record_obj)

head_to_head["home_six"]=home_six_record_list

#获取近6场战绩 客队
away_six_record = soup.find(id="team-fixtures-content-away-matches").find_all("tr")
away_six_record_list = []
for i in range(len(away_six_record)):
    away_six_record_obj={}
    away_six_record_obj["tournament"] = away_six_record[i].find(class_="tournament-link").get_text()


    if away_six_record[i].find(class_="team home") is None:
        away_six_record_obj["home"] = away_six_record[i].find(class_="team home winner").a.get_text()
    else:
        away_six_record_obj["home"] = away_six_record[i].find(class_="team home").a.get_text()

    away_six_record_obj["result"] = away_six_record[i].find(class_="result").a.get_text().replace("\n", "").replace(" ","")
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
    away_six_record_list.append(away_six_record_obj)

head_to_head["away_six"]=away_six_record_list

print(head_to_head)