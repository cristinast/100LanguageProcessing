#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#第2章: UNIXコマンドの基礎


#count 10 行数のカウント

#just use to count small file
'''
count = len(open('hightemp.txt','rU').readlines()) 
'''

# for big file,use circulation to count numbers of line
'''
count  = -1
for count,line in enumerate(open(r'hightemp.txt','rU')):
    pass
count += 1 
'''

#the best way,use carriage return to count numbers of line.
'''
count = 0
fp = open('hightemp.txt','r') #open files
while True:
    buffer = fp.read(1024*8192)
    if not buffer:
        break
    count += buffer.count('\n')
fp.close()
'''

# read next line and count line to get result.
'''
fp = open('hightemp.txt','r')

count = 0
line = fp.readline()
while line:
    line = fp.readline()
    count += 1;

fp.close()
'''
#print (count)


#replace blank 11 タブをスペースに置換
'''
import os
fp = open('hightemp.txt','r') #open files

for line in fp:
    str = line.replace('\t',' ').rstrip() #replace symbol form
    print (str)

fp.close()
'''

#save file 12 1列目をcol1.txtに，2列目をcol2.txtに保存
'''
import os

first_row = []
second_row = []
fp = open('hightemp.txt','r')
line = fp.readline()
while line:
    #print (line)
    split_files = line.split('\t')
    #print(split_files)
   
    first_row.append(split_files[0])
    

    second_row.append(split_files[1])
    line = fp.readline()

#print (first_row)
with open('col1.txt','w') as col1_file:
    for col1 in first_row:
        col1_file.write(col1)
        col1_file.write('\n')

with open('col2.txt','w') as col2_file:
    for col2 in second_row:
        col2_file.write(col2)
        col2_file.write('\n')
fp.close()


fp1 = open('col1.txt','r')
file1 = fp1.read()
print (file1)
fp1.close()

fp2 = open('col2.txt','r')
file2 = fp2.read()
print (file2)
fp2.close()
'''


#gather 13 col1.txtとcol2.txtをマージ