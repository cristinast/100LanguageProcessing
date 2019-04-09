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



'''
#Remove emphasize font 26 強調マークアップの除去 first way isn't using a function to save
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
    #re.sub(r"1","2",text) find 1 in text and use to 2 to change
    return re.sub(r"'{2,}", "", text)


info_dict = {}
Process_file = Extract_file(u'イギリス')
#Get out of all the basic information
m = re.search(r"{{基礎情報[^|]+\|(?P<information>.+?)\n}}", Process_file, re.DOTALL)
if m:
    #print(m.group("information"))
    for line in m.group("information").split("\n|"):
        #cut and remove,save space
        key,value = re.split(r"\s=\s",line,maxsplit=1)
        value = Remove_emphasis(value)
        info_dict[key] = value

for key,value in info_dict.items():
    print("{key}:{value}".format(key = key,value = value))

'''


'''
#Remove emphasize font 26 強調マークアップの除去 second way which uses a function to save
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
    return re.sub(r"'{2,}", "", text)


def Process_text(text):
    info_dict = {}
    m = re.search(r"{{基礎情報[^|]+\|(?P<information>.+?)\n}}", text,re.DOTALL) 
    if m:
        for line in m.group("information").split("\n|"):
            key,value = re.split(r"\s=\s",line,maxsplit = 1)
            info_dict[key] = value
    return info_dict



Get_text = Extract_file(u'イギリス')

Base_info = Process_text(Get_text)

Result_info = {}

for key,value in Base_info.items():
    value = Remove_emphasis(value)
    Result_info[key] = value
    print("{key}:{value}".format(key = key,value = value)


'''


'''
#Remove link of text 27 内部リンクの除去
import json
import re

def Extract_file(title):
    with open('jawiki-country.json','r') as fp:
        for line in fp:
            temp = json.loads(line)
            if title == temp['title']:
                return temp['text']
    fp.close()

def Process_text(text):
    info_dict = {}
    m = re.search(r"{{基礎情報[^|]+\|(?P<information>.+?)\n}}", text,re.DOTALL) 
    if m:
        for line in m.group("information").split("\n|"):
            key,value = re.split(r"\s=\s",line,maxsplit = 1)
            info_dict[key] = value
    return info_dict


def Remove_emphasis(text):
    return re.sub(r"'{2,}", "", text)

def Remove_internal_links(text):
     return re.sub(r"\[\[([^]]+)\]\]", lambda m: m.group(1).split("|")[-1], text)


Get_text = Extract_file(u'イギリス')

Base_info = Process_text(Get_text)

Result_info = {}

for key,value in Base_info.items():
    value = Remove_emphasis(value)
    value = Remove_internal_links(value)
    Result_info[key] = value
    print("{key}:{value}".format(key = key,value = value))
'''


'''
#Remaove mediawiki markup 28 MediaWikiマークアップの除去
import json
import re

def Extract_file(title):
    with open('jawiki-country.json','r') as fp:
        for line in fp:
            temp = json.loads(line)
            if title == temp['title']:
                return temp['text']
    fp.close()


def Process_file(text):
    info_dict = {}
    m = re.search(r'{{基礎情報[^|]+\|(?P<information>.+?)\n}}',text,re.DOTALL)
    if m:
        for line in m.group("information").split("\n|"):
            key,value = re.split(r"\s=\s",line,maxsplit = 1)
            info_dict[key] = value
    return info_dict


def Remove_category_links(text):
    return re.sub(r"\[\[Category:(.+?)\]\]", lambda m:m.group(1).split("|")[0],text)

def Remove_emphasis(text):
    return re.sub(r"'{2,}","",text)

def Remove_internal_links(text):
    return re.sub(r"\[\[([^]]+)\]\]", lambda m: m.group(1).split("|")[-1], text)

def Remove_external_links(text):
    return re.sub(r"\[([^]]+)\]", lambda m:m.group(1).split(" ")[-1],text)

def Remove_template(text):
    return re.sub(r"\{\{(.+?)\}\}", lambda m:m.group(1).split("|")[-1],text)

def Remove_redirect(text):
    return re.sub(r"#REDIRECT \[\[(.+?)\]\]", lambda m:m.group(1),text)

def Remove_unordered_list(text):
    return re.sub(r"^\*+\s*","",text,flags = re.MULTILINE)

def Remove_ordered_list(text):
    return re.sub(r"^#+\s*","",text,flags = re.MULTILINE)

def Remove_define_list(text):
    return re.sub(r"^(:|;)\s","",text,flags = re.MULTILINE)

def Remove_html_mark(text):
    return re.sub(r"<\/?[br|ref][^>]*?>","",text,flags = re.MULTILINE)

def Remove_comment(text):
    return re.sub(r"<!--.*?-->","",text)




Get_text = Extract_file(u'イギリス')


Base_info = Process_file(Get_text)

Result_info = {}

for key,value in Base_info.items():
    value = Remove_category_links(value)
    value = Remove_emphasis(value)
    value = Remove_internal_links(value)
    value = Remove_external_links(value)
    value = Remove_template(value)
    value = Remove_redirect(value)
    value = Remove_unordered_list(value)
    value = Remove_ordered_list(value)
    value = Remove_define_list(value)
    value = Remove_html_mark(value)
    value = Remove_comment(value)
    Result_info[key] = value
    print("('{key}' : '{value}')".format(key = key,value = value))

'''
#Get the picture of country flag 29 国旗画像のURLを取得する
import json
import re
from urllib.parse import urlencode
from urllib import request
import codecs

def Extract_file(title):
    with open('jawiki-country.json','r') as fp:
        for line in fp:
            temp = json.loads(line)
            if title == temp['title']:
                return temp['text']
    fp.close()


def Process_file(text):
    info_dict = {}
    m = re.search(r'{{基礎情報[^|]+\|(?P<information>.+?)\n}}',text,re.DOTALL)
    if m:
        for line in m.group("information").split("\n|"):
            key,value = re.split(r"\s=\s",line,maxsplit = 1)
            info_dict[key] = value
    return info_dict


def Remove_category_links(text):
    return re.sub(r"\[\[Category:(.+?)\]\]", lambda m:m.group(1).split("|")[0],text)

def Remove_emphasis(text):
    return re.sub(r"'{2,}","",text)

def Remove_internal_links(text):
    return re.sub(r"\[\[([^]]+)\]\]", lambda m: m.group(1).split("|")[-1], text)

def Remove_external_links(text):
    return re.sub(r"\[([^]]+)\]", lambda m:m.group(1).split(" ")[-1],text)

def Remove_template(text):
    return re.sub(r"\{\{(.+?)\}\}", lambda m:m.group(1).split("|")[-1],text)

def Remove_redirect(text):
    return re.sub(r"#REDIRECT \[\[(.+?)\]\]", lambda m:m.group(1),text)

def Remove_unordered_list(text):
    return re.sub(r"^\*+\s*","",text,flags = re.MULTILINE)

def Remove_ordered_list(text):
    return re.sub(r"^#+\s*","",text,flags = re.MULTILINE)

def Remove_define_list(text):
    return re.sub(r"^(:|;)\s","",text,flags = re.MULTILINE)

def Remove_html_mark(text):
    return re.sub(r"<\/?[br|ref][^>]*?>","",text,flags = re.MULTILINE)

def Remove_comment(text):
    return re.sub(r"<!--.*?-->","",text)

def Get_image(name):
    

    return flag_image_url



Get_text = Extract_file(u'イギリス')


Base_info = Process_file(Get_text)

Flag_image_name = Base_info["国旗画像"]
#print(Flag_image_name)

query = urlencode({
        "action":"query",
        "titles":"File:{0}".format(Flag_image_name),
        "format":"json",
        "prop":"imageinfo",
        "iiprop":"url", 
    })

#print(query)
url = "https://commons.wikimedia.org/w/api.php?{0}".format(query)
#print(url)
    
with request.urlopen(url) as response:
    body = response.read()
    data = json.loads(body.decode())
    #print(data)
    
flag_image_url = list(data["query"]["pages"].values())[0]["imageinfo"][0]["url"]

print(flag_image_url)

Result_info = {}

for key,value in Base_info.items():
    value = Remove_category_links(value)
    value = Remove_emphasis(value)
    value = Remove_internal_links(value)
    value = Remove_external_links(value)
    value = Remove_template(value)
    value = Remove_redirect(value)
    value = Remove_unordered_list(value)
    value = Remove_ordered_list(value)
    value = Remove_define_list(value)
    value = Remove_html_mark(value)
    value = Remove_comment(value)
    Result_info[key] = value
    print("('{key}' : '{value}')".format(key = key,value = value))





