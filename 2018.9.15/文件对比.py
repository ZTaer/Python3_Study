#/usr/bin/python3
#-*- coding:utf-8 -*-
#   #   问题文件对比
#   输入打开二个对比的文件
#   如果文件不存在则重新输入( 使用try可以搞定 )
#   文件打开使用seek()初始化
#   利用while循环( 当len(file.readline()) != 0 and len(file2.readline()) != 0 不满足条件结束循环  )
#           每一次循环cont加1来记录对比行数位置
#           判断readline()是否相等
#               不相等cont值加入noequal列表
#   结束循环后
#   打印出len(noequal)一共几处不同
#   分别打印出哪里不一样通过循环迭代'%s' % each

def compared(file1,file2):
    noequal = []
    count = 0
    file1.seek(0,0)
    file2.seek(0,0)
    f2 = iter(file2)
    for each in file1:
        count +=1
        if each != next(f2):
            noequal.append(count) # 记录不同处行数位置
    return noequal

if __name__ == "__main__":
    #   打开并验证文件是否正常
    print("请输入对比文件名!")
    while True:
        name1 = input("A文件名: ")
        name2 = input("B文件名: ")
        try:
            file1 = open('%s' % name1, 'rt')
            file2 = open('%s' % name2, 'rt')
            break
        except:
            print("文件不存在请重新输入!")

    #   比较处理
    noequal = compared(file1,file2) # 返回一个列表

    #   输出结果
    print("共有%s处不同" % len(noequal))
    for i in noequal:
        print("第 %s 行不同" % i)
    test(file1)
    file1.close()
    file2.close()
    
    

    
    
