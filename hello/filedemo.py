# -*- coding: UTF-8 -*-
# r，以只读方式打开文件
# w，打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a，打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# w+，打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。

file_obj = file("/Users/linyuanjing/myproject/python-learn/hello/test.properties","a")
file_obj.write('内容2')
file_obj.close()


file1=open("/Users/linyuanjing/myproject/python-learn/hello/test.properties","r")
file=file("/Users/linyuanjing/myproject/python-learn/hello/test.properties","r")
try:
    all_the_text = file.read()
finally:
    file.close()
print all_the_text
