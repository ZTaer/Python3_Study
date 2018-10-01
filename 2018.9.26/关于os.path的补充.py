import os
#   #   判断路径
os.path.exists('E://test.txt') #    判断文件/目录是否存在
os.path.isabs() #   判断是否是绝对路径
os.path.isdir() #   判断是否存在目录
os.path.isfile() #  判断文件是否存在
os.path.islink() #  判断是否是一个符号链接
os.path.ismount() # 判断是否是挂载点( 硬盘分区 )
os.paht.samefile('路径1','路径2') # 判断2个路径是否指定的是一个文件
