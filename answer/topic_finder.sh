grep -w $1 Chinese_alltext_clean.model1 >> $1.topic
python2.7 TopicWordAggregator.py $1.topic $1
rm $1.topic
