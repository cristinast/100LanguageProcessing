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
        
    

Parse_text()
sectence  = []
sectences  = []
with open('neko.txt.mecab','r') as nekomecab:
    for morpheme in nekomecab.read().split('\n'):
        surface = morpheme.split('\t')
        if len(surface) == 2:
            result = surface[1].split(',')
            word = {
                'surface' : surface[0],
                'base' : result[6],
                'pos' : result[0],
                'pos1': result[1]
            }
            sentence.append(word)
            if word['pos1'] == '句点':
                sentences.append(sentence)
                sentence = []
            elif len(surface) == 1:
                pass
            else: RuntimeError


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
        
    


Parse_file()
sentence  = []
sentences = []

with open('neko.txt.mecab','r') as nekomecab:
    for morpheme in nekomecab.read().split('\n'):
        surface = morpheme.split('\t')
        if len(surface) == 2:
            result = surface[1].split(',')
            word = {
                'surface' : surface[0],
                'base' : result[6],
                'pos' : result[0],
                'pos1': result[1]
            }
            sentence.append(word)
            if word['pos1'] == '句点':
                sentences.append(sentence)
                sentence = []
            elif len(surface) == 1:
                pass
            else: RuntimeError


result = []

for sentence in sentences:
    for morpheme in sentence:
        if morpheme['pos'] == '動詞':
            result.append(morpheme['surface'])
            #print (result)


for m in result:
    print(m)
'''

'''
#Extract Verb prototype 32 動詞の原形

import MeCab
import sys

def Parse_text():
    with open('neko.txt','r') as fp:
        with open('neko.txt.mecab','w') as result:
            mecab = MeCab.Tagger()
            result.write(mecab.parse(fp.read()))
        
    


Parse_text()
sentence = []
sentences = []


with open('neko.txt.mecab','r') as nekomecab:
    for morpheme in nekomecab.read().split('\n'):
        surface = morpheme.split('\t')
        if len(surface) == 2:
            result = surface[1].split(',')
            word = {
                'surface' : surface[0],
                'base' : result[6],
                'pos' : result[0],
                'pos1': result[1]
            }
            sentence.append(word)
            if word['pos1'] == '句点':
                sentences.append(sentence)
                sentence = []
            elif len(surface) == 1:
                pass
            else: RuntimeError



result = []

for sentence in sentences:
    for morpheme in sentence:
        if(morpheme['pos'] == '動詞'):
            result.append(morpheme['base'])

#for m in result:
  #  print(m) 
'''

'''
# Extract noun 33 サ変名詞
import MeCab
import sys


def Parse_file():
    with open('neko.txt','r') as fp:
        with open('neko.txt.mecab','w') as fp1:
            mecab = MeCab.Tagger()
            fp1.write(mecab.parse(fp.read()))
        
    

Parse_file()
sentence = []
sentences = []

with open('neko.txt.mecab','r') as nekomecab:
    for morpheme in nekomecab.read().split('\n'):
        surface = morpheme.split('\t')
        if len(surface) == 2:
            result = surface[1].split(',')
            word = {
                'surface' : surface[0],
                'base' : result[6],
                'pos' : result[0],
                'pos1': result[1]
            }
            sentence.append(word)
            if word['pos1'] == '句点':
                sentences.append(sentence)
                sentence = []
            elif len(surface) == 1:
                pass
            else: RuntimeError




result = []

for sentence in sentences:
    for morpheme in sentence:
        if morpheme['base'] != '*':
            if morpheme['pos'] == '名詞' and morpheme['pos1'] == 'サ変接続':
                result.append(morpheme['base'])

for m in result:
    print(m)
'''

'''
#Extract noun and noun with の 34「AのB」
import MeCab
import sys



def Parse_file():
    with open('neko.txt','r') as fp:
        with open('neko.txt.mecab','w') as fp1:
            mecab = MeCab.Tagger()
            fp1.write(mecab.parse(fp.read()))



Parse_file()
sentence  = []
sentences = []

with open('neko.txt.mecab','r') as nekomecab:
    for morpheme in nekomecab.read().split('\n'):
        surface = morpheme.split('\t')
        if len(surface) == 2:
            result = surface[1].split(',')
            word = {
                'surface': surface[0],
                'base': result[6],
                'pos': result[0],
                'pos1': result[1]
            }
            sentence.append(word)
            if word['pos1'] == '句点':
                sentences.append(sentence)
                sentence = []
            elif len(surface) == 1:
                pass
            else:
                RuntimeError



#print(sentences)


result = []


for sentence in sentences:
    for num in range(len(sentence)):
        if sentence[num]['surface'] == 'の' and sentence[num-1]['pos'] == '名詞' and sentence[num+1]['pos'] == '名詞':
            result.append(sentence[num-1]['surface']+'の'+sentence[num+1]['surface'])
        

for m in result:
    print(m)
'''

'''
#Extract the longest of noun 35 名詞の連接
import MeCab
import sys


def Parse_file():
    with open('neko.txt','r') as fp:
        with open('neko.txt.mecab','w') as fp1:
            mecab = MeCab.Tagger()
            fp1.write(mecab.parse(fp.read()))



Parse_file()
sentence  = []
sentences = []

with open('neko.txt.mecab','r') as nekomecab:
    for morpheme in nekomecab.read().split('\n'):
        surface = morpheme.split('\t')
        if len(surface) == 2:
            result = surface[1].split(',')
            word = {
                'surface': surface[0],
                'base': result[6],
                'pos': result[0],
                'pos1': result[1]
            }
            sentence.append(word)
            if word['pos1'] == '句点':
                sentences.append(sentence)
                sentence = []
            elif len(surface) == 1:
                pass
            else:
                RuntimeError



result = []

for sentence in sentences:
    noun = []
    for morpheme in sentence:
        if morpheme['pos'] == '名詞':
            noun.append(morpheme['surface'])
        else:
            if len(noun) > 1:
                result.append(''.join(noun))
            noun = []
    
    if len(noun) > 1:
        result.append(''.join(noun))
    noun = []
        
for m in result:
    print(m)  
'''


'''
#Get the frequency of a word 単語の出現頻度

import MeCab
import sys
import collections


def Parse_file():
    with open('neko.txt','r') as fp:
        with open('neko.txt.mecab','w') as fp1:
            mecab = MeCab.Tagger()
            fp1.write(mecab.parse(fp.read()))


Parse_file()
sentence  = []
sentences = []



with open('neko.txt.mecab','r') as nekomecab:
    for morpheme in nekomecab.read().split('\n'):
        surface = morpheme.split('\t')
        if len(surface) == 2:
            result = surface[1].split(',')
            word = {
                'surface': surface[0],
                'base': result[6],
                'pos': result[0],
                'pos1': result[1]
            }
            sentence.append(word)
            if word['pos1'] == '句点':
                sentences.append(sentence)
                sentence = []
        elif len(surface) == 1:
            pass
        else:
            RuntimeError



word_counter = collections.Counter()

for sentence in sentences:
    word_counter.update([morpheme['surface'] for morpheme in sentence])


result = word_counter.most_common()

print(result)
'''


'''
#Get the top 10 frequency of word 37 頻度上位10語
import MeCab
import sys
import collections
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def Parse_file():
    with open('neko.txt','r') as fp:
        with open('neko.txt.mecab','w') as fp1:
            mecab = MeCab.Tagger()
            fp1.write(mecab.parse(fp.read()))




Parse_file()
sentence = []
sentences = []


with open('neko.txt.mecab','r') as nekomecab:
    for morpheme in nekomecab.read().split('\n'):
        surface = morpheme.split('\t')
        if len(surface) == 2:
            result = surface[1].split(',')
            word = {
                'surface': surface[0],
                'base': result[6],
                'pos': result[0],
                'pos1': result[1]
            }
            sentence.append(word)
            if word['pos1'] == '句点':
                sentences.append(sentence)
                sentence = []
        elif len(surface) == 1:
            pass
        else:
            RuntimeError


word_counter = collections.Counter()

for sentence in sentences:
    word_counter.update(morpheme['surface'] for morpheme in sentence)

Top_word = list(zip(*word_counter.most_common(10)))
Word_name = Top_word[0]
Word_number = Top_word[1]


#get the picture

fp = FontProperties(fname='/System/Library/Fonts/ヒラギノ明朝 ProN.ttc')
plt.bar(range(0,10),Word_number,align='center',color = '#E58E9C')
plt.xticks(range(0,10),Word_name,FontProperties = fp)
plt.xlim(xmin = -1,xmax = 10)
plt.title('頻度上位10語',FontProperties = fp)
plt.xlabel('単語',FontProperties = fp)
plt.ylabel('出現頻度',FontProperties = fp)
plt.grid(axis='y')
plt.show()

'''



#Get histogram picture 38 ヒストグラム


        

            
        


