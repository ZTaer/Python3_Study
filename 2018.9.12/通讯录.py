#/usr/bin/python3
#-*-coding:utf-8-*-
import sys

#   #   问题写一个通讯录
#   有姓名与电话
#   有5个功能，查询，插入，插入检测，删除，退出
#   显示功能界面,等待指令
#   查询界面，索引输入的键值
#           有则显示内容 , 无则提示“查无此人”
#   插入界面
#           输入姓名,检测是否已经存在此人
#           是,则提示已经存在,是否修改内容
#           否,则新建内容
#   删除界面
#   输入删除的键值
#   提示确定删除
#           是,则删除,并提示删除成功
#           否,则不删除,并提示已取消删除
#   退出界面
#       提示“感谢使用”结束程序
#   #   在v2.0加入返回界面功能

def telet_index(x = 0): # 主界面
    print("|--- 欢迎使用通讯录 ---|")
    print(" |--- 1 : 查询联系人 ---|")
    print(" |--- 2 : 新建联系人 ---|")
    print(" |--- 3 : 删除联系人 ---|")
    print(" |--- 4 : 退出本程序 ---|")
    print(" |---    +++新增+++   ---|")
    print(" |--- 5 : 已有联系人 ---|")
    print(" |---      版本v2.0     ---|")
    x = str(x)
    if x == '0':
        x = input("输入指令: ")
    if x == '1':
        telet_find()
    elif x == '2':
        telet_join()
    elif x == '3':
        telet_delet()
    elif x == '4':
        print("|--- 感谢使用本程序! ---|")
        try:
            sys.exit(0)
        except:
            print("")
    elif x == '5':
        main_print()
        telet_index(1)
        
def telet_find(): # 查询联系人界面
    name = input("请输入查找姓名: ")
    if name in maindict:
        print('%s: %s' % (name , maindict[name]) )
        telet_index()
    else:
        print("查无此人!")
        yes_no = input("是否添加'Yes / No': ")
        if yes_no.lower() == 'yes':
            telet_join()
        else:
            telet_index()
            
            
def telet_join(): # 新建联系人界面
    each = input("姓名: ")
    if each in maindict:
        print('此联系人已经存在')
        yes_no = input("是否修改'Yes / No': ")
        if yes_no.lower() == 'yes':
            iphone = input("电话: ")
            main_join(each , iphone)
            telet_index()
        else:
            telet_index()
    else:
        iphone = input("电话: ")
        main_join(each , iphone)
        telet_index()

def telet_delet(): # 删除联系人界面
    name = input("删除无法恢复,请谨慎! \n姓名: ")
    if name in maindict:
        yes_no = input("确定删除'Yes / No': ")
        if yes_no.lower() == 'yes':
            main_delet(name)
            telet_index()
        else:
            telet_index()
    else:
        print("查无此人!")
        telet_index()

def main_join(name , iphone):
    maindict[name] = iphone
    print("%s: %s ( 成功! )" % (name , iphone))

def main_delet(name):
    maindict.pop(name)
    print("删除成功!")

def main_print():
    for i in maindict:
        print("%s: %s" % (i , maindict[i]))
    
    
if __name__ == "__main__":
    maindict = {'赵特':'123213','赵腾':'123213','赵飞':'123213'}
    telet_index()
