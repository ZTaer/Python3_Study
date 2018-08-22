#!/usr/bin/python3
#-*- coding:utf-8 -*-

# 原始sum()v1.0
def sum1(list):
    he = 0
    for i in list:
        he = he + i
    return he


# 升级版sum()无视字符串类型v1.0
def sum2(list):
    he = 0
    for i in list:
        if not isinstance(i,str):
            he = he + i
    return he


if __name__ == "__main__":
    list = ['a',5,5,5]
    # print (sum1(list))
    print (sum2(list))
