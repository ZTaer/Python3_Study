#!/usr/bin/python3
#-*- coding:utf-8 -*-

if __name__ == "__main__":
    # 解析式方法
    list1 = [(x, y) for x in range(10) for y in range(10) if x % 2 == 0 if y % 2 != 0]

    # 常规方法
    list2 = []
    for x in range(10):
        if x % 2 == 0:
            for y in range(10):
                if y % 2 != 0:
                    list2.append((x, y))

    print (list1)
    print (list2)