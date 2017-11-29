import pymysql

db = pymysql.connect(host="120.77.249.235", user="root",
                         password="chen3531", db="tangeqiu", port=3306)
def get_db_cur():
    cur = db.cursor()
    return cur