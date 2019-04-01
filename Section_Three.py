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

Process_file = Extract_file(u'イギリス')

for line in Process_file.split("\n"):
    reg = re.search(r"^(?P<level>=+)(?P<section>.+?)=",line)
    if reg:
        level = reg.group("level").count("=")-1
        section = reg.group("section")
        print("{0}:{1}".format(level,section))

'''




'''
#extract file 24 ファイル参照の抽出
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
#print(Process_file)
for line in Process_file.split("\n"):
    m = re.search(r"ファイル:(?P<file>.+?)\|",line)
    if m:
        print(m.group("file"))
'''



'''
#extract basic information 25 テンプレートの抽出
import json
import re
def Extract_file(title):
    with open('jawiki-country.json','r') as fp:
        for line in fp:
            temp = json.loads(line)
            if title == temp['title']:
                return temp['text']
    fp.close()


info_dict = {}
Process_file = Extract_file(u'イギリス')
#Get out of all the basic information
m = re.search(r"{{基礎情報[^|]+\|(?P<information>.+?)\n}}", Process_file, re.DOTALL)
if m:
    #print(m.group("information"))
    for line in m.group("information").split("\n|"):
        key,value = re.split(r"\s=\s",line,maxsplit=1)
        info_dict[key] = value

for key,value in info_dict.items():
    print("{key}:{value}".format(key = key,value = value))   


'''
#Remove emphasize font 26 強調マークアップの除去
import json
import re

def Extract_file(title):
    with open('jawiki-country.json','r') as fp:
        for line in fp:
            temp = json.loads(line)
            if title == temp['title']:
                return temp['text']
    fp.close()

def Remove_emphasis(text):
    """強調マークアップを除去"""
    return re.sub(r"'{2,}", "", text)


info_dict = {}
Process_file = Extract_file(u'イギリス')
#Get out of all the basic information
m = re.search(r"{{基礎情報[^|]+\|(?P<information>.+?)\n}}", Process_file, re.DOTALL)
if m:
    #print(m.group("information"))
    for line in m.group("information").split("\n|"):
        key,value = re.split(r"\s=\s",line,maxsplit=1)
        value = Remove_emphasis(value)
        info_dict[key] = value

for key,value in info_dict.items():
    print("{key}:{value}".format(key = key,value = value))
'''
result_dict = {}
for k,v in info_dict.items():
    v = Remove_emphasis(v)
    result_dict[k] = v

for key,value in result_dict.items():
    print("{key}:{value}".format(key = key,value = value))  

'''
