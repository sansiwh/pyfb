#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : get_match_odds.py
# @Author: sansi
# Python版本：3.6.5 
# @Date  : 2017/9/28
# 抓取比赛赔率

from data.spider_tool.common_tool import *
import re

headers = {
        "Host": "www.bet365.com",
        "Connection": "keep-alive",
        "Referer": "https://www.bet365.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        "Cookie": "aaat=am=0&at=00000000-0000-0000-0000-000000000000&ts=28-09-2017 02:45:06&v=2; bs=bt=1&mo=0; aps03=tzi=27&cg=1&ltwo=False&ao=1&cst=114&v=1&hd=Y&lng=10&cf=E&ct=42&oty=2&bst=1; rmbs=3; usdi=uqid=33465139%2DD6AC%2D4A63%2DA81B%2DFCBC35377EF2; pstk=2D41156E9D1B5D91A76654AB2763B18F000003; session=processform=0&id=%7BFAE7576E%2D1249%2D43AF%2DB4FE%2DFAD092784B92%7D&lgs=1&p=0&fms=1"
    }

#获取周末英超联赛比赛列表   从列表中获取比赛参数
def get_match_list():
    url = "https://www.bet365.com/SportsBook.API/web?lid=10&zid=0&pd=%23AC%23B1%23C1%23D14%23E33577329%23F2%23R1%23&cid=42&ctid=42"
    soup = get_soup(headers, url);
    re_list = re.findall(r"PD=(.+?);FF=;",str(soup))
    match_ids = []
    for i in re_list:
        match_id = re.findall(r"#D8#(.+?)#F3", i)
        if(len(match_id) > 0):
            match_ids.append(match_id[0])
    print(set(match_ids))


#获取每场比赛的赔率数据
def get_match_odds_soup():
    v1 = "E67036630"
    v2 = "R1"

    url = "https://www.bet365.com/SportsBook.API/web?lid=10&zid=0&pd=%23AC%23B1%23C1%23D8%23"+v1+"%23F3%23"+v2+"%23P%5E14%23Q%5E938%23&cid=42&ctid=42"
    soup = get_soup(headers,url);
    print(soup)

if __name__ == '__main__':
    #get_match_odds_soup();
    get_match_list()