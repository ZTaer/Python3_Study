#!/usr/bin/python3
#-*- coding:utf-8 -*-

#   斐波那契数列递归算法
def F(n):
    if n == 1 or n == 2:
        return 1
    elif n < 0:
        return -1
    if n > 2:
        return F(n - 1) + F(n - 2)

if __name__ == "__main__":
    print(F(40))

