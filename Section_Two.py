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




#from head print 14 先頭からN行を出力
'''
import os
input_number = int(input('please input you want to print row: '))
fp1 = open('hightemp.txt','r')
count = len(fp1.readlines())
fp1.close()
with open('hightemp.txt','r') as fp:
    if input_number > count:
        print ('outfiles')
    else:
        line = fp.readline().rstrip()
        print (line)
        input_number -=1
        while input_number > 0:
            line = fp.readline().rstrip()
            input_number -=1
            print(line)
fp.close()
'''



#from tail print 15 末尾のN行を出力
'''
import os
list_txt = []
input_number = int(input('please input you want to print row: '))
fp = open('hightemp.txt','r')
count = len(fp.readlines())
fp.close()
fp1 = open('hightemp.txt','r')
line = fp1.readlines()
if input_number > count:
    print ('outfiles')
else:
    input_number = count - input_number
    print(input_number)
    while input_number != count:
        list_txt.append(line[input_number])
        input_number += 1
for inform in list_txt:
    print(inform.rstrip())
#print(list_txt)
fp1.close()
'''



#from middle print 16 ファイルをN分割する
'''
import os
import math

fp = open('hightemp.txt','r')
count = len(fp.readlines())
fp.close()
input_number = int(input('please enter you want to split row: '))
fp1 = open('hightemp.txt','r')
line1 = fp1.readlines()
fp1.close()
if input_number > count:
    print('outfiles')
else:
    print_number = math.ceil(count / input_number) #Rounded rounded by element
    for i,file_txt in enumerate(range(0,count,print_number),1):
        for line in line1[file_txt:file_txt + print_number]:#print from middle.
            print(line.rstrip())
        print('\n')
'''


# delete duplicate values 17 １列目の文字列の異なり
'''
import os
first_row = []
fp = open('hightemp.txt','r')
line = fp.readline()
while line:
    split_files = line.split('\t')
    first_row.append(split_files[0])
    line = fp.readline()
fp.close()
#print(first_row)

result_list = list(set(first_row))#delete duplicate values

print(result_list)
'''


#sort 18 各行を3コラム目の数値の降順にソート
'''
import os
third_row = []
file_list = []


fp = open('hightemp.txt','r')
line = fp.readline()
while line:
    file_list.append(line)
    line = fp.readline()
#print(file_list)
for files in file_list:
    files = files.split('\t')
    #print(files[2])
    file_list = sorted(file_list,key = lambda file: float(files[2]),reverse = True)   

for lines in file_list:
    print(lines.rstrip())
fp.close()
'''

# 19 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
