import pymysql
from common_tool.mysql_tool.data_source import *

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
finally:
    db.close()  #关闭连接

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
    finally:
        db.close()


if __name__ == '__main__':
    print(get_team_info_by_name("曼联"))