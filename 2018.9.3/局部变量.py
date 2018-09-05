#/usr/bin/pyton3
#-*-coding:utf-8-*-

def test():
    global x # 加入global , 就相当于全局变量的x , 如果没有它就只是局部变量.
    x = 5
    return x

def test2():
    s = 20
    def test3():
        nonlocal s # 在使用" 非全局外部变量 "时加入nonlocal可防止错误 , 可以有效的将变量引用.
        s *= 2
        return s
    return test3()
        

if __name__ == "__main__":
    x = 10
    print(test())
    print(x)
    print(test2())
    
    
