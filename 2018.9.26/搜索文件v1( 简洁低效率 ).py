#/usr/bin/python3
#-*- coding:utf-8 -*-
import os
#   #   验证列表中是否存在文件
#   利用list.count()验证列表中是否有对应元素
#   for有个特性,如果迭代一个列表,列表不断的增加元素，那么for不断的循环

#   #   思路
#   将路径统计在一个列表中
#   使用路径生成法
#           读取路径,列出所有文件
#           检测到文件夹
#           路径+文件夹生成新路径

#           读取新路径,列出所有文件
#           检测到文件夹
#                   顺便使用count()检测查找的文件
#                   如果找到,记录路径
#           路径+文件夹生成新路径
#   #    具体实现
#   创建findFile()函数( 接受2个值,开始路径,及目标文件 )
#       创建路径列表listRoad
#       初始路径加入road

#       listdir()路径
#               检测到文件夹
#       初始路径+文件夹
#       加入listRoad列表

#   第一种写法,使用内置os函数( 代码简洁,效率不尽人意 )
def findFile(road='1' , name=0):
    listRoad = [] # 可访问路径列表
    listRoad.append(road) # 加入开始路径
    result = [] # 结果列表 
    for each in listRoad:
        try: # 防止,没有权限访问的文件夹报错
            file = os.listdir(each)
            result.append(os.path.join(each,name)) if file.count(name) else False # 验证目标文件是否存在
            for  i in file: # 检测是否有其它文件夹
                roadfile = os.path.join(each,i)
                if os.path.isdir( roadfile ) or os.path.ismount( roadfile ): # 有其它文件夹,则创建新的路径
                    listRoad.append(roadfile)
        except:
            print("--无法访问%s" % each)
            continue
    return result

        
if __name__ == "__main__":
    while True:
        road = input("查找路径: ")
        name = input("文件名称: ")
        if os.path.isdir(road) or road.os.path.ismount(road):
            for i in findFile(road,name):
                print(i)
            print("---END---")
            break
        else:
            print("路径不存在!")
    
