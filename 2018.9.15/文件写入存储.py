#/usr/bin/python3
#-*- coding:utf-8 -*-

#   #   问题多行输入
#   循环input输入来达到多行输入iter(input, stopword)
#   当检测到输入只等于":w"时结束循环
#   上面这些可以用Iter()解决
#   #   思路
#   创建文件并且输入文件名字
#   启动多行输入
#   将输入的内容写到创建的文件中

def content( file ):
    contentlist=[] # 创建存储内容的列表
    print("请输入存储内容: ")
    for each in iter(input, ':w'): # 循环input,如果检测到:w则停止循环
        contentlist.append(each+'\n') # 每一行输入末尾加入换行符号,并加入列表中
    file.writelines( contentlist ) 
        
if __name__ == "__main__":
    name = input("新建文件名: ")
    file = open('D:%s' % name , 'at+', encoding='utf-8')
    content(file)
    file.close()
