#!/usr/bin/python3
#-*- coding:utf-8 -*-

# def MyFun((x, y), (a, b)):
#     return x * y - a * b

# 测试return
def hello():
    print('Hello World!')
    return
    print('Welcome To FishC.com!')


# 模拟pow()函数
# 分析一下pow(), pow(2,2) == 2**2 结果为4
def power(num=0,p=1):
    return num**p


# 利用欧几里得算法求出最大公约数
# 分析:
#     除数 >= 被除数
#     除数 % 被除数 = 余数
#     如果等于0
#         返回 被数数
#     否则继续
#         原被除数 % 原余数 = 新余数
#         如果等于0 则输出 原余数
#         否则继续循,环直到新得出余数为0
def gcd(m,n):
    while True:
        r = m % n
        m = n
        n = r
        if r == 0:
            return m
            break

def gcd2(x, y):
    while y:
        t = x % y
        x = y
        y = t
    return x


if __name__ == "__main__":
    print(gcd(2,4))
    print(gcd2(2,4))



