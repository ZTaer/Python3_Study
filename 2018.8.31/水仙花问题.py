# /usr/bin/python3
# coding:utf-8

#   #   水仙花问题:
#   寻找水仙花数   
#   题目要求：如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。
#   例如153 = 1^3+5^3+3^3

#   #   分析解决:
#   解决3位数字生成问题( 生成字符串形式为列表元素 )
#   循环:
#       计算元素各位数字的立方和
#       验证: 立方和结果是否与元素值相等
#       不相等则删除在列表中相应的元素
#   循环完毕后
#   最终列表即是结果

#   生成机制
def intThree():
    num = 100
    threeIntList = []
    for i in range(900):
        threeIntList.append(str(num))
        num += 1
    return threeIntList

#   计算并验证
def intCheck( intList ):
    sumint = 0
    for i in intList:
        for each in i:
            sumint += int(each) ** 3
        if i != str(sumint):
            intList.remove(i)
    return intList
        

if __name__ == "__main__":
    print (intCheck(intThree()))
    
