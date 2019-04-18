#!/usr/bin/python3
#-*- coding:utf-8 -*-
import random # 引入随机函数库

if __name__ == "__main__":
    str1 = input("请输入开始: ") # 输入字符串
    if str1 == "开始": # 如果输入的字符串为“开始”,则进行执行
        for num in range(3): # 循环3次
            num = random.randint(1,1000) # 生成随机数
            print( "%s " % num ,end='' ) # 在同一行显示随机数字
