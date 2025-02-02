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
sentence  = []
sentences  = []
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


for line in sentences:
    print(line)

#print(sentences)
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

'''
#Get histogram picture 38 ヒストグラム
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
                'surface' : surface[0],
                'base' : result[6],
                'pos' : result[0],
                'pos1' : result[1]
            }
            sentence.append(word)
            if word['pos1'] == '句点':
                sentences.append(sentence)
                sentence = []
        elif len(surface) == 1:
            pass    
        else:
            RuntimeError

#count word
word_counter = collections.Counter()
for sentence in sentences:
    word_counter.update(morpheme['surface'] for morpheme in sentence)


list_word = list(zip(*word_counter.most_common()))
Word_number = list_word[1]

#font for the picture. NO Garbled  
fp = FontProperties(fname='/System/Library/Fonts/ヒラギノ明朝 ProN.ttc')
#decide which range to do
plt.hist(Word_number,bins = 30,range=(1,30),color = '#E58E9C')

#remove 0 data
plt.xlim(xmin = 1,xmax = 10)
#label 
plt.title('ヒストグラム',FontProperties = fp)
plt.xlabel('出現頻度',FontProperties = fp)
plt.ylabel('単語の種類数',FontProperties = fp)
#get x gridding if axis = 'x' it will get y gridding. 
#if we don't write it, it will get x+y by itself.
plt.grid(axis='y')
#show the picture
plt.show()

'''
#Rule of Zipf 39 Zipfの法則
import sys
import MeCab
import collections
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def Parse_file(filename):
    with open(filename,'r') as fp:
        with open('neko.txt.mecab','w') as fp1:
            mecab = MeCab.Tagger()
            fp1.write(mecab.parse(fp.read()))

def Map_Mecab(MecabFilename):
    sentence = []
    sentences = []
    with open(MecabFilename,'r') as nekomecab:
        for morpheme in nekomecab.read().split('\n'):
            surface = morpheme.split('\t')
            if len(surface) == 2:
                result = surface[1].split(',')
                word = {
                    'surface' : surface[0],
                    'base' : result[6],
                    'pos' : result[0],
                    'pos1' : result[1]
                }
                sentence.append(word)
                if word['pos1'] == '句点':
                    sentences.append(sentence)
                    sentence = []
            elif len(surface) == 1:
                pass
            else:
                RuntimeError
    return sentences

analysisfile = Parse_file('neko.txt')
Sentences = Map_Mecab('neko.txt.mecab')

word_counter = collections.Counter()
for sentence in Sentences:
    word_counter.update(morpheme['surface'] for morpheme in sentence)

list_word = list(zip(*word_counter.most_common()))
#Word_name = list_word[0]
#Word_number = list_word[1]

fp =  FontProperties(fname='/System/Library/Fonts/ヒラギノ明朝 ProN.ttc')
#plt.scatter(range(1,len(Word_number)+1),Word_number)
plt.scatter(range(len(list_word[1])),list_word[1],color = '#E58E9C')

#plt.xlim(1,len(Word_name)+1)
#plt.ylim(1,Word_name)
#decide range of x coordinate axis
plt.xlim(1,len(list_word[0]))
#decide range of y coordinate axis
plt.ylim(1,list_word[1][0])

#logarithmetics
plt.xscale('log')
plt.yscale('log')

plt.title('Zipfの法則',FontProperties = fp)
plt.xlabel('出現頻度順位',FontProperties = fp)
plt.ylabel('出現頻度',FontProperties = fp)



plt.grid(axis= 'y')
plt.show()