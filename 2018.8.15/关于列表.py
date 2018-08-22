#!/usr/bin/python3
#-*- coding:utf-8 -*-

if __name__ == "__main__":
    # test = [ 'A','B',12,21.2,'c' ]
    # test.append('D') #增加单个元素
    # test.extend(['d','e']) #增加多个元素
    # test.insert(0,'S') #自定义位置注入元素
    # print(test)

    # test = ['A', 'B', 12, 21.2, 'c']
    # test.remove('c') # 必须知列表元素值才能删除
    # del test[0] # 删除元素
    # cut = test.pop(1) # 取出元素
    # print ( test )
    # print ( cut )

    list = [1,2,3,4,5,6,1,1,3,3,44,5]
    list.count(1) # 查看列表中相同元素数量
    list.index(44) # 查看元素在列表中的序列

    list.reverse() # 列表序列元素翻转
    list.sort() # 从小到大排序
    list.sort(reverse=True) # 先排序后翻转( sort可以添加一些参数来进行排序 )



