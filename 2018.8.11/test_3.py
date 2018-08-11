#!/usr/bin/python3
#-*- coding:utf-8 -*-
import random

#数据机构
    # 1.输入值
    #     输入一个数字
    #
    # 2.生成随机数字(0-10的整数)
    #
    # 3.判断值
    #     不正确(3次机会)
    #         提示太大
    #         提示太小
    #     正确
    #         游戏结束
    # 4.输出信息

#变量名称
    #num        输入的数字
    #change     剩余的机会数
    #sjs        答案随机数
    #sjsc       机会随机数

#消息模块
class Msg():
    def __init__(self,change,sjs):
        self.change = change
        self.sjs = sjs

    #输入提示
    def input_msg(self):
        return int(input("请输入一个数字(0-10): "))

    #错误提示
    def mini_msg(self):
        print ("提示: 太小\n")

    def max_msg(self):
        print ("提示: 太大\n")

    def change_msg(self):
        print ("剩余"+str(self.change)+"次机会")

    def lose_msg(self):
        print ("机会用尽你输啦!\n正确答案是: " + str(self.sjs))

    #正确提示
    def win_msg(self):
        print ("恭喜你,回答正确!\n")

#生成随机数
def ssjs():
    return random.randint(0,10)

def ssjsc():
    return random.randint(2, 5)

if __name__ == "__main__":
    sjsc = ssjsc()
    change = sjsc
    sjs = ssjs()
    print ("初始的机会数是看运气的哦!")
    while True:
        msg = Msg(change, sjs)

        if change <= sjsc and change >0:
            msg.change_msg()
            num = msg.input_msg()
            if num == sjs:
                msg.win_msg()
                break
            elif num > sjs:
                msg.max_msg()
            elif num < sjs:
                msg.mini_msg()
            change = change - 1
        else:
            msg.lose_msg()
            break
