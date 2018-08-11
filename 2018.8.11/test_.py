#!/usr/bin/python3
#-*- coding:utf-8 -*-
import random

n = 5

def inputNum():
    num = int(input("请输入数字(0-10): "))
    return num

def ifNum( num ):
    x = random.randint(0,10)
    if num == x:
        print ("正确")
        print ("游戏结束!")
        return "a"
    else:
        print ("错误")
        print ("正确答案:"+str(x))
        print ("")



if __name__ == "__main__":
    print ("你一共有5次机会")
    while True:
        print("剩余" + str(n) + "次机会")
        n = n-1
        if n <= 5 and n >= 0:
            if ifNum(inputNum()) == "a":
                break
            else:
                continue
        else:
            print ("机会已用完!")
            print ("游戏结束!")
            break