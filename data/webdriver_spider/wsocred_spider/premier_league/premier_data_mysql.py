#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : premier_data_mysql.py
# @Author: sansi
# Python版本：3.6.5 
# @Date  : 2017/11/17

from common_tool.mysql_tool.mysql_tool import *
import re

# 插入交手记录
def insert_fight(dic):
    league_gid_str = get_league_info_by_name(dic["tournament"])
    match_date = dic["date"]
    score = dic["result"]

    home = del_space(dic["home"])
    away = del_space(dic["away"])
    date_flag = dic["date_flag"]

    main_team_gid = name_gid[home]
    custom_team_gid = name_gid[away]
    gid = get_snowflake_gid()

    sql = "insert into fight_record (gid,league_gid,match_date,score,main_team_gid,custom_team_gid,date_flag,create_time) values" \
          "("+str(gid)+","+str(league_gid_str)+",'"+date_format(str(match_date))+"','"+str(score)+\
          "',"+str(main_team_gid)+","+str(custom_team_gid)+",'"+str(date_flag)+"',NOW())"
    insert(sql)

#插入近期战绩
def insert_nearly_six(dic):
    league_gid_str = get_league_info_by_name(dic["tournament"])
    home = del_space(dic["home"])
    away = del_space(dic["away"])
    main_team_gid = get_team_info_by_name(home)
    custom_team_gid = get_team_info_by_name(away)
    match_date = date_format(dic["date"])
    score = dic["result"]
    home_gid = dic["home_gid"]
    away_gid = dic["away_gid"]
    wol = dic["wol"]

    if wol=="w":
        wol_str = "3"
    elif wol == "l":
        wol_str = "0"
    elif wol == "d":
        wol_str = "1"
    else:
        wol_str = "4"

    turn = dic["turn"]
    gid = get_snowflake_gid()

    sql = "insert into nearly_six_record (gid,league_gid,match_date,turn,score,main_team_gid,custom_team_gid," \
          "if_win,create_time,home_gid,away_gid) values ("+str(gid)+","+str(league_gid_str)+",'"+str(match_date)+"',"\
          +str(turn)+",'"+str(score)+"','"+str(main_team_gid)+"','"+str(custom_team_gid)+"','"+str(wol_str)+"',NOW(),"\
          +str(home_gid)+","+str(away_gid)+")"
    insert(sql)

#删除多个空格，保留一个
def del_space(str):
    return re.sub(' +', ' ', str)

#日-月-年 格式转换
#11-02-2017
def date_format(date):
    date = date.split("-")
    return date[2]+"-"+date[1]+"-"+date[0]

#根据标记判断是否插入新数据
def if_insert(home,away,date_flag):
    sql = "SELECT count(*) FROM fight_record WHERE date_flag = '"+str(date_flag)+"' " \
          "AND ((main_team_gid = "+str(home)+" AND custom_team_gid = "+str(away)+")" \
          "OR (main_team_gid = "+str(away)+" AND custom_team_gid = "+str(home)+" ))"
    result = query(sql)
    return result[0][0]