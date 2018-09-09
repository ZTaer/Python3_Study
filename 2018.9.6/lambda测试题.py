#!/usr/bin/python3
#-*- coding:utf-8 -*-

# 返回一个lambda
def make_repeat(n):
    return lambda s: s * n

if __name__ == "__main__":
    s = lambda x, y=3: x * y
    print(s(5,5))

    # 求出3的倍数
    print(list(filter( lambda x : None if  x % 3 else x , range(1,99))))

    # 元组转换成列表
    listxy = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
    print(list(map(lambda y : list(y),listxy )))


    # 返回一个lambda
    double = make_repeat(2)  # double = lambda s : s * 2
    print(double(8))
    print(double('FishC'))
