import sys

list = [1,2,3,4]
it = iter(list) #   iter()创建一个迭代器
while True:
    try:
        print(next(it),end="") # next(it)输出迭代器下一个元素
    except StopIteration: # StopIteration防止迭代器出现死循环
        sys.exit()
