"""
Name : realFunction.py
Author  : 王泓林
Contect : wanghonglin@cstc.org.cn
Time    : 2022/8/5  9:42
Desc:
"""
import sqlite3
import sqlite3_connect
import input_test1 #连接输入界面py文件
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial  #获取qt输入需要的组件

cursor,db = sqlite3_connect.connect();  #建立与数据库的连接
'''查询表格数据记录数量，返回记录条数'''
def getNum(table_name):
    resNum = -1
    try:
        resNum= cursor.execute("select count(*) from {}".format(table_name)).fetchone()[0]
        return resNum
    except Exception as e:
        print("查询表{}数据记录条数失败:".format(table_name), e)

'''按序号查询记录，返回序号对应数据记录'''
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

'''表storage2记录更新,按文档编号唯一找到'''
def update_storage2(wendang_num,jilu1,jilu2,jilu3,jilu4):
    '''在输入的时候补充判断语句，不能存在空语句'''
    try:
        result_upSt2 = cursor.execute("select 目的2,目的3,目的4,目的5,目的6,目的7,目的8 from storage2 where 文档编号 = ?"\
                       ,[wendang_num]).fetchone()
        print(result_upSt2)
        j = 2   #确定数据记录中的第一套空字段
        for i in result_upSt2:
            if i is None:
                break;
            else: j = j+1
        cursor.execute('update storage2 set 操作日期{}=?,操作人{}=?,操作方式{}=?,目的{}=? where 文档编号 '
                       '= ?'.format(j,j,j,j), [jilu1, jilu2, jilu3, jilu4, wendang_num])
        db.commit()
    except Exception as e:
        print("表storgage2更新数据记录更新失败:",e)

'''单条插入数据表格input1'''
def storage_to_input1():  #函数:将输入界面的输入存入到表格input1中
    global line1_input, line2_input, line3_input, line4_input, line5_input, line6_input;  # 声明为全局变量，方便调用
    '''首先查询表格内存在的序号，方便给序号（主键）赋值'''
    num_input1 = getNum("input1")+1
    try:
        insert_sqli = "insert into input1 values (?,?,?,?,?,?,?)"
        cursor.execute(insert_sqli,[num_input1, line1_input, line2_input, line3_input, line4_input, line5_input, line6_input])
    except Exception as e:
        print("函数'storage_to_input1' to 插入数据失败:", e)
        ui.textBrowser.append("输入数据失败:{}".format(e));    #需要改进，怎么把错误e给放进去
    else:
        db.commit()
        ui.textBrowser.append("插入数据成功，本次输入输入数据如下:");    #文本框内确认输入成功
        input_confirm();

'''从input1数据库中将本次输入调出打印在输入确认界面，方便确认输入是否错误'''
def input_confirm():
    num_input1 = getNum("input1")
    try:
        result = search_func1("input1",num_input1)
        print("本次输入的内容:",result)
    except Exception as e:
        print("函数'input_confirm'插入数据失败:", e)
        #ui.textBrowser.setText("数据失败:");    #需要改进，怎么把错误e给放进去
    else:
        db.commit()
        ui.textBrowser.append(str(result));    #文本框内确认输入成功,需要确认后续能够在文本框内追加写入
        #ui.textBrowser.setMaximumSize(100)    #用于限制文本最大的显示行数限制，待学习
        input_to_storage2()