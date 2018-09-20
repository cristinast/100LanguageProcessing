#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

#Index method
'''
strA = "ahiuewihkdnlsdjih"
strA[::-1]
'''

#Group list method
strA = raw_input("Please enter string which need to reverse.")
order = []
for i in strA:
    order.append(i)
order.reverse() #reverse list
print ''.join(order) #change list into string. not support python2.7


