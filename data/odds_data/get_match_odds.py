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
import time
import random

# headers = {
#         "authority":"www.whoscored.com",
#         "Connection": "close",
#         "referer":"https://www.whoscored.com/Regions/252/Tournaments/2/England-Premier-League",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
#         "Cookie": "visid_incap_774904=ITmb3E5gQkG8FhIF6IlXFamVvlkAAAAAQUIPAAAAAAAciEtKa9+kQOcD4ytW+1xx; permutive-id=cfb4ff64-f96a-4874-9f9a-9bcb79ff8619; __gads=ID=b04d007e9e38558d:T=1506186977:S=ALNI_MblHWBHHibDSkamBMNd9sX9cPHWLg; vl=1:-8.00|2:CN|3:HUBEI|4:|5:HUBEI/|6:HUBEI/WUHAN|7:430022|!0; vd=chinatelecom.com.cn; vg=072a9421-a356-4e6f-a628-57b9d0f973fa; ip=1873766147; permutive-session=%7B%22session_id%22%3A%22eff418ee-4aa4-4462-afbe-112e0aa18a0f%22%2C%22last_updated%22%3A%222017-09-23T17%3A32%3A34.862Z%22%7D; _psegs=%5B1920%2C1930%2C2126%2C2441%2C2300%2C1956%2C1907%5D; incap_ses_431_774904=q68IblEKUGgcHFcW0Tj7Bc9vylkAAAAA6nRAEFUPFu493Z/6QUkRuA==; _ga=GA1.2.199745529.1505662476; _gid=GA1.2.725387932.1506437635"
#     }

headers = {
        "Connection": "keep-alive",
        "Referer": "https://www.bet365.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
        "Cookie": "aaat=am=0&at=00000000-0000-0000-0000-000000000000&ts=04-10-2017 15:32:54&v=2; session=processform=0&id=%7BB0AAD56D%2D1969%2D45DC%2D8730%2DC254659B2E47%7D; pstk=FBC149251E01454B832A77798A0C4217000003; usdi=uqid=A24F4DF6%2D7AF4%2D4EB6%2D8F79%2D4A9FB0F1C8FB; aps03=tzi=27&oty=2&bst=1&hd=Y&lng=10&cf=E&ct=42&cst=114&v=1&cg=1&ltwo=False&ao=1; rmbs=3; bs=bt=1&mo=0&fs=0||&"
    }

collection = get_mondb().match_odd_data
# my_headers = [
#     "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0"
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
#     "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
# ]

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

    #随机获取浏览器信息
    # random_header = random.choice(my_headers)
    #设置随机信息
    # headers['User-Agent'] = random_header
    # print(headers)

    soup = get_soup(headers,url);
    return soup

#查询大于某一时间的所有比赛
def get_match_odds_from_db(time):
    list = collection.find({"match_time":{"$gte": time}}).sort([("match_id",1)])
    return list

#根据参数传递的列表，插入所有比赛的赔率数据
#解析赔率数据
def get_odds_data(id):
    soup = get_match_odds_soup(id)
    match_odd_data_info = {}
    match_odd_data_info["match_id"] = id
    #赔率数据类型1，ID时间没有类型
    match_odd_data_info["data_type"] = 1

    final_result = re.findall(r"NA=全场赛果(.+?)NA=双胜彩", str(soup))
    match_odd_data_info["final_result"] = final_result

    right_score = re.findall(r"NA=正确得分(.+?)NA=半/全场", str(soup))
    match_odd_data_info["right_score"] = right_score
    print(match_odd_data_info)
    get_mondb().match_odd_data.insert_one(match_odd_data_info)

#查询所有赔率信息
def get_all_odds_info():
    list = collection.find({"data_type": 1}).sort([("match_id", 1)])
    return list

if __name__ == '__main__':
    #查询并插入比赛列表
    # match_odd_time_list = get_match_list()
    # print(match_odd_time_list)
    # insert_odd_data(match_odd_time_list)

    #添加赔率信息
    # list = get_match_odds_from_db('20171014123000');
    # print(list.count())
    # get_odds_data(list[19]["match_id"])

    print("---------")
    for i in get_all_odds_info():
        print(i)
