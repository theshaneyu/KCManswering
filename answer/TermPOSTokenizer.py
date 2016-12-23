# -*- coding: utf-8 -*-
"""
Created on Mon May 16 20:38:53 2016

@author: user
"""

import jieba
import jieba.posseg as pseg
import sys
#jieba.set_dictionary('dict.txt.big.txt')
jieba.load_userdict('dict.txt.big.txt')
filename=sys.argv[1]
output = sys.argv[2]
mission = sys.argv[3]

f = open(filename,'r', encoding='utf8')
f2 =open(output,'a', encoding='utf8')


if mission=='t':
    for sentence in f.readlines():
        if sentence!='\n':
            words = pseg.cut(sentence)
            for word,flag  in words:
                if word!='\n':
                    if sys.argv[4][0]!='+'and'-'+str(flag)[0] not in sys.argv and '-'+str(flag) not in sys.argv:
                        f2.write("\n"+word+" "+flag)
                    elif '+'+str(flag)[0] in sys.argv :
                        f2.write("\n"+word+" "+flag)                            
                else:
                    f2.write('\n')
        else:
            f2.write("\n")

elif mission=='w'and len(sys.argv)>4:
    for sentence in f.readlines():
        if sentence!='\n':
            words = pseg.cut(sentence)
            for word,flag  in words:
                if word!='\n':
                    if sys.argv[4][0]!='+'and'-'+str(flag)[0] not in sys.argv and '-'+str(flag) not in sys.argv:
                        f2.write("\n"+word)
                    elif '+'+str(flag)[0] in sys.argv :
                        f2.write("\n"+word)        
                else:
                    f2.write('\n')
        else:
            f2.write("\n")


elif mission=='w'and len(sys.argv)==4:    
    for sentence in f.readlines():
        if sentence!='\n':
            words = jieba.cut(sentence, cut_all=False)
            for word in words:
                if word!='\n':
                    f2.write("\n"+word)
                else:
                    f2.write('\n')

        else:
            f2.write("\n")

f.close()
f2.close()

#for deleting the first blank line
with open(output, 'r', encoding='utf8') as fin:
    data = fin.read().splitlines(True)
with open(output, 'w', encoding='utf8') as fout:
    fout.writelines(data[1:])



