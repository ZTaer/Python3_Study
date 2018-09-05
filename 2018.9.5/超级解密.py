#/usr/bin/python3
#-*-coding:utf-8-*-
import re

#   #   问题分析:
#   每一个密码为小写字母
#   每个密码左右二边均只有3个大写字母
#   #   分析解决
#   我打算用正则表达式
#   首先找到并以列表的形式记录所有小写字母的位置
#                   利用for循环
#   然后逐一验证小写字母左右二边是否为大写字母
#                   先用截片前后3并合并成字符串
#                   判断是否全部为大写字母
#                           否:  则移除小写字母对应的列表元素
#   循环验证后,输出所有列表对应元素
def supercount( content ):
    az = 'qwertyuiopasdfghjklzxcvbnm'
    password = []
    posnum = 0
    for i in content:   #   记录所有小写字母位置
        posnum += 1
        for y in az:
            if i == y:
                password.append(posnum-1)
    return password
                
    

    


if __name__ == "__main__":
    print(supercount('asdasdasd%^&*GHasdasdLHL'))
    
