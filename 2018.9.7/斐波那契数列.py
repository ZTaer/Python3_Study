#/usr/bin/python3
#-*-coding:utf-8-*-

#   斐波那契数列计算和
def F(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n <= 2:
        result = 1
    elif n < 0 :
        return -1
    while n > 2:
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        n -= 1
        result = n3
    return result

if __name__ == "__main__":
    print(F(55))
    
