#!/usr/bin/python3
#-*- coding:utf-8 -*-

if __name__ == "__main__":

    # 字符串方法,位置更替format()
    a = "{0} love {1}".format("I" , "you")
    b = "{a} love {b}".format(a="I" , b = "you")
    print (a,b)

# # 字符串格式修改函数

    # 字符串开头字母大写
    a1 = 'zhao teng'.capitalize()
    print (a1)

    # 字符串全部小写
    a2 = 'Zhao'.casefold()
    print (a2)

    # 字符串剧中
    a3 = 'a'.center(15)
    print (a3)

    # 设置tab空格大小
    a6 = 's\tpace'.expandtabs(tabsize=4)
    print(a6)

    # 以字符串作为分隔符，插入到111中所有的字符之间
    a19 = 'oo7'.join('111')
    print (a19)

    # 大写转小写字母
    a20 = 'oosdASD'.lower()
    print (a20)

    # 去掉字符串左边空格
    a21 = '  oo77  '.lstrip()
    print (a21)

    # 替换(原内容,新内容,替换次数)
    a22 = 'abcdeasdfasdcas'.replace('a','1',3)
    print (a22)

    # 去掉末尾空格
    a24 = 'oo7a '.rstrip()
    print (a24)

    # 查看是否以指定字符开头(可自定义开始位置)
    a25 = 'zhaosdsd'.startswith('zhao',0,4)
    print (a25)

    # 删除前后空格
    a26 = ' asdasdaadss '.strip()
    print (a26)

    # 大小写翻转
    a27 = 'asdsASD'.swapcase()
    print (a27)

    # 强制开头大写其他小写
    a28 = 'zhao'.title()
    print (a28)

    # 所有小写转化为大写
    a29 = 'asdasd'.upper()
    print (a29)


# # 部分字符串内容判断函数

    # 统计指定字符串数量(可自定义位置),然后返回数量
    a4 = 'jkhaksdnbfkbnavnboabdofe'.count('a',0,4)
    print (a4)

    # 判断是否以指定字符串结尾(可自定义位置),是则返回True否则返回False
    a5 = 'asdasoo7'
    test = a5.endswith('oo7')
    print (test)

    # 查看字符串中是否有指定字符串,有则返回索引值,否则返回-1
    a7 = 'asdasdasdzhaoasfloo7asds'.find('oo7')
    print (a7)

    # 与find功能一样,从右开始查找
    a23 = 'zhaoteng'.rfind('en')
    print(a23)

# # 整体字符串类型判断函数

    # 如果字符串只有字母数字则返回True
    a8 = 'asdasdasd'.isalnum()
    a9 = '123123123'.isalnum()
    a10 = 'asdas/23123asd'.isalnum()
    print (a8,a9,a10)

    # 如果字符串全部是字母则返回True
    a11 = 'aaa22'.isalpha()
    print (a11)

    # 如果字符串全为10进制则返回True
    a12 = '123123'.isdecimal()
    print (a12)

    # 如果字符串全为数字则返回True
    a13 = '12312a333'.isdigit()
    print (a13)

    # 如果字符串全为小写字母则返回True
    a14 = 'asds'.islower()
    print (a14)

    # 如果字符串全为数字则返回True
    a15 = '12312a333'.isnumeric()
    print (a15)

    # 如果字符串全为空格则返回True
    a16 = ' '.isspace()
    print (a16)

    # 如果字符串开头大写,其余小写则为True
    a17 = 'Aasd'.istitle()
    print (a17)

    # 如果字符串字母全部为大写则返回True
    a18 = 'ASDDa'.isupper()
    print (a18)






