from data.spider_tool.common_tool import *



def next_match_data():
    # 第一轮32周  本赛季第一场ID 1190174 1
    week = "32"

    url = 'https://www.whoscored.com/tournamentsfeed/15151/Fixtures/?d=2017W' + week + '&isAggregate=false'
    soup = get_soup(url);
    print(soup)

if __name__ == '__main__':
    next_match_data();