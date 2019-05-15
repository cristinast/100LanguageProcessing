#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Section five 第5章 係り受け解析

import CaboCha
import sys


class Morpheme():
    def __init__(self,surface,base,pos,pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    
    def Output_data(self):
        print('surface[{}]\tbase[{}]\tpos[{}]\tpos1[{}]'.format(self.surface,self.base,self.pos,self.pos1))



def Parse_file():
    with open('neko.txt','r') as fp:
        with open('neko.txt.cabocha','w') as fp1:
            cabocha = CaboCha.Parser()
            for line in fp:
                fp1.write(cabocha.parse(line).toString(CaboCha.FORMAT_LATTICE))


Parse_file()
sentence = []
sentences = []

with open('neko.txt.cabocha','r') as nekocabocha:
    for line in nekocabocha:
        if line == 'EOS\n':
            sentences.append(sentence)
            sentence = []
        elif line[0] == '*':
            continue
        else:
            other = line.split('\t')
            others = other[1].split(',')
            surface = other[0]
            base = others[6]
            pos = others[0]
            pos1 = others[1]
            morpheme = Morpheme(surface,base,pos,pos1)
            sentence.append(morpheme)

for m in sentences:
    print(m)
