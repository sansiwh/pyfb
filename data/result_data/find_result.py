#从数据库查询数据
from data.spider_tool.mongo_db import *

#获取两队本赛季战绩
def find_result_by_name(name1,name2):
    res_list = get_mondb().match_result.find({"$or": [{"match_main": name1}, {"match_cust": name1}]})
    res_list2 = get_mondb().match_result.find({"$or": [{"match_main": name2}, {"match_cust": name2}]})
    for i in res_list:
        #mongodb获取的是字典类型
        #print(i)
        print("主场:"+i['match_main']+"  "+str(i['match_main_score'])+":"+str(i['match_cust_score']) + "  客场:"+i['match_cust'])

    print("--------------------------------------------------")

    for i in res_list2:
        #mongodb获取的是字典类型
        #print(i)
        print("主场:"+i['match_main']+"  "+str(i['match_main_score'])+":"+str(i['match_cust_score']) + "  客场:"+i['match_cust'])


if __name__ == '__main__':
    find_result_by_name("热刺","伯恩茅斯")