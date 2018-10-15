#/usr/bin/python3
#-*- coding:utf-8 -*-
import random

def intnum( num ): # 转换成整数类型数字
    while True:
        try:
            num = int(num)
            break
        except:
            num = input("请输入整数类型数字: ")
    return num
    

if __name__=="__main__":
    secret = random.randint(1,10)
    print('------------------我爱鱼C工作室------------------')
    
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
    guess = intnum(temp)
    
    while guess != secret:
        temp = input("哎呀，猜错了，请重新输入吧：")
        guess = intnum(temp)
        
        if guess == secret:
            print("我草，你是小甲鱼心里的蛔虫吗？！")
            print("哼，猜中了也没有奖励！")
        else:
            if guess > secret:
                print("哥，大了大了~~~")
            else:
                print("嘿，小了，小了~~~")
    print("游戏结束，不玩啦^_^")
