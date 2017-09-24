from data.spider_tool.common_tool import *


#获取比赛id和对阵队名
def his_match_data():
    # 第一轮32周  本赛季第一场ID 1190174
    week = "32"

    url = 'https://www.whoscored.com/tournamentsfeed/15151/Fixtures/?d=2017W' + week + '&isAggregate=false'
    soup = get_soup(url);
    return soup

#详细数据
#https://www.whoscored.com/Matches/1190174/Show/England-Premier-League-2017-2018-Arsenal-Leicester
#需要比赛id和对阵队名 从 his_match_data()获取
def his_detail_data(match_id,main_team,cus_team):

    url = 'https://www.whoscored.com/Matches/'+match_id+'/Show/England-Premier-League-2017-2018-'+main_team+'-'+cus_team


if __name__ == '__main__':
    his_data = his_match_data();
    print(his_data)
    # for i in his_data:
    #     print(i)