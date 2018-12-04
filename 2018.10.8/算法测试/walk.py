#!/usr/bin/python3

import os
road = input('输入: ')
#   #   关于os.walk
#   接受:
#       接受3个数据参数,开始路径road,onerror错误报告默认为None可不写,反向目录获取topdown=False
#   返回:
#        一个元祖( road(所有文件夹路径 - 字符串类型) , dirs(所有文件夹名称 - 列表类型) , file(所有文件名称 - 列表类型) )
for road, dirs, files in os.walk(road, topdown=False):
    #   显示所有文件( 带路径位置 )
    for i in files:
        print( road+os.sep+i )

