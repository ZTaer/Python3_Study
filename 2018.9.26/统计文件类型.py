#/usr/bin/python3
#-*- coding:utf-8 -*-
import os

#   #   我想做一个,自动分析后缀名并建立数据统计
#   #   问题获取当前目录文件类型
#   利用os.listdir( os.curdir ) 来获取当前目录所有文件
#   使用split('.')进行分割处理判断后缀名

#   #   主体思路
#   创建equrtNum()函数接受2个参数一个值,一个列表,返回相同的数量
#       创建一个计数器count = 0
#       循环列表:
#               如果相等则coun进行加1
#       循环结束后返回"count"值
#   创建kindMain()函数分析文件后缀名几种类型( 接受一个路径 ,由kindMain()来进行当前目录格式类型统计)
#       使用os.listdir( os.curdir )获取当前文件目录文件
#       将分割后,每一个元素加入合集( add()函数可以加入合集元素 )
#       利用合集的不重复性set()可以转换为合集
#       合集转换为列表( 方便索引 )
#       返回列表
#   创建kindFile()函数确定类型后,在进行分别统计( 接受1个参数: 路径 )创建主体函数
#       将路径所有文件后缀名统计到一个列表( 重复性列表 )
#       使用kindMain()统计后缀名种类( 非重复性列表 )
#       创建结果列表result
#       for循环( 由kindMain()返回的列表 )
#           使用equrtNum()函数,接受2个参数一个值,一个列表,返回相同的数量
#           以元组的形式加入result列表( each , num )
#       返回result列表

def equrtNum( value , listown ): # 值与列表对比,返回相同的数量
    count = 0
    for  each in listown:
        count+=1 if value == each else False
    return count

def kindMain( road=os.curdir ): # 接受文件路径,统计文件类型( 利用合集的不重复性 )返回一个不重复性,文件种类列表
    file = os.listdir( road )
    listset = [] 
    listset = set(listset) # 创建没有值的空合集
    for i in file:
        cut = i.split('.')
        listset.add('文件夹') if len(cut) == 1 else listset.add(cut[len(cut) - 1]) # 文件夹没有后缀名, 所以需特殊照顾,len(cut) -1是保证取的是结尾值
    return list(listset)

def kindFile( road=os.curdir ): #    主体函数
    file = os.listdir( road )
    listown = [] # 重复性文件种类列表
    for i in file:
        cut = i.split('.')
        listown.append('文件夹') if len(cut) == 1 else listown.append(cut[len(cut) -1]) # 文件夹没有后缀名, 所以需特殊照顾,len(cut) -1是保证取的是结尾值
    listset = kindMain(road) # 非重复性文件种类列表
    result = [] # 结果列表
    for each in listset:
        num = equrtNum( each , listown ) # 获取文件种类相同值
        result.append((each,num)) # 以元组的形式存储进入结果列表
    return result
            

if __name__ == "__main__":
    for each in kindFile('C://'):
        print("[ %s ] 文件类型---共有[ %s ]个" % (each[0],each[1]) )
    
    
