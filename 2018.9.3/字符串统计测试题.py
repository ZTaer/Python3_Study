#/usr/bin/python3
#-*-coding:utf-8-*-
import re

#   #   问题统计文字
#   #   核心问题统计文字
#   只检查,数字,字母,空格,其他
#   目前想到的方法,就是用find()方法进行循环来判断
#   生成字母 列: abc = recompile('[a-zA-Z]')
#   生成数字 列: num = recompile(' [0-9] ')
#   以列表的形式返回符合条件的元素findall()
#    然后在以len()测量出元素数量
#   #   多数据导入问题
#   def test( *x ):
#           for i in x:
#               进行测试
def count(*inputstr):
    for i in inputstr:
        def check_num():
            nonlocal i
            pattern = re.compile('[0-9]')
            return len(pattern.findall( i ))

        def check_az():
            nonlocal i
            pattern = re.compile('[a-zA-Z]')
            return len(pattern.findall( i ))

        def check_space():
            nonlocal i
            pattern = re.compile(' ')
            return len(pattern.findall( i ))
        
        other_num = len(i) - check_num() - check_az() - check_space()
        print("数字: ",check_num(),"字母: ",check_az(),"空格: ",check_space(),"其他: ",other_num)

    

if __name__=="__main__":
    count('sadasd234234','sadasd(^&*^')
    
    
    
