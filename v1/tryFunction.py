"""
Name : tryFunction.py
Author  : 王泓林
Contect : wanghonglin@cstc.org.cn
Time    : 2022/3/14  12:53
Desc:这个文件作用是读取键盘上的输入，将输入结果存入数据库中，存储后展示本次存储的台账记录并提示成功
"""

import sqlite3
import sqlite3_connect

cursor,db = sqlite3_connect.connect();  #建立与数据库的连接

def getNum(table_name):
    resNum = -1
    try:
        resNum= cursor.execute("select count(*) from {}".format(table_name)).fetchone()[0]
        return resNum
    except Exception as e:
        print("查询表{}数据记录条数失败:".format(table_name), e)

def search_func1(table_name,xuhao_num):
    #需要改进的地方，能不能直接在语句内直接调用table_name变量，而不是if，else语句判断
    global line1_input, line2_input, line3_input, line4_input, line5_input, line6_input;  # 声明为全局变量，方便调用
    try:
        result_func1 = cursor.execute("select * from {} where 序号 = ?".format(table_name),[xuhao_num]).fetchone()
    except Exception as e:
        print("按序号查询表{}内容失败:".format(table_name),e)
        result_func1 = -1
    else:
        print("按序号查询表{}内容成功:".format(table_name),result_func1)
    return result_func1

'''按照文档编号查询记录，返回文档编号对应结果'''
def search_func2(table_name,wendang_num):
    try:
        if table_name == "input1":  #表input1返回文档编号对应全部数据记录
            result_func2 = cursor.execute("select * from input1 where 文档编号 = ?",[wendang_num]).fetchall()
        if table_name == "storage2":    #表storage2返回文档编号对应单条数据记录
            result_func2 = cursor.execute("select * from input1 where 文档编号 = ?",[wendang_num]).fetchone()
    except Exception as e:
        print("按文档编号查询表{}内容失败:".format(table_name), e)
        result_func2 = -1
    else:
        print("按文档编号查询表{}内容成功:".format(table_name), result_func2)
    return result_func2

output = search_func2("storage2",222)
print(output)

