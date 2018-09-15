#/usr/bin/python3
#-*- coding:utf-8 -*-

if __name__ == "__main__":
    set1 = {1,2,3,4}
    print(set1)
    set1.add(233) # 添加元素
    set1.remove(2) # 移除元素
    print(set1)

    # 创建不可变合集
    set2 = frozenset([1,2,3,4])

    #   常用内置函数
    set1.pop() # 移除并返回一个任意元素

    set3 = {5,6}
    set1.update(set3) # 更新函数
    print(set1)
    
