import pymysql

db = pymysql.connect(
    host='stuq.ceshiren.com',
    user='hogwarts_python',
    password='hogwarts_python',
    db='hogwarts_python',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)


def test_conn():
    with db.cursor() as cursor:
        sql = "show tables;"  # 查询数据库中的表名称
        cursor.execute(sql)
        print(sql)
        print(cursor.fetchall())


def test_select():
    with db.cursor() as c:
        sql = "select * from xsb where username=%s"
        c.execute(sql, ["demo"])
        print(c.fetchall())
