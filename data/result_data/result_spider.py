import urllib.request
from data.spider_tool.proxy import *
from bs4 import BeautifulSoup
from data.spider_tool.mongo_db import *

#插入每轮比赛结果
#比赛轮数
turn_num = "7"

def get_soup():
    headers = {
        "Connection": "close",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        "Cookie": "u=721493343230860; s=fq124vw7g9; webp=0; aliyungf_tc=AQAAAAGV+zc0dQQAGq85cQVvSoYsqrE4; xq_a_token=afe4be3cb5bef00f249343e7c6ad8ac7dc0e17fb; xq_a_token.sig=6QeqeLxu5hi1S21JgtozJ1EZcsQ; xq_r_token=a1e0ac0c42513dcf339ddf01778b49054e341172; xq_r_token.sig=VPMAft0BfpDHm5UE0QJ5oDLYunw; __utmt=1; __utma=1.1379458042.1493343321.1493778350.1493783528.5; __utmb=1.3.10.1493783528; __utmc=1; __utmz=1.1493343321.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1493369217,1493688491,1493778343,1493779071; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1493784158"
    }
    url = 'http://www.ssports.com/data/rankMatch_' + turn_num + '.html'
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    return soup

#返回集合直接插入mongodb
def get_result_list():
    tr_data = get_soup().find_all("tr")
    #本轮结果集合
    turn_result = []
    for index in range(len(tr_data)):
        #比赛结果
        match_result = {}
        tr_html = BeautifulSoup(str(tr_data[index]), "html.parser")
        td_data = tr_html.find_all("td")
        match_date = td_data[1].get_text()
        match_result["match_date"]=match_date

        match_main = td_data[2].get_text()
        match_result["match_main"] = match_main

        score = td_data[3].get_text()
        score_arr = score.strip().split(":")
        match_main_score = score_arr[0].strip()
        match_cust_score = score_arr[1].strip()
        match_result["match_main_score"] = int(match_main_score)
        match_result["match_cust_score"] = int(match_cust_score)

        match_cust = td_data[4].get_text()
        match_result["match_cust"] = match_cust

        match_result["turn_num"] = turn_num

        turn_result.append(match_result)
    return turn_result

def insert_mongodb(list):
    #用集合批量插入MONGODB，结果为单条插入
    get_mondb().match_result.insert_many(list)


if __name__ == '__main__':
    turn_result = get_result_list()

    print(turn_result)
    #get_mondb().match_result.remove()


    insert_mongodb(turn_result)
    # for i in get_mondb().match_result.find():#{"turn_num": turn_num}
    #     print(i)

    # res_list = get_mondb().match_result.find({"$or": [{"match_main": "阿森纳"}, {"match_cust": "阿森纳"}]})
    # for i in res_list:
    #     print(i)