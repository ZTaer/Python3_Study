#!/usr/bin/python3
#-*- coding:utf-8 -*-

if __name__ == "__main__":

    # 关于list()与len()
    a = 'asdasd'
    b = list(a) # 关于list()将,字符串转化成列表的元素
    c = len(b) # 关于len(),返回元素个数
    print (b)
    print (c)

    # 关于max(), 返回最大值.min()相反;在比较字母时实际比较是ascll码,但是字母和数字不可以混合比较
    e = (1,23,4,3425,32)
    e1 = [123,123,2134,4,523,21]
    e = max(e)
    e1 = max(e1)
    print (e,e1)

    # 关于sum() , 元素相加返回和
    f = [1,23,4,5,3]
    f1 = (12,23,2,43)
    print (sum(f) + sum(f1))

    # 关于sorted()与reversed()与sort()和reverse()没有什么区别

    # 关于enumerate(), 将引导值与元素值组成元组
    g = [23,34,5,6,23,2]
    g1 = list(enumerate(g))
    print (g1)

    # 关于zip() ,二个列表合并对应元素位置,组合成元组
    h = [1,2,3,4,5,6,7]
    h1 = [7,6,54,3,21,]
    print(list(zip(h,h1)))

