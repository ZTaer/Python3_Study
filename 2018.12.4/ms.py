#!/usr/bin/python3
#-*- coding:utf-8 -*-
import os
import time

#   功能1: 莫斯密码( 从txt文档中读取 )翻译成英文与数字
#   功能2: 英文与数字翻译成摩斯密码( 并存储到一个txt文档里 )
#   #   问题
#   存储摩斯密码表,以字典的形式msdict = {“A”:'.-',"B":'-...'}
#   1.问题摩斯密码 到 英文与数字
#       获取txt文档,以空格为分割点，创建读取到的摩斯密码内容列表fileMsList
#       创建结果列表
#       迭代fileMsList
#         如果列表中无'-'or'.'则直接将值加入结果列表
#           迭代msdict.items()
#               fileMsList内容与内容对比相同则输出key值
#               key值加入结果列表
#       显示结果,writelines(list)并txt文件保存结果列表
#  2.问题英文数字 到 摩斯密码
#  os读取文件内容整理成列表fileContentList
#  迭代每一个元素
#       判断是否为字母or数字否则直接加入结果列表
#           将msdict[迭代值]元素加入结果列表
#  显示结果writelines(list)并txt文件保存结果列表
msdict = {
    "A":".-",
    "B":"-...",
    "C":"-.-.",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    "1":".----",
    "2":"..---",
    "3":"...--",
    "4":"....-",
    "5":".....",
    "6":"-....",
    "7":"--...",
    "8":"---..",
    "9":"----.",
    "0":"-----"
}
def msToaz(road): # 摩斯密码转字母数字
    result = []
    with open("%s" % road,"rt+",encoding="utf-8") as file:
        file.seek(0)
        for msLines in file:
            for ms in msLines.split(" "):
                print(ms)
                if "-" in ms or "." in ms:
                    print("1")
                    for key , values in msdict.items():
                        if ms == values:
                            result.append(key)
                        elif ms == values+"\n":
                            result.append(key+"\n")
                else:
                    result.append(ms)
    print(result)
    return  result

def azToms(road):
    file = open("%s" % road, 'rt+', encoding='utf-8')
    file.seek(0)
    fileMsList = list(file.read().upper()) # upper()小写字母全部变大写,字符串内容转列表元素(其实不转列表直接迭代字符串也是可以的,但是过段时间长忘记这件事情,出于容易理解转换列表把)
    result = []
    for az in fileMsList:
        result.append(msdict[az]) if az.isalnum() else result.append(az) # msdict[az]字典键值读取的内容直接加结果列表
        result.append(" ") # 每一个翻译结果加一个空格,在写入文件后更加人性化
    file.close()
    return result

def wq( result ): # 交互式存储文件
    siveName = input("是否保存Y/N: ").upper()
    if siveName == 'Y':
        fileName = input("保存文件名为(.txt): ")
        file = open('%s.txt' % fileName , 'wt+')
        file.writelines(result) # writelines()可以将列表内容写入文件
        file.close()
        print("保存成功 - 位置: 执行程序当前目录\n")
    else:
        print("未保存文件\n")

if __name__ == "__main__":
    power = True
    while power:
        print("1 - 摩斯密码-转-字母数字")
        print("2 - 字母数字-转-摩斯密码")
        print("q - 退出程序")
        choose = input("选择功能: ").upper()
        if choose == '1':
            road = input("请输入待转换文档路径: ")
            result = msToaz(road)
            print("转换成功: %s" % result)
            wq(result)
        elif choose == '2':
            road2 = input("请输入待转换文档路径: ")
            result2 = azToms(road2)
            print("转换成功: %s" % result2)
            wq(result2)
        elif choose == 'Q':
            print("程序结束,谢谢使用!")
            time.sleep(1)
            power = False
        else:
            print("输入错误,请重新输入!")