"""
Name : sqlite3_connect.py
Author  : 王泓林
Contect : wanghonglin@cstc.org.cn
Time    : 2022/3/14  15:45
Desc:连接数据库文件
"""
import sqlite3
def connect():
    db = sqlite3.connect("test.db")  # 数据库名
    #db = sqlite3.connect(host="localhost",  # 连接到数据库，服务器为本机
    #                    user="root",  # 用户名
    #                     passwd="123456",  # 密码
    #                    db="test1")  # 数据库名
    cursor = db.cursor()  # 获得数据库游标
    return cursor,db

#r = cursor.execute("select 序号 from storage1")  # 执行SQL语句，获取记录
#data = cursor.fetchall()  # 获取数据
#print(data)  # 输出数据
#cursor.close()  # 关闭游标
#db.close()  # 关闭数据库连接