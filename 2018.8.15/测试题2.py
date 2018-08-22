#!/usr/bin/python3
#-*- coding:utf-8 -*-

if __name__ == "__main__":
    list1 = ['1.jost do it' ,'2.一切皆有可能' , '3.让编程改变世界','4.Impossible' ]
    list2 = ['4.阿迪达斯','2.李宁','3.鱼c工作室','1.耐克']
    list3 = [name + '：' + slogan[2:] for slogan in list1 for name in list2 if slogan[0] == name[0]]
    for each in list3:
        print (each)

    # 字符串定位
    A = 'abcdefg'
    print ( A[0],A[3] ) # 通过这种方法直接可以索引出字符串数据
    print ( type( A[0]))