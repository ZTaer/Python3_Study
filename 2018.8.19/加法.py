#!/usr/bin/python3
#-*- coding:utf-8 -*-

def inputnum():
    return float(input("输入:"))

def jiafa_(x,y): # 加法计算
    return x+y

if __name__ == "__main__":
    x = inputnum()
    y = inputnum()
    print ("加法计算结果: "+ str(jiafa_(x,y)))


