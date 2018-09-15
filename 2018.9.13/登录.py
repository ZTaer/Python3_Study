#/usr/bin/python3
#-*- coding:utf-8 -*-
import sys

#   #   问题登录界面
#   用户名(键值) + 密码(内容)
#   新建用户界面
#   输入用户名,并且判断是否已经存在
#           是:重新输入
#           否:输入密码
#   登录用户界面
#   输入用户名,并且检测是否已经存在
#           是:输入密码
#                   检测密码是否正确
#                       是: 登录成功
#                       否: 重新输入密码
#           否:重新输入用户名
#   退出界面
#   import sys
#   try:
#       sys.exit(0)
#   except:
#       print("")

def user_index(order = 0):
    
    #   检测核心
    check_user = lambda user : 1 if user in userdict else 0
    check_password = lambda user , password : 1 if password == userdict[user] else 0
    #   用户加入字典核心
    def main_join( user, password ):
        userdict[ user ] = password

    #   注册界面
    def user_sin():
        user = input("用户名: ")
        while check_user( user ):
            user = input("已存在请重新输入: ")
        password = input("密码: ")
        main_join( user , password )
        print("成功注册!\n赶紧去尝试登录吧:D\n")
        user_index()

    #   登录界面
    def user_login():
        user = input("用户名: ")
        while not check_user( user ):
            user = input("用户名不存在\n请重新输入: ")
        password = input("密码: ")
        i = 0
        while not check_password(user , password) and i < 3:
            password = input("密码错误请重新输入: ")
            i+=1
        if check_password( user , password ):
            print("登录成功\n欢迎进入HackerSystem2.318( 点击右上角结束程序 )")
        else:
            print( "登录失败!" )
            

    #   主界面
    print('|--- 新建用户: N / n ---|')
    print('|--- 登录账号: E / e ---|')
    print('|--- 退出程序: Q / q ---|')
    while  not order:
        order = input("请输入指令: ")
    order = str(order).lower() # 格式化命令
    if order == 'n' :
        user_sin() # 进入注册界面
    elif order == 'e':
        user_login() # 进入登录界面
    elif order == 'q': # 退出程序
        try:
            sys.exit()
        except:
            print("程序结束!\n")
        

if __name__ == "__main__":
    userdict = {'ztaer':'123456','zhao':'666666'}
    user_index()
    
