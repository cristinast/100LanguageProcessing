#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Extract
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

#Connect
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

