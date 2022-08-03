"""
Name : 数据库建表.py
Author  : 王泓林
Contect : wanghonglin@cstc.org.cn
Time    : 2022/3/14  13:03
Desc:运行main前，运行此文件建立数据库表格
"""
import sqlite3
import sqlite3_connect


cursor,db = sqlite3_connect.connect();  #建立与数据库的连接

# 建表的sql语句
sql_text_1 = '''CREATE TABLE input1
           (序号 INT,
            项目编号 VARCHAR(45),
            文档编号 VARCHAR(45),
            操作日期 DATETIME,
            操作方式 VARCHAR(45),
            目的 VARCHAR(45));'''
# 执行sql语句
#cursor.execute(sql_text_1)

sql_text_2 = '''CREATE TABLE storage2
           (序号 INT,
            文档编号 VARCHAR(45),
            项目编号 VARCHAR(45),
            操作日期1 DATETIME,
            操作人1 VARCHAR(45),
            操作方式1 VARCHAR(45),
            目的1 VARCHAR(45),
            操作日期2 DATETIME,
            操作人2 VARCHAR(45),
            操作方式2 VARCHAR(45),
            目的2 VARCHAR(45),          
            操作日期3 DATETIME,
            操作人3 VARCHAR(45),
            操作方式3 VARCHAR(45),
            目的3 VARCHAR(45),
            操作日期4 DATETIME,
            操作人4 VARCHAR(45),
            操作方式4 VARCHAR(45),
            目的4 VARCHAR(45),
            操作日期5 DATETIME,
            操作人5 VARCHAR(45),
            操作方式5 VARCHAR(45),
            目的5 VARCHAR(45),
            操作日期6 DATETIME,
            操作人6 VARCHAR(45),
            操作方式6 VARCHAR(45),
            目的6 VARCHAR(45),
            操作日期7 DATETIME,
            操作人7 VARCHAR(45),
            操作方式7 VARCHAR(45),
            目的7 VARCHAR(45),
            操作日期8 DATETIME,
            操作人8 VARCHAR(45),
            操作方式8 VARCHAR(45),
            目的8 VARCHAR(45)
            );'''

#cursor.execute(sql_text_2)
sql = "select * from input1"
num_input1 = cursor.execute(sql)
num_input1 += 1
print(num_input1)
#r = cursor.execute("select 序号 from storage1")  # 执行SQL语句，获取记录
#data = cursor.fetchall()  # 获取数据
#print(data)  # 输出数据
#cursor.close()  # 关闭游标
#db.close()  # 关闭数据库连接
