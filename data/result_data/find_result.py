#从数据库查询数据
from data.spider_tool.mongo_db import *

def find_result_by_name(name):
    res_list = get_mondb().match_result.find({"$or": [{"match_main": name}, {"match_cust": name}]})
    for i in res_list:
        print(i)

if __name__ == '__main__':
    find_result_by_name("切尔西")
