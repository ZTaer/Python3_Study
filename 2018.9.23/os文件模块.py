#!/usr/bin/python3
#-*- coding:utf-8 -*-
import os
import time
#   #   OS模块练习
if __name__ == "__main__":
    #   主要OS命令
    os.getcwd() # 获取当前工作目录
    os.listdir('E:\\') # 列出文件目录
    os.chdir('E:\\STUDY') # 更换工作目录为
    os.mkdir('E:\\Study\\Python3\\OS_Test') # 创建单层文件夹
    os.makedirs("E:\\Study\\Python3\\OS_Test\\A\\B") # 创建多层文件夹
    open('E:\\Study\\Python3\\OS_Test\\test.txt', 'wt+') # 创建一个TXT文档
    os.chdir('E:\\STUDY\\Python3') # 更换工作目录
    os.remove('OS_Test\\test.txt') # 删除文件
    os.removedirs('A\\B')   # 删除目录
    os.mkdir('OS_Test\\Test') # 创建目录
    os.rename('TEST', 'test') # 修改文件名
    os.system('cmd') # 使用当前系统SHELL命令
    #   没有括号OS小参数
    os.curdir # 当前目录'.'
    os.pardir # 上一级目录'..'
    os.sep # 显示当前操作系统的路径符号
    os.linesep # 显示当前系统的终止符
    os.name # 查看当前系统（包括：Linux系统'posix',  win系统'nt', 'mac', 'os2', 'ce', 'java'）

    #   # os下的path,主要修改关于路径的函数
    os.path.basename('E://test.txt') # 去掉路径只保留文件名字
    os.path.dirname('E://test.txt') #   与basename()相反

    os.path.join('E://', 'test.txt') # 路径组合
    os.path.split('E://test.txt') # 分割路径,返回一个元组(其实就是将路径最后一位分割)
    os.path.join('E://', 'test.txt') #  分割文件扩展名
    os.path.getsize('E://Study') # 获取文件大小( 单位为字节 )
    os.path.getatime() # 查看访问时间(浮点数秒为单位)
    os.path.getctime() # 查看创建时间
    os.path.getmtime() # 查看修改时间

    #   因为getatime及其他,返回的是,单位秒的浮点数,所以需要gmtime()来转换
    import time
    import os
    time.gmtime(os.path.getatime('E://Stuey//dns.png'))