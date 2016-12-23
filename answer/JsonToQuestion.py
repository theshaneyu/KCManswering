import sys
import json
import os
import re

JsonFile = sys.argv[1]

with open(JsonFile, 'r', encoding='utf8') as f1:
    JsonStr = f1.read()

JsonOption = json.loads(JsonStr) #JsonOption is the json string of the questions

path = './QuestionText' # the path of the directory in which we store the question text files
path2 = './QuestionTextJiebaCut'
path3 = './QueryKcmResult'

if not os.path.exists(path):
    try:
        os.makedirs(path)
        print('Directory QuestionText established!')
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

if not os.path.exists(path2):
    try:
        os.makedirs(path2)
        print('Directory QuestionTextJiebaCut established!')
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise

if not os.path.exists(path3):
    try:
        os.makedirs(path3)
        print('Directory QueryKcmResult established!')
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise

for i in range(len(JsonOption)): #len(JsonOption) is the number of the questions
    filename = 'QuestionText_%d'%(i,)
    with open(os.path.join(path, filename), 'w') as TempFile:
        TempFile.write(JsonOption[i]['Question'])




    


