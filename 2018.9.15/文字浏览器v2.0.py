#/usr/bin/python3
#-*- coding:utf-8 -*-
#   13:2输入13:21打印第13行到第21行，
#   输入:21打印前21行，
#   输入21:则打印从第21行开始到文件结尾所有内容
#   我打算将每一行加入列表中,然后利用list[1:4]特性显示元素( 核心 )

#   #   问题解决list[ 分号输入 ]
#   输入值有可能是"256"类型,"33:55"区别在于有没有":"号,简洁一点统一进行fontformart()进行格式化

#   创建fontformart()函数格式化line的值,接受line值,以及content核心列表
#   #   问题因为line值没有没有":"是二种算法
#   当没有":"时,由于是由range()控制所以line值不能是负数,且不能大于len(content)数量
#               line = int(line)
#               while当line<0或者line > len(content)时:
#                               如果line小于零line = --line
#                               如果line > len(content)时,line = len( content )
#               返回line值
#   当有":"时,字符串":"无法在列表切片使用。所以返回一个2位数字的列表
#               xylist = line.split(':')会出现空字符串
#               while 当xylist[0] == '' 或者 xylist[1] == '':
#                       如果xylist[0] == ''那么xylist[0] = 0
#                       如果xylist[1] == "那么xylist[1] = len( content ) + 1
#               返回xylist列表

#   创建fileInfo(road , line)函数,接受文件路径,以及显示行数
#               检查文件是否存在,如果错误则重新输入检测
#               成功打开文件要seek(0,0)
#               将文件中每一行加入列表content中( 为有":"情况下做准备 )
#               创建文件迭代it = iter( content ) ( 为没有":"情况下做准备 )
#   
#               如果road.find(':')小于0:
#                       line = 使用fontformart()进行格式化数值
#                       通过range( line )控制循环次数,来迭代显示next( it )
#               其它情况: ( line值中有":" ):
#                       line = 使用fontformart()进行格式化数值
#                       循环迭代出content[ line ]中元素

def fontformart( line , content ): #    格式化line值
    if line.find(':') < 0: #    没有":"情况下
        line = int(line)
        while line < 0 or line > len(content): # 保证没有负数,且不大于content元素数量
            line = -line if line < 0 else line
            line = len(content) if line > len(content) else line
        return line
    elif line.find(':') >= 0 : #    有":"情况下
        xylist = line.split(':')
        while xylist[0] == '' or xylist[1] == '': #  保证没有空字符串
            xylist[0] = 0 if xylist[0] == '' else int( xylist[0] )
            xylist[1] = len(content) + 1 if xylist[1] == '' else int( xylist[1] )
        return xylist
        
def fileInfo( road , line): #   主要功能函数
    #   #   文件路径验证
    while True:
        try:
            file = open('%s' % road , 'rt',encoding='utf-8')
            file.seek(0,0)
            print("<<<---打开文件成功--->>>\n")
            break
        except:
            print("文件不存在!")
            road = input("请重新输入: ")
    #   准备核心
    content = []
    for each in file:
        content.append( each )
    it = iter( content )
    #   行动核心
    if line.find(':') < 0 : #   line没有":"情况下
        line = fontformart( line , content ) #  格式化line值,保证没有负数,且不大于content元素数量
        for i in range( line ):
            print( next(it),end='' )
        print('\n<<<---     END      --->>>')
    else: # line有":"情况下
        line = fontformart( line , content ) #  格式化line值,保证没有空字符串
        for each1 in content[ line[0] : line[1] ]: # 列表的切片特性,迭代出元素
            print( each1,end='')
        print('\n<<<---     END      --->>>')
    
    
if __name__ == "__main__":
    road = input("目录文件: ")
    line = input("显示几行: ")
    fileInfo(road , line) #   主要功能函数
    
    
