#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# 类似map

d={'a':1,'b':2}
print d['b']

#设置
d['Adam'] = 67
print d['Adam']
#循环  结果无序
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key
    print  d[key]
# value 迭代
for value in d.values():
    print value
# key value 迭代
for k,v in d.items():
    print k+":"+str(v)
