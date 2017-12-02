import pymysql

#tangeqiutest 测试库
#tangeqiu 正式库
db = pymysql.connect(host="120.77.249.235", user="root",
                         password="chen3531", db="tangeqiu", port=3306, charset="utf8")
def get_db_cur():
    cur = db.cursor()
    return cur