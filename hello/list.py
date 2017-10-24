#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
word=['a','b','c','d','e','f','g']

a=word[2]
print "a is: "+a
b=word[1:3]
print "b is: "
print b # 第1，2 对象.
c=word[:2]
print "c is: "
print c # 第0，1 对象.
d=word[0:]
print "d is: "
print d # 全部.
e=word[:2]+word[2:]
print "e is: "
print e # All elements of word.
f=word[-1]
print "f is: "
print f # 最后一个.
g=word[-4:-2]
print "g is: "
print g # index 3 and 4 elements of word.
h=word[-2:]
print "h is: "
print h # The last two elements.
i=word[:-2]
print "i is: "
print i # Everything except the last two characters
l=len(word)
print "Length of word is: "+ str(l)
print "Adds new element"
word.append('h')
print word

#enumerate 将list  转换成 下标 值 键值对
ls=list(range(1, 11))
for i,value in enumerate(ls):
    print str(i)+":"+str(value)