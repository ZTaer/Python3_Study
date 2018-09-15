#/usr/bin/python3
#-*-coding:utf-8-*-

#   #   将上一题中的文件（OpenMe.mp3）保存为新文件（OpenMe.txt）
#   核心 content = str(f.read()) 可以将读取的文件转化成字符串
#   核心 f2.write(f1.read())


if __name__ == "__main__":
    #   #   打开文件 ,  并且一行一行的显示
    music = open('G:\\STUDY\\Python3\\2018.9.14\\OpenMe.mp3' ,'at+')
    music_txt = open('G:\\STUDY\\Python3\\2018.9.14\\OpenMe.txt' ,'at+')
    music.seek(0,0)
    for each in music:
        print(each)
        music_txt.write(each) # 写入文档
    music.close()
    music_txt.close()
        
        
        
    
    
