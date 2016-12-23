# -*- coding: utf-8 -*-
import sys
import operator

file = open(sys.argv[1], 'rw')
topic_word = sys.argv[2]
#file2 = open(sys.argv[2], 'r')
#outputfile = open (sys.argv[3],'w')
#stopwordlist = []
#ignore = 0

#for line in file2.readlines():
#	for token in line.split():
#		stopwordlist.append(token)
topic_dic = {}
for line in file.readlines():
	triple = line.split()
	if(len(triple)==3):
		if (triple[0]!=topic_word):
			if(triple[0] in topic_dic):
				topic_dic[triple[0]]=topic_dic[triple[0]]+int(triple[2])
			else:
				topic_dic[triple[0]]=int(triple[2])
		else:
			if(triple[1] in topic_dic):
				topic_dic[triple[1]]=topic_dic[triple[1]]+int(triple[2])
			else:
				topic_dic[triple[1]]=int(triple[2])

sorted_topic_dic = sorted(topic_dic.items(), key=operator.itemgetter(1))

for x in sorted_topic_dic:
        y = str(x).decode('string_escape')
        print(y)


file.close()

