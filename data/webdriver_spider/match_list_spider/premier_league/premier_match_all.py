from selenium import webdriver
import json
from common_tool.mysql_tool.mysql_tool import *
import snowflake.client

#snowflake_start_server --port=30001
#snowflake.client.setup("localhost", 30001)
#print(snowflake.client.get_guid())



# browser = webdriver.Chrome()
# browser.get('https://soccer.hupu.com/schedule/England.html')
# html = browser.page_source
# browser.close()
# print(html)
snowflake.client.setup("localhost", 30001)
def insert_match_info():
    file = open("match.json")
    jsonstr = json.load(file)

    for i in range(len(jsonstr)):
        gid = snowflake.client.get_guid()
        main_team_gid = get_team_info_by_name(jsonstr[i]["home"])
        custom_team_gid = get_team_info_by_name(jsonstr[i]["away"])
        league_gid = "375414018631794688" #暂时写死
        match_type = "375414018631794688" #暂时写死
        match_date = jsonstr[i]["time"]
        match_week = jsonstr[i]["day"]
        match_time = jsonstr[i]["socre"].strip().replace("\n", "").replace("\r", "").replace("\t", "")
        turn = jsonstr[i]["turn"]

        sql = "insert into match_info(gid,main_team_gid,custom_team_gid,league_gid,match_date,match_week,match_time,match_type,turn)" \
              " values("+str(gid)+","+str(main_team_gid)+","+str(custom_team_gid)+","+league_gid+",'"+match_date+"','"+match_week+"','"+match_time+"',"+match_type+","+str(turn)+")"
        insert(sql)
    close_db()

if __name__ == '__main__':
    insert_match_info()