#/usr/bin/python3
#-*- coding:utf-8 -*-
import os

#   #   问题搜索视频文件
#   读取路径已经在上一题解决
#   #   想法
#   读取路径后,os.listdir()读取所有文件后,使用split()进行后缀名获取,如果符合要求则加入列表
#   反向思维,后缀名获取后,要求格式列表.count( 获取的后缀名 )如果为True加入结果列表
#   思路
#   创建格式列表video = []
#   获取后缀名末尾, end = cut[ len(cut) - 1 ]
#   video.count( end )如果为真,加入结果列表 

def findFile(road='1' ): # 接受2个参数( 开始路径,目标文件 )
    listRoad = [] # 可访问路径列表
    listRoad.append(road) # 加入开始路径
    result_video = [] # 搜索结果
    result_music = []
    result_spaci = []
    video = ['mp4','rmvb','3gp','avi','rm','flv','mov'] # 视频查找格式要求
    music = ['mp3','wmv','wma','mod','ra','md'] # 音乐查找要求
    spaci = ['exe']
    for each in listRoad: 
        try: 
            file = os.listdir(each)  
            for i in file: 
                roadfile = os.path.join(each,i)
                cut = i.split('.')
                
                #   #   修改点 - 获取后缀名末尾,video.count( end )如果为真,加入结果列表
                end = cut[ len(cut) - 1 ]
                if len(cut) == 2: # 当不是文件夹时,进行验证
                    result_video.append(roadfile) if video.count(end) else False
                    result_music.append(roadfile) if music.count(end) else False
                    result_spaci.append(roadfile) if spaci.count(end) else False
                    
                if len(cut) == 1: 
                    listRoad.append(roadfile)
                elif len(cut) > 2:  
                    try:
                        if os.path.isdir(roadfile): 
                            listRoad.append(roadfile)
                        else: # 多单位时当不是文件夹时,进行验证
                            result_video.append(roadfile) if video.count(end) else False
                            result_music.append(roadfile) if music.count(end) else False
                            result_spaci.append(roadfile) if spaci.count(end) else False
                    except:
                        # print('----无法访问%s文件夹' % roadfile)
                        continue      
        except:
            # print('----无法访问%s文件夹' % each)
            continue
    return ( '空' if len(result_video) == 0 else result_video , '空' if len(result_music) == 0 else result_music, '空' if len(result_spaci) == 0 else result_spaci )

if __name__ == "__main__":
    road = input("查找路径: ")
    file = findFile(road)
    
    print("----视频")
    for each in file[0]:
        print(each)
        
    print("----音乐")
    for i in file[1]:
        print(i)

    print("----EXE")
    for i in file[2]:
        print(i)
    result = open('搜索结果.txt','wt+',encoding='utf-8')
    for each1 in file:
        for each2 in each1:
            result.writelines(each2+'\n')
    result.close()
    
    

    
