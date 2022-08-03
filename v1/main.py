"""
Name : 数据库建表.py
Author  : 王泓林
Contect : wanghonglin@cstc.org.cn
Time    : 2022/3/14  13:03
Desc:这是主程序界面，尽量不在这里写ui函数。调用其他文件和库，展示图形化界面
PS:我最讨厌的就是别人不写注释 还有 自己要写注释
"""
import sqlite3
import sys
import sqlite3_connect
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial  #获取qt输入需要的组件
import input_test1 #连接输入界面py文件
#import 数据库建表


cursor,db = sqlite3_connect.connect();  #建立与数据库的连接

'''读取输入界面输入信息'''
def get_input1(ui):
    global line1_input, line2_input, line3_input, line4_input, line5_input, line6_input;  #声明为全局变量，方便调用
    if(ui.lineEdit_1.text()):
        line1_input = ui.lineEdit_1.text()  # 获取项目编号行的输入
        line2_input = ui.lineEdit_2.text()  # 获取文档编号行的输入
        line3_input = ui.lineEdit_3.text()  # 获取日期行的输入
        line4_input = ui.lineEdit_4.text()  # 获取操作人行的输入
        line5_input = ui.lineEdit_5.text()  # 获取操作方式行的输入
        line6_input = ui.lineEdit_6.text()  # 获取目的行的输入
        storage_to_input1();
    #print(line1_input,line2_input,line3_input,line4_input,line5_input,line6_input)

'''按序号查询记录，返回多个查询结果'''
def search_func1(table_name,xuhao_num):
    #需要改进的地方，能不能直接在语句内直接调用table_name变量，而不是if，else语句判断
    global line1_input, line2_input, line3_input, line4_input, line5_input, line6_input;  # 声明为全局变量，方便调用
    if (table_name == 'storage2'):    #查询storage2库
        sqli_func1 = "select * from storage2 where 序号 = %s;"
        try:
            cursor.execute(sqli_func1, xuhao_num);
            result_func1 = cursor.fetchone()
            print(result_func1)
        except Exception as e:
            print("按序号查询表storage2失败:", e)
        else:
            print("按查询storage2成功")
            return result_func1
    if (table_name == 'input1'):    #查询input1库
        sqli_func1 = "select * from input1 where 序号 = %s;"
        try:
            cursor.execute(sqli_func1, xuhao_num);
            result_func1 = cursor.fetchone()
            print(result_func1)
        except Exception as e:
            print("按序号查询表input1失败:", e)
        else:
            print("按查询表input1成功")
            return result_func1
    if (table_name == 'storage1'):    #查询storage1库
        sqli_func1 = "select * from storage1 where 序号 = %s;"
        try:
            cursor.execute(sqli_func1, xuhao_num);
            result_func1 = cursor.fetchone()
            print(result_func1)
        except Exception as e:
            print("按序号查询storage1失败:", e)
        else:
            print("按查询storage1成功")
            return result_func1
    if (table_name == 'storage3'):    #查询storage3库
        sqli_func1 = "select * from storage3 where 序号 = %s;"
        try:
            cursor.execute(sqli_func1, xuhao_num);
            result_func1 = cursor.fetchone()
            print(result_func1)
        except Exception as e:
            print("按序号查询storage3失败:", e)
        else:
            print("按查询storage3成功")
            return result_func1

'''表storage2记录更新,按文档编号唯一找到'''
def update_storage2(wendang_num,jilu1,jilu2,jilu3,jilu4):
    sqli = 'select * from storage2 where 文档编号 = %s'
    cursor.execute(sqli,wendang_num)
    result_temp1 = cursor.fetchone()
    print(result_temp1)
    print(wendang_num)
    if (result_temp1 != None):
        '''找到第一组空的记录位置'''
        cursor.execute('select 目的2,目的3,目的4,目的5,目的6,目的7,目的8 from storage2 where 文档编号 = %s',wendang_num)
        result_temp1 = cursor.fetchone()
        if(result_temp1[0] == None):
            cursor.execute('update storage2 set 操作日期2=%s,操作人2=%s,操作方式2=%s,目的2=%s where 文档编号 '
                           '= %s',[jilu1,jilu2,jilu3,jilu4,wendang_num])
        elif(result_temp1[0] == None):
            cursor.execute('update storage2 set 操作日期3=%s,操作人3=%s,操作方式3=%s,目的3=%s where 文档编号 '
                           '= %s',[jilu1,jilu2,jilu3,jilu4,wendang_num])
        elif (result_temp1[0] == None):
                cursor.execute('update storage2 set 操作日期4=%s,操作人4=%s,操作方式4=%s,目的4=%s where 文档编号 '
                               '= %s', [jilu1, jilu2, jilu3, jilu4, wendang_num])
        elif (result_temp1[0] == None):
                cursor.execute('update storage2 set 操作日期5=%s,操作人5=%s,操作方式5=%s,目的5=%s where 文档编号 '
                               '= %s', [jilu1, jilu2, jilu3, jilu4,wendang_num])
        elif(result_temp1[0] == None):
            cursor.execute('update storage2 set 操作日期6=%s,操作人6=%s,操作方式6=%s,目的6=%s where 文档编号 '
                           '= %s',[jilu1,jilu2,jilu3,jilu4,wendang_num])
        elif (result_temp1[0] == None):
                cursor.execute('update storage2 set 操作日期7=%s,操作人7=%s,操作方式7=%s,目的7=%s where 文档编号 '
                               '= %s', [jilu1, jilu2, jilu3, jilu4, wendang_num])
        elif (result_temp1[0] == None):
                cursor.execute('update storage2 set 操作日期8=%s,操作人8=%s,操作方式8=%s,目的8=%s where 文档编号 '
                               '= %s', [jilu1, jilu2, jilu3, jilu4,wendang_num])
    db.commit()
    #增加错误提示

'''按照文档编号导出输出文件'''
def output_wendang():
    #如果形参得到是all，则全部输出，如果是wrong，则导出没有销毁的记录
    #sqlt_out1 = "select * from storage2;"
    try:
        sqlt_out1 = "select * into outfile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/output2.xls' from storage2 ;"
        #sqlt_out1 = "mysqldump -uroot -p123456 -defalut-character-set=utf8 test1 storage2 >C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/output1.xls;"
        cursor.execute(sqlt_out1)  # 默认不返回查询结果集， 返回数据记录数。
    #sqlt_out2 = "select * from storage2 where 序号 = %s;"
    #输出中文乱码，表头暂时没能打印，找
    except Exception as e:
        print("输出文件失败:", e)
        # ui.textBrowser.append("输入数据失败:");  # 需要改进，怎么把错误e给放进去
    else:print("输出成功")

'''单条插入数据表格input1'''
def storage_to_input1():  #函数:将输入界面的输入存入到表格input1中
    global line1_input, line2_input, line3_input, line4_input, line5_input, line6_input;  # 声明为全局变量，方便调用
    '''首先查询表格内存在的序号，方便给序号（主键）赋值'''
    sqli = "select * from input1;"
    num_input1 = 0 ;
    num_input1 = cursor.execute(sqli)  # 默认不返回查询结果集， 返回数据记录数。
    '''向数据库内赋值，包括读取的行与自动赋值的序号'''
    num_input1 = num_input1 + 1;   #序号是主键，不可重复，不可改动
    try:
        insert_sqli = "insert into input1 values (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(insert_sqli,[num_input1, line1_input, line2_input, line3_input, line4_input, line5_input, line6_input])
    except Exception as e:
        #print("插入数据失败:", e)
        ui.textBrowser.append("输入数据失败:");    #需要改进，怎么把错误e给放进去
    else:
        # 如果是插入数据， 一定要提交数据， 不然数据库中找不到要插入的数据;
        db.commit()
        #print("插入数据成功;")
        ui.textBrowser.append("插入数据成功，本次输入输入数据如下:");    #文本框内确认输入成功
        input_confirm();

'''从input1数据库中将本次输入调出打印在输入确认界面，方便确认输入是否错误'''
def input_confirm():
    sqli2 = "select * from input1;"
    num_input1 = 0;
    num_input1 = cursor.execute(sqli2)  # 默认不返回查询结果集， 返回数据记录数。
    try:
        search_sqli = "select * from input1 where 序号 = %s"
        cursor.execute(search_sqli, num_input1);
        result = cursor.fetchone();
    except Exception as e:
        print("插入数据失败:", e)
        #ui.textBrowser.setText("数据失败:");    #需要改进，怎么把错误e给放进去
    else:
        # 如果是插入数据， 一定要提交数据， 不然数据库中找不到要插入的数据;
        db.commit()
        #print("插入数据成功;")
        #print(result)
        ui.textBrowser.append(str(result));    #文本框内确认输入成功,需要确认后续能够在文本框内追加写入
        #ui.textBrowser.setMaximumSize(100)    #用于限制文本最大的显示行数限制，待学习
        input_to_storage2()

'''按照文档编号查询按钮'''
'''按照操作人查询'''
'''按照项目编号查询'''
'''普通查询'''
'''记录删除'''

'''将input1中得到的输入数据，存储到其他的三个表中，方便输入,应该是从数据库表格中读取，注意是否可以使用联结'''
'''好像可以用联结，先取消storage1以及按照项目编号查询的功能，先把这个按文档编号查询的和输出的功能弄好'''
def input_to_storage2():
    #这个应该由查询，插入以及更新功能模组组成，先获得input1中新输入的数据记录，判断是否已经有文档记录，没有的话新增记录，有的话则更新新的记录
    '''下面抓取本次输入的文档编号'''
    sqli3 = "select * from input1;"
    search_sqli_1 = "select 文档编号 from input1 where 序号 = %s"
    num_input1 = 0;  #统计input1中的记录行数
    num_input1 = cursor.execute(sqli3)  # 默认不返回查询结果集， 返回数据记录数。
    cursor.execute(search_sqli_1, num_input1);
    result_1 = str(cursor.fetchone()[0])
    #print(result_1)
    '''判断storage2是否已经有这个文档编号的记录'''
    global line1_input, line2_input, line3_input, line4_input, line5_input, line6_input;  # 声明为全局变量，方便调用
    search_sqli_2 = "select * from storage2 where 文档编号 = %s"
    cursor.execute(search_sqli_2,line2_input)
    result_2 = str(cursor.fetchone())
    #print(result_2)
    if(result_2 != 'None'):    #已有记录
        ui.textBrowser.append("该文档已有记录如下:"+result_2);
        update_storage2(result_1,line3_input,line4_input,line5_input,line6_input)
        #本处添加更新功能的内容
        ui.textBrowser.append("本次输入后该文档记录更新为:")
    else:    #无记录
        sqli4 = "select * from storage2;"
        num_input2 = 0;
        num_input2 = cursor.execute(sqli4)  # 默认不返回查询结果集， 返回数据记录数。
        '''向数据库内赋值，包括读取的行与自动赋值的序号'''
        num_input2 = num_input2 + 1;  # 以上几行是为了确定序号，序号是主键，不可重复，不可改动
        try:
            insert_sqli2 = "insert into storage2 (序号,文档编号,项目编号,操作日期1,操作人1,操作方式1,目的1) values(%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(insert_sqli2,[num_input2, line2_input, line1_input, line3_input, line4_input, line5_input, line6_input])
        except Exception as e:
            print("存储到表storage2失败:", e)
            #ui.textBrowser.append("输入数据失败:");  # 需要改进，怎么把错误e给放进去
        else:
            # 如果是插入数据， 一定要提交数据， 不然数据库中找不到要插入的数据;
            db.commit()
            # print("插入数据成功;")
            result_3 = search_func1('storage2',num_input2)
            '''单行数据去除空，看看能不能转为函数，最终目标是把能放到类里面，然后引用就行'''
            result_3_output = [];
            for x in result_3:
                if(x != None):result_3_output.append(x);
            result_3_output = str(result_3_output);
            #print(str(result_3_output))
            ui.textBrowser.append("存储到表storage2成功，这是该台账的第一次记录,存储如下:"+result_3_output);  # 文本框内确认输入成功



'''清除输入按钮'''

'''清除文本框按钮'''

'''运行输入界面文件，看看这个能否作为主程序进行运行'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = input_test1.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    global line1_input, line2_input, line3_input, line4_input, line5_input, line6_input;    #声明并初始化全局变量，方便调用
    line1_input, line2_input, line3_input, line4_input, line5_input, line6_input = ['0', '0', '0', '0', '0', '0'];
    ui.pushButton_input.clicked.connect(partial(get_input1, ui));    #获取输入字符串
    ui.pushButton_output1.clicked.connect(output_wendang)
    app.exec_()  #如果改成sys.exit(app.exec_())则关闭窗口，程序退出
    cursor.close();
    db.close();




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
