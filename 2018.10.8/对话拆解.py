#!/usr/bin/python3
#-*- coding:utf-8 -*-
import os
import pickle

#   #   文件自动创建处理
#   默认创建"boy_%s.txt"/"gir_%s.txt" % n = 1
#   #   语句问题处理
#   我打算用for循环迭代出每一行
#   单个处理每一个迭代对象
#   如果被迭代对象不等于“=”( 用rfind()解决 )
#       直接使用split(':')分割对话
#           如果分割后列表长度为2
#               如果列表[0] == "小甲鱼",那么将列表[1]存入boy_%s.txt % n
#               如果列表[0] == "小客服",那么将列表[1]存入gir_%s.txt % n
#           如果列表单位为1那么直接加入gir/boy_%s.txt % n
#   如果有"="那么
#       n+=1并且创建文件"boy_%s.txt"/"gir_%s.txt" n
#   #   核心split()函数以及rfind()函数
#   #   对话分解 , 版本2.0使用pickle模块进行存储

def chatCategory( chatfile ):
    n = 1
    boy = open('boy_%s.txt' % n,'wb+')
    gir = open('gir_%s.txt' % n, 'wb+')
    chatfile.seek(0, 0) # 设置指针为开头,保证迭代完整性
    for chatline in chatfile:
        if chatline.rfind('=') < 0: # 没有分割线进行迭代语句处理
            list = chatline.split(':') # 使用split(":")来分割被迭代出的字符串
            if len(list) == 2: # 真正的对话处理
                if list[0] == '小甲鱼':
                    pickle.dump( list[1] , boy )
                elif list[0] == '小客服':
                    pickle.dump( list[1] , gir )
            elif len(list) == 1: # 空格,什么的一起写入
                pickle.dump( list[0] , boy )
                pickle.dump( list[0] , gir )
        else: # 如果有分割线创建新的文件
            boy.close()
            gir.close()
            n+=1
            boy = open('boy_%s.txt' % n, 'wb+')
            gir = open('gir_%s.txt' % n, 'wb+')
    boy.close()
    gir.close()

if __name__ == "__main__":
    chat_file = open('record.txt','at+')
    chatCategory(chat_file)
    chat_file.close()
