#/usr/bin/python3
# -*- coding:utf-8 -*-

#  十进制转换成二进制转换
# 分析
# 255/2 = 127
# 255%2= 1
# 127/2 = 63
# 127 %2 =1
# 由此循环

# 核心
# print('a'+'b')
# 'ab'
def binn( numint ):
    listbin = []
    endbin = '0b'
    nagative = False
    if numint < 0:
        nagative = True
    while True:
        end = int(numint / 2) # 整数除法 无语.....9 // 2 = 4 ; -9 // 2 = -5
        r = numint % 2
        listbin.append(str(r))
        numint = end
        if numint == 0:
            for i in list(reversed(listbin)):
                endbin +=i
            if nagative:
                return '-'+endbin
            else:
                return endbin
            break

if __name__ == "__main__":
    print(bin(84))
    print(binn(84))
