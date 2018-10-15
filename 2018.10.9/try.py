#/usr/bin/python3
#-*- coding:utf-8 -*-

if __name__=="__main__":
    try:
        with open('e://test.txt','wt+') as file:
            for i in file:
                print(i)
    except NameError as x:
        print('NameError'+str(x))
    else:
        print('成功读取')
