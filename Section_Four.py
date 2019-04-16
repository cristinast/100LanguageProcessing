#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#before you start this section, you need to make sure MeCab in your laptop. 
# so u need to install it and configure it in your laptop

# Read Morphological Analysis result 30 形態素解析結果の読み込み
'''
import MeCab
import sys
#mecab = MeCab.Tagger('-Owakati') #-Ochasen
#print(mecab.parse("今日はいい天気ですね。"))

def Parse_text():
    with open('neko.txt','r') as fp:
        with open('neko.txt.mecab','w') as result:
            mecab = MeCab.Tagger()
            result.write(mecab.parse(fp.read()))
        result.close()
    fp.close()

Parse_text()
sectence  = []
sectences  = []
with open('neko.txt.mecab','r') as nekomecab:
    for morpheme in nekomecab.readlines():
        #print(morpheme)
        #cut result by tap
        surface = morpheme.split('\t')
        #there is only tap in this line
        if len(surface) >= 2:
            #use , to change
            result = surface[1].split(',')
            word = {
                'surface' : surface[0],#kinds of word
                'base' : result[6],#prototype
                'pos' : result[0],
                'pos1' : result[1]
            } 
            sectence.append(word)
            
            # is this sentence finshed
            if(word['pos1'] == '句点'):# or word['pos1'] == '空白':
                sectences.append(sectence)
                sectence = []
nekomecab.close()

for line in sectences:
    print(line)

#print(sectences)
'''

'''

#Extract verb  31 動詞
import MeCab
import sys

def Parse_file():
    with open('neko.txt','r') as fp:
        with open ('neko.txt.mecab','w') as result:
            mecab = MeCab.Tagger()
            result.write(mecab.parse(fp.read()))
        result.close()
    fp.close()


Parse_file()
sentence  = []
sentences = []

with open('neko.txt.mecab','r') as nekomecab:
    for morpheme in nekomecab.readlines():
        surface = morpheme.split('\t')
        if len(surface) >= 2:
            result = surface[1].split(',')
            word = {
                'surface': surface[0],
                'base': result[6],
                'pos': result[0],
                'pos1': result[1]
            }
            sentence.append(word)
            if (word['pos1'] == '句点'):
                sentences.append(sentence)
                sentence = []
nekomecab.close()

result = []

for sentence in sentences:
    for morpheme in sentence:
        if morpheme['pos'] == '動詞':
            result.append(morpheme['surface'])
            #print (result)


for m in result:
    print(m)
'''

#Extract Verb prototype 32 動詞の原形

