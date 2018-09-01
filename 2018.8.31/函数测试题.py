#/usr/bin/python3
#coding:utf-8

#   #   问题:
#   0. 编写一个符合以下要求的函数：
#   a) 计算打印所有参数的和乘以基数（base=3）的结果
#   b) 如果参数中最后一个参数为（base=5），则设定基数为5，基数不参与求和计算。

#   #   分析解决:
#   需要给函数创建一个关键字参数,用于接受多个参数
#   元祖转化成列表
#   取出最后一位设置base基数
#   sun(合并列表元素)
#   与base计算
#   计算结果返回

def test( *listbase ):
    listsum = []
    for i in listbase:  # 元组转化成列表
        listsum.append(i)
    base = listsum.pop(len(listsum) - 1) # 取列表最后一位元素,设置为base
    print(base)
    return sum(listsum)*base

if __name__ == "__main__":
    print( test(1,2,3) )
    
