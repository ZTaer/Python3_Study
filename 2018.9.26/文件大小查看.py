#/usr/bin/python3
#-*- coding:utf-8 -*-
import os

#   #   问题
#   os.curdir 为当前目录
#   我准备写一个可以自定义目录的文件大小统计
#   使用os.path.getsize()可以获取文件大小( 注意不能获取文件夹大小 )
#   os.path.join()可以组合路径

#   #   思路
# 首先获取路径下的所有文件,去除文件夹
#  创建结果列表
#       循环列表
#           获取大小
#           以元组的形式加入结果列表
#       返回列表
def fileSize(road = os.curdir): # 获取文件大小( 不包含文件夹 )
    filelist = [] # 文件列表
    result = [] # 结果
    file = os.listdir( road ) # 读取目录文件列表
    for each in file:
        cut = each.split('.') # 通过split()方法来区分,文件与文件夹
        filelist.append(os.path.join(road,each)) if len(cut) > 1 else False # 路径与符合条件的文件加入
    for i in filelist:
        filesize = os.path.getsize( i ) # 获取文件大小
        result.append(( os.path.basename(i) , filesize)) # 去掉文件路径加入结果列表
    return result
        
        
if __name__ == "__main__":
    listsize = fileSize()
    for i in listsize:
        print("%s-[ %s Bytes]" % (i[0],i[1]))
    
    




