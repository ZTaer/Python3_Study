#!/usr/bin/python3
#-*- coding:utf-8 -*-

def min1(list): # # 逻辑过度
    if len(list) == 1:
        return list[0]
    else:
        bf = list[:]
        for each in bf:
            bf.remove(each)
            for i in bf:
                if each < i:
                    continue
                elif each > i:
                    each = i
            return each

def min2(list): # # 逻辑过度
    if len(list) == 1:
        return list[0]
    else:
        bf = list[:]
        each = bf.pop(0)
        for i in bf:
            if each < i:
                continue
            elif each > i:
                each = i
        return each

def min3(list): # # min()我的正解
    if len(list) == 1:
        return list[0]
    else:
        each = list[0]
        for i in list:
            if each < i:
                continue
            elif each > i:
                each = i # 核心
        return each

def min4(x): # # min()小甲鱼正解
    least = x[0]

    for each in x:
        if each < least:
            least = each

    return least

if __name__ == "__main__":
    list = [4,6,2,6,8,3,98,6,2,-1,8,8,8,8,-10,123,123,12,3,123,12,312,312,3,4,2354,4,56,-2,-123,-45465,-354,-34]
    print (min1(list))
    print (min2(list))
    print (min3(list))
    print (min4(list))