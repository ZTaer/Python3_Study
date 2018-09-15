#/usr/bin/python3
#-*-coding:utf-8-*-
#   #   关于lambda用法
#   #   关于filer()过滤器用法
#   #   关于map()便捷加工用法

if __name__=="__main__":
    g = lambda x : x**2 
    print(g(5))

    add1 = lambda x,y : x+y
    print(add1(5,6))

    print(list(filter(None,[ 1,0,True,False ]))) #  返回真

    test = filter( lambda x : x % 2 , range(9) ) #  返回偶数
    print(list(test))

    test2 = map( lambda x : x**2 , range(9)  ) #    便捷式加工
    print( list(test2) )
