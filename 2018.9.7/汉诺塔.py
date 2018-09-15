#!/usr/bin/python3
#-*- coding:utf-8 -*-
def hanoi(n,x,y,z):
    if n == 1:
        print(x, ' --> ',z)
    else:
        hanoi(n-1 , x , z , y) # n-1个盘子从x移动到y
        print(x, ' --> ',z) # 将底下最后一个盘子从x移动到z上
        hanoi(n-1,y ,x, z) # 将y上的n-1个盘子移动到z上
    print("E-N-D")

if __name__ == "__main__":
    hanoi_num = int(input("请输入盘子数量: "))
    # step_1second = int(input("请输入一秒可以运行步数: "))
    step = 2 ** hanoi_num - 1 # 步骤数量计算
    # second = step / step_1second # 时间计算
    # hour = second/3600
    # day = hour / 24
    # year = day / 365
    print("需要%d步完成!" % step)
    # print("大约需要: %d年 %d天 %d时 %f秒" % (year,day,hour,second))
    hanoi(hanoi_num,'X','Y','Z')
