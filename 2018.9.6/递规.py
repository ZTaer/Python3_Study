#/usr/bin/python3
#-*-coding:utf-8-*-

def test( x ): # 普通写法
    y = 1
    for i in range(1,x+1):
        y *= i
    return y

def test2( x ): # 递归写法
    if x == 1:
        return 1
    else:
        return x * test2(x-1)

if __name__ == "__main__":
    print(test(5))
    print(test2(5))

