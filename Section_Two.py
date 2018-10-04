#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-


#第2章: UNIXコマンドの基礎


#count 10 行数のカウント
import sys
import os
import re

data = sys.stdin.read('hightemp.txt')
lines = data.count('\n')

print "%(lines)s" %locals()
