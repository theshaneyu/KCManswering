# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 15:00:01 2016

@author: Shane Yu
"""
import json
import sys
import re
import os
import operator

filename1 = sys.argv[1] #filename1 is 'question.json'
#filename2 = sys.argv[2] #result of querying KCM model

with open(filename1, 'r') as f1:
	JsonStr = f1.read()

JsonOption = json.loads(JsonStr)

#for sorting the filelist numberically
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)


FileList = os.listdir('./QueryKcmResult')
FileList = natural_sort(FileList)
#print(FileList) in ordered checked!

n=0 #for incrementing the options index

for file in FileList:
    with open('./QueryKcmResult/'+file, 'r') as f2:
        print('./QueryKcmResult/'+file+' has been computed')
        KcmStr = f2.read() #KcmStr is the result of querying KCM Model

    #KcmStr's string processing
    KcmStr = KcmStr.replace("(", "")\
    .replace(")", "")\
    .replace("'", "")\
    .replace(",", "")\
    .replace(" ", "")

    KcmStr = re.sub("\d+", "", KcmStr)

    #KcmList is a list of the results from querying KCM model
    KcmList = KcmStr.split('\n')

    times = {'A':"", 'B':"", 'C':""}
    times['A'] = KcmList.count(JsonOption[n]['A'])
    times['B'] = KcmList.count(JsonOption[n]['B'])
    times['C'] = KcmList.count(JsonOption[n]['C'])
    
    #print 'computation result: ', times   <== Cancel the comment to see the result dictionary

    Sorted_Dict = sorted(times.items(), key=operator.itemgetter(1), reverse=True)
    print('===> Question', (n+1), "'s answer is : ",Sorted_Dict[0][0] , "<===")

    n = n + 1

    