#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Reverse 00文字列の逆順
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
'''
#Extract 01「パタトクカシーー」
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

#Connect 02「パトカー」＋「タクシー」＝「パタトクカシーー」
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

#Split and Permute 03円周率
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


#Split and Extract and Permute 04元素記号
'''
import re #get re.split
StrA = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
StrB = re.split(r'[,. ]',StrA)
#StrB = StrA.split() a easy to split long string into word.
Number_first_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
Words = {} #get a new dictionary

while '' in StrB: #delete null character string
    StrB.remove('')

for Number,Word in enumerate(StrB, 1): #use enumerate to find every word.
    if Number in Number_first_list:
        Words[Word[0:1]] = Number #push into dictionary
    else:
        Words[Word[0:2]] = Number 
 
print (Words)
'''

# implement n-gram function 05 n-gram
'''
import re #get re.split
def n_gram(sentence,n):
    output_text = []
    for i in range(len(sentence) - 1):
        output_text.append(sentence[i:i+n])

    return output_text

input_text = 'I am an NLPer'
process_text = re.split(r'[,. ]',input_text)
while '' in process_text:
    process_text.remove('')

print (u'this is word bi-gram:')
print (n_gram(input_text,2))
print (u'this is character bi-gram:')
print (n_gram(process_text,2))
'''

# set 06 集合
'''
import re
def n_gram(sentence,n):
    output_text = []
    for i in range(len(sentence) - 1):
        output_text.append(sentence[i:i+n])
    return output_text

input_xtext = 'paraparaparadise'
input_ytext = 'paragraph'

xtext_output = n_gram(input_xtext,2)
ytext_output = n_gram(input_ytext,2)

#get union set 和集合
#union_set  = [i for i in xtext_output if i in ytext_output] other way
union_set = list(set(xtext_output).union(set(ytext_output)))
#get intersection set 積集合
intersection_set = list(set(xtext_output).intersection(set(ytext_output)))
#get difference set 差集合
#difference_set = [i for i in xtext_output if i not in ytext_output] other way
xdifference_set = list(set(xtext_output).difference(ytext_output))
ydifference_set = list(set(ytext_output).difference(xtext_output))
'''

# generate sentence 07 テンプレートによる文生成
'''
def sentence(x,y,z):
   # my_list = [x,y,z]
    return ("「{hour}時の{temperature}は{value}」".format(hour = x,temperature = y,value = z))

x = 12
y = '気温'
z = 22.4

print (sentence(x,y,z))
'''

# English alphabet translates to ASCII and other languages keep same 08 暗号文
def cipher(sentence):
    










