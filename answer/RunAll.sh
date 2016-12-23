python JsonToQuestion.py questions.json

LOCATION='./QuestionText' # This directory stores the text files of the questions.
LOCATION2='./QuestionTextJiebaCut' # This directory stores the Jieba cut of the questions.
LOCATION3='./QueryKcmResult' # This directory stores the results from querying KCM model.

# This loop does the Jieba cut for each question's text file in './QuestionText'
n=0
for item in $LOCATION/*
do
    python TermPOSTokenizer.py $item ./QuestionTextJiebaCut/QuestionTextJiebaCut_$n w -Ag -a -ad -an -b -c -Dg -d -e -e -f -g -h -m -o -p -q -r -Tg -u -Vg -v -vd -vn -w -x -y -z
    echo "===> QuestionTextJiebaCut_$n is finished! <==="
    n=$(( n+1 ))	 # increments $n
done


# This loop iterates over the JiebaCut results, with each result we query the KCM model then
# print all the query results from one question(it includes many JiebaCuts) together.
m=0
for item2 in $LOCATION2/*
do
    READFILE=$item2

    while read line || [ -n "$line" ]; do
        grep -w $line Chinese_alltext_clean.model1 >> $line.topic
        python TopicWordAggregator.py $line.topic $line >> ./QueryKcmResult/KcmResult_$m
        echo "$item2 ==> $line has been written into KcmResult_$m"
        rm $line.topic
    done < $READFILE

    m=$(( m+1 ))     # increments $m
done

# AnsGenerator.py calculates the number of the question options' appearences in those
# KCM query results, and the one with the largest number are considered to be the most possible answer.
python AnsGenerator.py questions.json
rm -rf QueryKcmResult QuestionText QuestionTextJiebaCut