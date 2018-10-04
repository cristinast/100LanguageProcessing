#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#第2章: UNIXコマンドの基礎


#count 10 行数のカウント

#just use to count small file
#count = len(open('hightemp.txt','rU').readlines()) 

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
fp = open('hightemp.txt') #open files
while True:
    buffer = fp.read(1024*8192)
    if not buffer:
        break
    count += buffer.count('\n')
fp.close()
'''

#print (count)


#replace blank 11 タブをスペースに置換
