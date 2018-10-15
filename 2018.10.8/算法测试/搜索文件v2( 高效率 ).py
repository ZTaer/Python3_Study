#/usr/bin/python3
#-*- coding:utf-8 -*-
import os
#   #   验证列表中是否存在文件
#   利用list.count()验证列表中是否有对应元素( 核心1 )
#   for有个特性,如果迭代一个列表,列表不断的增加元素，那么for不断的循环 ( 核心2 )

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

#   #   此为方法二,代码虽然多,但是效率绝对牛逼!

def findFile(road='1' , name=0): # 接受2个参数( 开始路径,目标文件 )
    listRoad = [] # 可访问路径列表
    listRoad.append(road) # 加入开始路径
    for each in listRoad: # 迭代可访问路径列表,进行逐一验证
        try: # 有些文件夹没有权限访问,使用try防止报错
            file = os.listdir(each)
            for i in file: # 迭代文件列表,检测是否有其他文件夹( 使用split()方法 )
                roadfile = os.path.join(each,i)
                cut = i.split('.')
                if len(cut) == 1: # 单位为1时为文件夹,加入路径列表
                    listRoad.append(roadfile)
                elif len(cut) > 2: # 单位大于2时( 有些文件夹的名称有"."所以使用os.path.isdir()进行二次验证是否为文件夹 )
                    try:
                        if os.path.isdir(roadfile): # 真则加如可访问路径列表( os.path.isdir()判断是否为目录 )
                            listRoad.append(roadfile)
                    except:
                        # print('----无法访问%s文件夹' % roadfile)
                        continue
        except:
            # print('----无法访问%s文件夹' % each)
            continue
    print('--GO--')
    for i in listRoad:
        print(i)
    print('--END--')
    return None

if __name__ == "__main__":
    road = input("查找路径: ")
    findFile(road)
        
    
    
