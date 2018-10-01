#/usr/bin/python3
#-*- coding:utf-8 -*-

#   多位文字替换
#   实验1: 每一行加入列表中
#   实验2: 整体修改
#   第一种方法( 我使用的方法 ): split()生成列表,通过inset()插入需修改的值
#   而这种方法的关键点在于,插入点在哪
#   第二种方法( 小甲鱼的方法 ): replace()函数可以替换字符串内容

#   #   思路

#   #   创建intonum函数,接受1个参数,linelist的长度
#   #   问题解决生成关键插入点列表intonum = []
#   3.1.3
#   4.1.3.5
#   5.1.3.5.7
#   6.1.3.5.7.9
#   count = 1 初始化
#   循环range( len(原列表) - 1 ):
#           count加入intonum列表
#           count+=2
#   返回intomum列表

#   #   问题查找值
#   其实文件被seek()后,直接len(file.read().split(' 原文字 ')) - 1即可得到


#   创建fontReplace()函数接受3个参数: file文件,otext原文字,etext修改文字
#   验证打开的文件( 别忘记seek(0,0) )
#   将每一行加入列表
#   加入计数器count( 转换写入模式做准备 )
#   跌带列表，单个处理每一行
#           使用mainReplace()传入,一行文字,原文字,修改文字
#           当count == 1使用
#               传入的每一行文字写入file文件( 注意打开模式为wt+覆盖写入 )
#           其它情况下使用
#               传入的每一行文字写入file文件( 注意打开模式为at+追加写入 )
#           count +=1
#   处理完毕,显示文件使有内容


#   #   创建mainReplace()函数,一行文字,原文字,修改文字
#   一行文字进行split处理linelist
#   循环intonum关键点:
#           linelist.insert( 关键点,修改文字 )
#   插入处理完毕后,将linelist列表元素相加,转化成字符串
#   返回一行字符串
def intonum( num ):
    intolist = []
    count = 1
    for i in range( num-1 ):
        intolist.append(count)
        count+=2
    return intolist

def mainReplace( line , otext , etext ):
    linelist = line.split(otext)
    result = ''
    for each in intonum( len(linelist) ):
        linelist.insert( each , etext )
    for i in linelist:
        result += i
    return result

def fontReplace( name , otext , etext):
    while True:
        try:
            file = open( '%s' % name , 'rt', encoding='utf-8' )
            file.seek(0,0)
            break
        except:
            print("文件不存在 ! ")
            name = input("重新输入: ")
    content = []
    count = 1
    for each in file:
        content.append(each)
    file.close()
    for line in content:
        line_new = mainReplace( line , otext , etext )
        if count == 1:
            file = open( '%s' % name , 'wt+', encoding='utf-8' )
            file.seek(0,0)
            file.write(line_new)
            file.close()
        else:
            file = open( '%s' % name , 'at+', encoding='utf-8' )
            file.seek(0,0)
            file.write(line_new)
        count+=1
    file.close()

def findnum( name,otext ):
    while True:
        try:
            file = open( '%s' % name , 'rt', encoding='utf-8' )
            file.seek(0,0)
            break
        except:
            print("文件不存在 ! ")
            name = input("重新输入: ")
    result = len(file.read().split(otext)) - 1
    return result
    

if __name__ == "__main__":
    name = input("文件名: ")
    otext = input("修改值: ")
    etext = input("修改为: ")
    num = findnum( name,otext )
    print( "文件%s中共有%s个[ %s ]" % (name , num , otext) )
    print( "你确定将全部[ %s ]替换成[ %s ]吗?" % (otext , etext) )
    while True:
        chose = input("YES/NO: ").lower()
        if chose == 'yes':
            fontReplace(name , otext , etext)
            print("修改成功!")
            break
        elif chose == 'no':
            print("取消修改!")
            break
        else:
            print("输入有误,请重新输入!")


