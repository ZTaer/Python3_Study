#/usr/bin/python3
#-*- coding:utf-8 -*-
import os

#   #   主要功能是删除指定文件目录及文件
#   检测是否为win系统os.name()
#   如果是则执行本程序
#   创建,sysif()函数来判断当前系统,并且返回需要扫描的挂载点( 接受必定扫描路径 )
#       寻找挂载点:d,e,f,g,h,i,j,k
#       返回可用挂载点
#   创建,findDirs()函数扫描指定文件及文件夹是否存在( 接受3个参数:  硬盘列表, 指定文件列表，指定文件夹列表 )
#       使用walk获取文件目录,判断是否有指定列表内容( 指定文件夹/文件 )
#           爬取挂载点所有文件路径并记录
#                   判断是否有指定文件
#                       是: 加入文件所在文件夹路径
#           爬取挂载点所有文件夹路径并记录
#                   判断是否有指定文件夹
#                       是:  记录路径
#       返回一个列表,记录的是指定文件的路径
#   创建,deleteDirs()函数用于删除指定文件夹( 接受1个参数: 指定文件夹路径 )
#       使用walk获取指定文件夹路径/所有文件路径
#           尝试删除文件
#           尝试删除文件夹
#   执行成功则在当前文件路径生成嘲讽TXT文档

def sysif( syssave=[] ):
    result = []
    result.extend( syssave )
    if os.name == 'nt':
        sysList = ['d:','e:','f:','g:','h:','i:','j:','k:']
        for each in sysList:
            try:
                os.listdir(each)
                result.append(each+os.sep)
            except:
                continue

    result = set(result)
    result = list(result)
    return result

def findDirs( disklist='' , dirsname=[] , filesname=[] ):
    result = []
    for road , dirs , files in os.walk(disklist,topdown=False):
        for each1 in files:
            result.append(road) if each1 in filesname else False
        for each2 in dirs:
            result.append(road+each2) if each2 in dirsname else False

    result = set(result)
    result = list(result)
    return result

def deleteDirs( road ):
    if len(road) > 0:
        for road , dirs , files in os.walk(road,topdown=False):
            for i in files:
                try:
                    os.remove(road+os.sep+i)
                except:
                    continue
            try:
                os.rmdir(road)
            except:
                continue

if __name__ =="__main__":
    dirname=['test111']
    filesname=['asd.txt']
    roadCPU = []
    for disks in sysif():
        roadCPU.extend( findDirs(disks , dirname , filesname) )
    for end in roadCPU:
        deleteDirs(end)



