from selenium import webdriver
import json
#from common_tool.mysql_tool.mysql_tool import *
import snowflake.client

#snowflake_start_server --port=30001
snowflake.client.setup("localhost", 30001)
print(snowflake.client.get_guid())



# browser = webdriver.Chrome()
# browser.get('https://soccer.hupu.com/schedule/England.html')
# html = browser.page_source
# browser.close()
# print(html)

file = open("match.json")
jsonstr = json.load(file)


print(jsonstr[0])
#print(get_team_info_by_name(jsonstr[0]['home']))

sql = "insert into user(id,username,password) values(4,'liu','1234')"

#for i in jsonstr:
    #print(i["socre"].strip().replace("\n", "").replace("\r", "").replace("\t", ""))
    #print(i)