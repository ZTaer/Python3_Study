#!/usr/bin/python3
#-*- coding:utf-8 -*-
import random

temp = input("猜一个数字(0-10): ")
guess = int(temp)
x = random.randint(0,10)
if guess == x:
    print("恭喜你,猜中啦！！")
else:
    print("很遗憾,你猜错啦!")
    print("正确答案是: "+str(x))