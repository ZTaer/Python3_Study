#!/usr/bin/python3
#-*- coding:utf-8 -*-

#数据结构
    #输入一个分数
    #   转化成浮点数类型
    #检测分类
    #打印消息
    #    xx分打印xx

def check_socre( score ):
    if score >= 90 and score <= 100:
        return "成绩评价为: A\n"
    elif score < 90 and score >= 80:
        return "成绩评价为: B\n"
    elif score < 80 and score >= 60:
        return "成绩评价为: C\n"
    elif score < 60 and score >= 0:
        return "成绩评价为: D\n"
    else:
        return "resume"


if __name__ == "__main__":
    input_score = float(input("输入分数( 100-0 ): "))
    check_socre(input_score)
    while True:
        if check_socre( input_score ) == "resume":
            input_score = float(input("超出成绩范围!\n请重新输入( 100-0 ): "))
            check_socre(input_score)
            continue
        else:
            print ( check_socre(input_score) )
            break

            
