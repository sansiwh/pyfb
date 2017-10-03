#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : get_match_odds.py
# @Author: sansi
# Python版本：3.6.5 
# @Date  : 2017/9/28
# 抓取比赛赔率

from data.spider_tool.common_tool import *
import re
from data.spider_tool.mongo_db import *

headers = {
        "Host": "www.bet365.com",
        "Connection": "keep-alive",
        "Referer": "https://www.bet365.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        "Cookie": "aaat=am=0&at=00000000-0000-0000-0000-000000000000&ts=28-09-2017 02:45:06&v=2; bs=bt=1&mo=0; aps03=tzi=27&cg=1&ltwo=False&ao=1&cst=114&v=1&hd=Y&lng=10&cf=E&ct=42&oty=2&bst=1; rmbs=3; usdi=uqid=33465139%2DD6AC%2D4A63%2DA81B%2DFCBC35377EF2; pstk=2D41156E9D1B5D91A76654AB2763B18F000003; session=processform=0&id=%7BFAE7576E%2D1249%2D43AF%2DB4FE%2DFAD092784B92%7D&lgs=1&p=0&fms=1"
    }

#获取周末英超联赛比赛列表   从列表中获取比赛参数
#获取列表后按照时间  key:20170707 value:list
def get_match_list():
    url = "https://www.bet365.com/SportsBook.API/web?lid=10&zid=0&pd=%23AC%23B1%23C1%23D14%23E33577329%23F2%23R1%23&cid=42&ctid=42"
    soup = get_soup(headers, url);

    re_list = re.findall(r";BC(.+?)#R1#P", str(soup))
    match_odd_time_list = []
    for i in re_list:
        match_odd_time = {}
        match_time = re.findall(r"=(.+?);PD", i)
        match_id = re.findall(r"#D8#(.+?)#F3", i)
        match_odd_time["match_id"] = match_id[0]
        match_odd_time["match_time"] = match_time[0]
        match_odd_time_list.append(match_odd_time)
    return match_odd_time_list;

#数据插入赔率表
def insert_odd_data(list):
    get_mondb().match_odd_data.insert_many(list)

#获取每场比赛的赔率数据
def get_match_odds_soup(url_id):
    url = "https://www.bet365.com/SportsBook.API/web?lid=10&zid=0&pd=%23AC%23B1%23C1%23D8%23"+url_id+"%23F3%23R1%23P%5E14%23Q%5E33577329%23&cid=42&ctid=42"
    soup = get_soup(headers,url);
    return soup

#查询大于某一时间的所有比赛
def get_match_odds_from_db(time):
    collection = get_mondb().match_odd_data
    list = collection.find({"match_time":{"$gte": time}})
    return list

if __name__ == '__main__':
    #查询并插入比赛列表
    #match_odd_time_list = get_match_list()
    #print(match_odd_time_list)
    #insert_odd_data(match_odd_time_list)

    list = get_match_odds_from_db('20171014123000');
    print(list[0]['match_id'])
    print(get_match_odds_soup(list[0]['match_id']))
    # for i in list:
    #     print(i['match_id'])
    #     print(i['match_time'])