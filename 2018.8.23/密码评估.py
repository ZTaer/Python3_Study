#!/usr/bin/python3
#-*- coding:utf-8 -*-
import re


# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位



# 核心点,判断字符串内容类型
# 如果只有数字or字母则.isalnum()
# 查看是否以指定字符开头(可自定义开始位置).startswith()
# 查看字符串中是否有指定字符串,有则返回索引值,否则返回-1.find()
# 统计指定字符串数量(可自定义位置),然后返回数量.count()


# 输入
def password():
    return (input("请输入密码: "))

class Check():

    def __init__(self,password):
        self.password = password

    # 低安全等级检测
    def check_danger(self):
        if self.password.isalnum():
            return True
        else:
            return False

    # 中/高安全等级检测

    def check_az(self):
        pattern = re.compile('[a-zA-Z]')
        if pattern.findall( self.password ):
            return True
        else:
            return False

    def check_num(self):
        pattern = re.compile('[0-9]')
        if pattern.findall(self.password):
            return True
        else:
            return False

    # 检测开头
    def check_head(self):
        pattern = re.compile('[a-zA-z]')
        if pattern.findall(self.password[0]):
            return True
        else:
            return False

    # 检测有无特殊符号
    def check_list(self):
        symbol = list('~!@#$%^&*()_=-/,.?<>;:[]{}\|')
        for each in symbol:
            if self.password.find(each) >= 0:
                result = True
                break
            elif self.password.find(each) < 0:
                result = False
        return result

    # 密码长度检测
    def check_len(self):
        return len(self.pas)

class Msg():
    def __init__(self,check_msg):
        self.check_msg = check_msg

    def checkmsg(self):
        print("你的密码安全级别评定为:",self.check_msg)

    def goodmsg(self):
        print("请继续保持")

    def badmsg(self):
        print('请按以下标准设置密码:\n\t'+
              '1.密码必须有数字,字母,特殊符号三种组合\n\t' +
                '2.密码只能由字母开头\n\t' +
              '3.密码长度不能低于16位')

if __name__ == "__main__":
    password = password()
    ck = Check(password)

    if ck.check_len() <= 8:
        safe = '低'

    elif ck.check_len() >= 16 and ck.check_head():
        if ck.check_num() and ck.check_list() and ck.check_az():
            safe ='高'

    elif ck.check_len() > 8:
        if ck.check_az() and ck.check_num():
            safe = '中'
        elif ck.check_az() and ck.check_list():
            safe = '中'
        elif ck.check_num() and ck.check_list():
            safe = '中'
        else:
            safe = '低'
    else:
        safe = '低'

    msg = Msg(safe)
    msg.checkmsg()

    if safe =='高':
        msg.goodmsg()
    else:
        msg.badmsg()
















