import pymysql
import utilspy.textpy as tp


def connect(userid, username):
    try:
        db = pymysql.connect(host="XXX",
                             port=XXX,
                             user="XXX",
                             password="XXX",
                             database="XXX",
                             charset='utf8')
        cursor = db.cursor()
        solve(cursor, userid, username)
        cursor.close()
        db.close()

    except:
        print('数据库连接失败')


def solve(cursor, userid, username):
    sql = f'select * from todolist where userid = {userid}'
    cursor.execute(sql)
    res = cursor.fetchall()
    print(
        f'\nHave a good day {username} ! {len(res)} backlogs in your Todolist:')
    tp.separator()
    for index, todo in enumerate(res):
        print(f'({index+1}): {todo[2]}')
    tp.separator()
