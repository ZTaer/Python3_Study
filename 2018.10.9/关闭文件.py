#/usr/bin/python3
#-*-coding:utf-8 -*-

if __name__=="__main__":
    try:
        with open('My_File.txt') as file: # 用with 打开文件可以自动关闭文件
            print(file.read())
    except FileNotFoundError as x:
        print('错误FileNotFoundError: ' + str(x))
        

    
