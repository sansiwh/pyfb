from common_tool.mysql_tool.mysql_tool import *

#按照轮数计算排行榜
#同分比较净胜球 再比进球数
def calculate_rank_by_turn(turn):
    if turn == 1:
        rank_list = []
        sql = "select main_team_gid,custom_team_gid,match_time from match_info where turn = " + str(turn)
        results = query(sql)
        for i in results:
            #数据存入元素后放入集合进行排序
            home_gid = i[0]
            away_gid = i[1]
            score = i[2]
            home_goal = score.split(":")[0]
            away_goal = score.split(":")[1]
            #rank_num,team_gid,win_num,tie_num,lose_num,win_goal,lose_goal,point,turn
            #home
            if score.split(":")[0] > score.split(":")[1]:
                rank_home = (home_gid,1,0,0,int(home_goal),int(away_goal),3,1)
                rank_away = (away_gid,0,0,1,int(away_goal),int(home_goal),0,1)
                rank_list.append(rank_home)
                rank_list.append(rank_away)
            elif score.split(":")[0] == score.split(":")[1]:
                rank_home = (home_gid,0,1,0,int(home_goal),int(away_goal),1,1)
                rank_away = (away_gid,0,1,0,int(away_goal),int(home_goal),1,1)
                rank_list.append(rank_home)
                rank_list.append(rank_away)
            else:
                rank_home = (home_gid,0,0,1,int(home_goal),int(away_goal),0,1)
                rank_away = (away_gid,1,0,0,int(away_goal),int(home_goal),3,1)
                rank_list.append(rank_home)
                rank_list.append(rank_away)
        for i in rank_list:
            time.sleep(0.1)
            league_gid = 375414018631794688
            gid_str = get_snowflake_gid()
            gid = (gid_str, league_gid)
            values = gid + i
            sql = "insert into league_rank_info (gid,league_gid,team_gid,win_num,tie_num,lose_num,win_goal,lose_goal,point,turn)" \
                  " values " + str(values)
            insert(sql)
    else:
        #SELECT * from league_rank_info where turn = 1 ORDER BY point desc,(win_goal-lose_goal) desc,win_goal
        sql = "select main_team_gid,custom_team_gid,match_time from match_info where turn = " + str(turn)
        results = query(sql)
        for i in results:
            time.sleep(0.1)
            league_gid = 375414018631794688
            gid_str = get_snowflake_gid()
            home_gid = i[0]
            away_gid = i[1]
            score = i[2]
            home_goal = score.split("-")[0]
            away_goal = score.split("-")[1]

            #home
            sql = "select win_num,tie_num,lose_num,win_goal,lose_goal,point from league_rank_info where turn = " + str(turn - 1) + " and team_gid = " + str(home_gid)
            rank_home_data = query(sql)
            win_num = rank_home_data[0][0]
            tie_num = rank_home_data[0][1]
            lose_num = rank_home_data[0][2]
            win_goal = rank_home_data[0][3]
            lose_goal = rank_home_data[0][4]
            point = rank_home_data[0][5]
            if home_goal > away_goal:
                win_num = win_num + 1
                point = point + 3
            elif home_goal == away_goal:
                tie_num = tie_num + 1
                point = point + 1
            else:
                lose_num = lose_num + 1
                point = point

            win_goal = win_goal + int(home_goal)
            lose_goal = lose_goal + int(away_goal)
            sql = "insert into league_rank_info (gid,league_gid,team_gid,win_num,tie_num,lose_num,win_goal,lose_goal,point,turn)" \
                  " values ("+str(gid_str)+","+str(league_gid)+","+str(home_gid)+","+str(win_num)+","+str(tie_num)+","+str(lose_num)+","+str(win_goal)+","+str(lose_goal)+","+str(point)+","+str(turn)+")"
            insert(sql)

            #away
            time.sleep(0.1)
            gid_str = get_snowflake_gid()
            sql = "select win_num,tie_num,lose_num,win_goal,lose_goal,point from league_rank_info where turn = " + str(turn - 1) + " and team_gid = " + str(away_gid)
            rank_away_data = query(sql)
            away_win_num = rank_away_data[0][0]
            away_tie_num = rank_away_data[0][1]
            away_lose_num = rank_away_data[0][2]
            away_win_goal = rank_away_data[0][3]
            away_lose_goal = rank_away_data[0][4]
            away_point = rank_away_data[0][5]
            if home_goal < away_goal:
                away_win_num = away_win_num + 1
                away_point = away_point + 3
            elif home_goal == away_goal:
                away_tie_num = away_tie_num + 1
                away_point = away_point + 1
            else:
                away_lose_num = away_lose_num + 1
                away_point = away_point

            away_win_goal = away_win_goal + int(away_goal)
            away_lose_goal = away_lose_goal + int(home_goal)
            sql = "insert into league_rank_info (gid,league_gid,team_gid,win_num,tie_num,lose_num,win_goal,lose_goal,point,turn)" \
                  " values (" + str(gid_str) + "," + str(league_gid) + "," + str(away_gid) + "," + str(
                away_win_num) + "," + str(away_tie_num) + "," + str(away_lose_num) + "," + str(away_win_goal) + "," + str(
                away_lose_goal) + "," + str(away_point) + "," + str(turn) + ")"
            insert(sql)


#抓取最新排名

if __name__ == '__main__':
    calculate_rank_by_turn(15)