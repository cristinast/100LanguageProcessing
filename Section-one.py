#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Reverse 文字列の逆順
#Index method
'''
strA = "ahiuewihkdnlsdjih"
strA[::-1]
'''

'''
#Group list method
strA = raw_input("Please enter string which need to reverse.")
order = []
for i in strA:
    order.append(i)
order.reverse() #reverse list
print ''.join(order) #change list into string. not support python2.7

#Extract 「パタトクカシーー」
'''
'''
StrA = 'パタトクカシーー'

print (StrA[1])
print (StrA[3])
print (StrA[5])
print (StrA[7])

StrB =''
StrB += StrA[1]
StrB += StrA[3]
StrB += StrA[5]
StrB += StrA[7]
print (StrB)
'''

#Connect 「パトカー」＋「タクシー」＝「パタトクカシーー」
'''
StrA = 'パトカー'
StrB = 'タクシー'
StrC = ''
if len(StrA) == len(StrB):
    for j in range(len(StrA)) and range(len(StrB)):
        StrC += StrA[j] + StrB[j]
elif len(StrA) > len(StrB):
     for j in range(len(StrA)):
        StrC += StrA[j] + StrB[j]
elif len(StrA) < len(StrB):
    for j in range(len(StrB)):
        StrC += StrA[j] + StrB[j]
print (StrC) 
'''

#Permute and Combine 円周率
'''
import re #get re.split
StrA = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
StrB = re.split(r'[, .]',StrA)
while '' in StrB: #delete null character string
    StrB.remove('')
StrC = sorted(StrB, key=str.lower) # sort by alphabet
#sorted(StrB, key = str.lower)
#StrB.sort()
print (StrC)
'''


