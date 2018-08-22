#!/usr/bin/python3
#-*- coding:utf-8 -*-

if __name__ == "__main__":
    name = input('请输入用户名: ')
    score = [['迷途',85],['黑色',99],['SB',0]]
    pass1 = False
    for each in score:
        if each[0] == name:
            print (name + '得分: ',each[1],'分')
            pass1 = True
            break
    if not pass1:
        print("无此用户")


