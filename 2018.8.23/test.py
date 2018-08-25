#!/usr/bin/python3
#-*- coding:utf-8 -*-
import re

# 正则表达式判断密码

if __name__ == "__main__":
    pattern = re.compile( '[a-zA-Z]' )
    result = pattern.findall('asdasd')
    print (result)
    if result:
        print ('1')
    else:
        print('2')


