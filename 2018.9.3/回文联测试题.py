#/usr/bin/python3
#-*- coding:utf-8 -*-

#   #   判断是否为回文联
#   列如: 上海自来水来自海上
#   #   分析解决
#   目测有二种情况:
#           1.字符串为偶数情况下
#           2.字符串为寄数情况下
#   解决len奇偶数判断问题,如果i%2如果余1则为寄数得0则为偶数
#   1.当len值为偶数情况下:
#                 len(a) = 8
#                 截取a[:len(a)//2] == a[len(a)//2:][::-1] 进行对比 ( [::-1]是切片参数应用,此时进行字符串反转排序 )
#   2.当len值为寄数情况下:
#                 len(b)
#                截取b[: len(b)//2 ] == b[len(b)//2+1: ][::-1] 进行对比 
#   截取完片段则进行对比
def count( countstr ):
    end = False
    def reversestr( x ):
        return x[::-1]
    if len( countstr ) % 2 == 0:
        if countstr[ : len( countstr )//2 ] == countstr[ len(countstr)//2:][::-1]:
            end = True
    elif len( countstr ) % 2 ==1:
        if countstr[:len(countstr)//2] == countstr[ len(countstr)//2+1:][::-1]:
            end = True
    return end

'''
另外一种方法
def palindrome(string):
    list1 = list(string)
    list2 = reversed(list1)
    if list1 == list(list2):
        return '是回文联!'
    else:
        return '不是回文联！'
print(palindrome('上海自来水来自海上'))
'''

if __name__=="__main__":
    if count( input("请输入: ") ) :
        print("是回文联!")
    else:
        print("不是回文联!")

    
    
    
    
