#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : proxy.py
# @Author: sansi
# @Date  : 2017/9/13

import urllib.request
from bs4 import BeautifulSoup
import random


def getIpList(headers):
    url = 'http://www.xicidaili.com/nn/'
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    ips = soup.find_all("tr")
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all("td")
        ip_list.append(tds[1].text + ":" + tds[2].text)
    return ip_list;


def getRandomIp(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    }

    ip_list_port = getIpList(headers)
    random_ip = getRandomIp(ip_list_port)
    print(random_ip)