# -*- coding: utf-8 -*-
import sqlite3

sql = 'select * from user; select * from messages;' \
      ''

def connectDB():
    con = sqlite3.connect('data-dev.sqlite')
    cur = con.cursor()

    return con, cur


def insertDB(cur,  sql):
    try:
        data = cur.executescript(sql)
        for i in data:
            print(i)
    except:
        pass




def close_cur_DB(con, cur):
    con = con
    cur = cur
    cur.close()
    con.close()


con, cur = connectDB()

insertDB(cur, sql)

close_cur_DB(con, cur)