import pymysql
from common_tool.mysql_tool.data_source import *
import snowflake.client

name_gid = {}
cur = get_db_cur()
sql = "select * from team_info"
print("查询")
try:
    cur.execute(sql)
    results = cur.fetchall()
    for row in results:
        name_gid[row[1]]=row[0]
except Exception as e:
    raise e

#缓存球队信息
def get_team_info_by_name(name):
    return  name_gid[name]

def insert(sql):
    try:
        cur.execute(sql)
        db.commit()
    except Exception as e:
        db.rollback()
        raise e

def close_db():
    db.close()

if __name__ == '__main__':
    print(get_team_info_by_name("莱斯特城"))
    snowflake.client.setup("localhost", 30001)
    gid = snowflake.client.get_guid()

    #sql = "insert into match_info(gid,main_team_gid,custom_team_gid,league_team_gid,match_date,match_week,match_time,turn) values(4030163061145862145,375434198808264704,375434474885742592,375414018631794688,2017-08-12,星期六,4:3,1)"
    sql = "insert into match_info(gid,main_team_gid,custom_team_gid,league_gid,match_date,match_week,match_time,turn) values(4030173254533513217,375434198808264704,375434474885742592,375414018631794688,'2017-08-12','星期六','4:3',1)"
    insert(sql)