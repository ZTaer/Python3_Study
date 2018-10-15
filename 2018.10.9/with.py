#/usr/bin/python3
#-*- coding:utf-8 -*-

if __name__=="__main__":
    try:
        for each1 in range(3):
            for each2 in range(3):
                if each1 == 2:
                    raise KeyboardInterrupt
                print(each1,each2)
    except KeyboardInterrupt :
        print('退出')
#    with open('e://test.txt','w') as file:
#        print('OK')

    
