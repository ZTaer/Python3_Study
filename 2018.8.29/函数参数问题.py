#!/usr/bin/python3
#-*- coding:utf-8 -*-

# 给于参数默认值,可以保证在没有参数情况下不出错
def test (name = 0 , score = 0):
    print (name,':',score)

# 防止参数传递顺序错误的问题
def test2 (name = 0 , score = 0):
    print(name, ':', score)

# 收集参数,可以传入多个参数( 保存为元组 )
def test3 (*name , score = 0): # "*name"可以收集多个参数,并保存为元祖.
    print(name[:], ':', score)

if __name__ == "__main__":
    test()
    test2(score=88 , name ='赵飞')
    test3('赵',1,2,3,4,'a',score='5000000000')





