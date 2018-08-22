#!/usr/bin/python3
#-*- coding:utf-8 -*-
import time

# 简单电梯模拟v1.0 ---
#     循环：
#         设定目标楼层 -/ 输入模块
#         开门-无障碍物-关门 -/ 安全模块
#         从当前楼层到--目标楼层 -/ 执行模块
# #         开门-无障碍物-关门
#         -/ 消息模块

def inputnum():
    return int(input("输入目标楼层: "))

class Safety():
    def turndoor(self):
        return "开门"
    def offdoor(self):
        return "关门"
    def notsafe(self):
        return "有障碍物"
    def safe(self):
        return "无障碍物"

def aims(stars,end):
    print (stars)
    time.sleep(1)
    if stars > end:
        while True:
            stars = stars - 1
            if stars == 0:
                continue
            else:
                print (stars)
                time.sleep(1)
            if stars == end:
                print ("已到达: "+str(end))
                break
    elif stars < end:
        while True:
            stars = stars + 1
            if stars == 0:
                continue
            else:
                print (stars)
                time.sleep(1)
            if stars == end:
                print ("已到达: "+str(end))
                break
    elif stars == end:
        print("已到达: " + str(end))

if __name__ == "__main__":
    stars = 1
    sf = Safety()
    while True:
        end = inputnum()
        aims(stars,end)
        stars = end
        time.sleep(2)
        print(sf.turndoor())
        time.sleep(2)
        print(sf.safe())
        time.sleep(2)
        print(sf.offdoor())
        time.sleep(2)


