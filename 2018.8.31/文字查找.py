#/usr/bin/python3
#-*- coding:utf-8 -*-

#   #   查找字符串问题
#   #   分析解决
#   输入待查找字符串 inputstr
#   输入查找目标 findstr

#   先判断输入的字符串数量(记录输入lennum )
#   不断循环索取inputstr中的值,判断是否与findstr[0]相等
#   如果相等则headEqual记录每一个二者相等的位置
#   由headEqual的长度决定循环次数
#       索取findstr[headEqual+1] (headEqual <= lennum),与,inputstr(headEqual+1)验证是否相等:
#       如果不等停止本次循环
#       如果此循环结束则sufltEqual + 1
#    当所有循环结束则输出结果

def findstr(inputstr,aims):
        lennum = len(aims)
        headEqual = [] # 开头位置相等列表
        i = 0 # 临时计数器
        sufltEqual = 0

        # 记录aims开头相等位置
        for each in inputstr:
                i += 1
                if each == aims[0]:
                        headEqual.append(i-1)
        for each1 in headEqual:
                for each2 in range(lennum): # 位移验证( 多位数字查找核心 )
                        if aims[each2] == inputstr[each1 + each2]:
                                correct = True
                        else:
                                correct = False
                if correct: # 此乃点睛之笔
                        sufltEqual += 1
        return sufltEqual

if __name__ == "__main__":
        inputstr = input("请输入目标字符串: ")
        aims = input("查找: ")
        print(findstr(inputstr,aims))
    
