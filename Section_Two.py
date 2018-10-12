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
#another solution, under consideration
'''
import os
fp = open('hightemp.txt','r')
input_list = fp.readlines()
replace_list = []
push11 = []
#print (input_list)
for line in input_list:
    process_list = line.replace('\t',' ')
    replace_list.append(process_list)
#print (replace_list)

print(push11)

with open('clo11.txt','w') as col11_file:
    for col11 in replace_list:
        col11_file.write(col11)
        col11_file.write('\n')

fp.close()
'''

#gather 13 col1.txtとcol2.txtをマージ
#implement it according to my idea. so complex.
''' 
import os
#import flatten #need to verify

fp1 = open('col1.txt','r')
fp2 = open('col2.txt','r')

list1 = []
list2 = []
list12 = []
i = 0
j = 0

line1 = fp1.readline()
line1 = line1.replace('\n','\t')
line2 = fp2.readline()

while line1:
    list1.append(line1)
    line1 = fp1.readline()
    line1 = line1.replace('\n','\t')

while line2:
    list2.append(line2)
    line2 = fp2.readline()

#list12 = zip(list1,list2)
#for i,j in zip(list1,list2):
 #   list12.append(zip(list1,list2))

while i < len(list1) and j < len(list2): #merge into a list
    list12.append(list1[i])
    list12.append(list2[j])
    i += 1
    j += 1

print(list12)
with open('col12.txt','w') as col12_file:
    for col12 in list12:
        col12_file.write(col12)
 
fp1.close()
fp2.close()
'''

#other way by Internet.
'''
import os
fp1 = open('col1.txt','r')
fp2 = open('col2.txt','r')

with open('col12.txt','w') as col12_file:
    for fp1_line,fp2_line in zip(fp1,fp2): #use function python [zip] to merge
        col12_file.write(fp1_line.rstrip()+'\t'+fp2_line.rstrip()+'\n')
'''




#head print 14 先頭からN行を出力

