#/usr/bin/python3
#-*- coding:utf-8 -*-
import pickle

if __name__ == "__main__":
    #   存储
    test = [1,2,34,5,123,12,324,4,234,324,234,234]
    pickle_file = open('test.pkl','wb') # 后缀名随便写,不过最好要有提示性( 注意读取模式使用二进制写入 )
    pickle.dump( test , pickle_file ) # test列表保存到test.pkl文件
    pickle_file.close()

    #   读取
    pickle_file = open('test.pkl','rb') # 注意读取模式使用二进制读取
    test = pickle.load( pickle_file ) # 读取pickle文件
    print(test)
