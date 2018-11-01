#!/usr/bin/env python3
# -*- coding: utf-8 -*-




#第3章: 正規表現
#read and get json files 20 JSONデータの読み込み
import json


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



#get out of the row of goal 21 カテゴリ名を含む行を抽出
import json

with open('jawiki-country.json','r') as fp:


fp.close()
