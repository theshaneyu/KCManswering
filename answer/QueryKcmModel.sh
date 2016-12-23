#/bin/bash

READFILE=$1

while read line; do
     echo "$line finished!"
     grep -w $line Chinese_alltext_clean.model1 >> $line.topic
     python2.7 TopicWordAggregator.py $line.topic $line >> $2.result
     rm $line.topic
done < $READFILE
