#!/usr/bin/python3
#-*- coding:utf-8 -*-

if __name__ == "__main__":

    # 字符串方法,位置更替format()
    a = "{0} love {1}".format("I" , "you")
    b = "{a} love {b}".format(a="I" , b = "you")
    print (a,b)

