#!/usr/bin/env python3
# -*- coding: utf-8 -*-




#第3章: 正規表現
#read and get json files 20 JSONデータの読み込み
import json

'''
#read json files
with open('jawiki-country.json','r') as fp:
    #put json into dictionary
    for line in fp:
        temp = json.loads(line)
        #search and find goal for title, print
        if temp['title'] == 'イギリス':
            print(temp['text'])
            break
        
fp.close()
'''


'''
#get out of the row of goal 21 カテゴリ名を含む行を抽出
import json
import re

def Extract_file(title):  
    with open('jawiki-country.json','r') as fp:
        for line in fp:
            temp = json.loads(line)
            if title == temp['title']:
                return temp['text']
    fp.close()

Process_file = Extract_file(u"イギリス")

pattern = re.compile(r'\[\[Category')

for line in Process_file.split("\n"):
    #different way to match category
    #if re.search(r"Category:",line):
    if pattern.match(line):
        print (line)
'''


#extract content of category 22. カテゴリ名の抽出
'''
import json
import re

def Extract_file(title):  
    with open('jawiki-country.json','r') as fp:
        for line in fp:
            temp = json.loads(line)
            if title == temp['title']:
                return temp['text']
    fp.close()

Process_file = Extract_file(u"イギリス")
'''
'''
pattern = re.compile(r"\[\[Category:(.*)\]\]")
for line in Process_file.split("\n"):
    lines = pattern.match(line)
    if lines:
        print(lines[1])
'''
'''
for line in Process_file.split("\n"):
    m = re.search(r"Category:(?P<category>.+?)\||]",line)
    if m:
        print(m.group("category"))
'''  



# extract section 23 セクション構造
import json
import re
def Extract_file(title):
    with open('jawiki-country.json','r') as fp:
        for line in fp:
            temp = json.loads(line)
            if title == temp['title']:
                return temp['text']
    fp.close()

Process_file = Extract_file(u'イギリス')

for line in Process_file.split("\n"):
    reg = re.search(r"^(?P<level>=+)(?P<section>.+?)=",line)
    if reg:
        level = reg.group("level").count("=")-1
        section = reg.group("section")
        print("{0}:{1}".format(level,section))
            




