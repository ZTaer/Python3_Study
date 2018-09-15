#/usr/bin/python3
#-*-coding:utf-8-*-



if __name__=="__main__":
    #   #   创建字典
    #   标准创建字典方法
    dict1 = { 1 : ' one ', 2 : 'two' }

    #   利用dict()方法创建字典
    dict2 = dict(三='three', 四='four' ) # 此方法"键值"有问题!
    dict3 = dict((( 5,' five ' ), (6,' six ')))

    # 利用fromkeys()创建字典( 主要用来创建键值 )
    dict4 = {}
    dict5 = {}
    dict4 = dict4.fromkeys((range(5)),'seven')
    dict5 = dict5.fromkeys((1,2,3),'eight')

    print(dict1,dict2,dict3,dict4,dict5)

    #   #   字典的修改/创建元素
    a={1:'what' , 2:'fuck'}
    print(a)
    a[1] = 'hello' # 通过键值修改对应元素
    a[3] = '!' # 添加元素
    print(a)

    #   #   迭代字典元素
    # keys(),values(),items()
    b={}
    b = b.fromkeys((range(10)),'无')
    for eachkeys in b.keys(): # 迭代出字典键值
        print(eachkeys)
    for eachvalues in b.values(): # 迭代出字典内容
        print(eachvalues)
    for eachitems in b.items(): # 以元组的形式迭代出字典完整元素
        print(eachitems)

    #   #   清空字典
    c = {}
    c = c.fromkeys((range(10)),'hello')
    print(c)
    c.clear()
    print(c)

    #   #   取出字典元素
    #   pop() 取出字典单个元素
    #   popitem() 随机返回并删除字典中的一对键和值(一般删除末尾对)
    f = {}
    f = f.fromkeys((range(5)),'hello')
    f.pop(1)
    f.popitem()
    print(f)

    #   #   通过setdefault() 添加字典元素
    g = {}
    g = g.fromkeys((range(5)),'wokao!')
    print(g)
    g.setdefault(5,'2333')
    print(g)
    #   通过便捷方法添加字典元素
    print( 6 in g ) # 用关系符检查一下字典中是否有无键值
    g[6] = '55555' # 添加元素
    print(g)

    #   #   更新字典
    h = {}
    h = h.fromkeys((range(5)),'++++')
    j = {666:'---'}
    print(h,j)
    h.update(j) # 更新( 将j字典中的元素加入到h字典中 )
    print(h)
    
    


























    
    
