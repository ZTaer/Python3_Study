#!/usr/bin/python3
#-*- coding:utf-8 -*-

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

def power(x,n):
    if n == 1:
        return x
    else:
        return x*power(x,n-1)

def fb(n):
    if n <= 2:
        return 1
    elif n > 2:
        return fb(n - 1) + fb (n - 2)



if __name__ == "__main__":
    print(fact(3))
    print(power(3,4))
    print(fb(12))
