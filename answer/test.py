# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 15:00:01 2016

@author: Shane Yu
"""
import json
import sys
import re

filename1 = sys.argv[1] #選項
filename2 = sys.argv[2] #題目斷詞並搜尋完之後的結果

# Reading data back
with open(filename1, 'r') as f:
    JsonStr = f.read().decode('utf8') #選項

with open(filename2, 'r') as g:
	QuesStr = g.read().decode('utf8') #題目斷詞並搜尋完之後的結果

JsonOption = json.loads(JsonStr)

#print(type(JsonStr))
#print(JsonStr)
#print('==========================')
#print(JsonOption[0]['A'])
#print(type(QuesStr))

#print(QuesStr)
QuesStr = QuesStr.replace("(", "")\
.replace(")", "")\
.replace("'", "")\
.replace(",", "")\
.replace(" ", "")

QuesStr = re.sub("\d+", "", QuesStr)
#print(QuesStr)

QuesList = QuesStr.split('\n') #QuesList是以換行為單位的一的list

#print(QuesList[1])


times = {'A':"", 'B':"", 'C':""}
times['A'] = QuesList.count(JsonOption[0]['A'])
times['B'] = QuesList.count(JsonOption[0]['B'])
times['C'] = QuesList.count(JsonOption[0]['C'])
print(times)

#AnsA = QuesList.count(JsonOption[0]['A'])
#AnsB = QuesList.count(JsonOption[0]['B'])
#AnsC = QuesList.count(JsonOption[0]['C'])

#print(AnsA, AnsB, AnsC)
#print(QuesList[5699])
