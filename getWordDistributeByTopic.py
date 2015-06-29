import re
import pickle

topic = open('topicInfo')
topics_dict = {}
word_dist_dict = {}

while 1:
    lines = topic.readlines(100000)
    if not lines:
        break

    for line in lines:
        if not re.match(r'^topic', line, re.M | re.I):
            continue
        topic_list = []
        single_topic_arr = line.split(' ')

        topic_num = single_topic_arr[1].replace('#', '')
        for word in single_topic_arr:
            word_weight_arr = word.split('*')
            if len(word_weight_arr) is not 2:
                continue

            # build topic word weight
            topic_word_weight_dict = {}
            topic_word_weight_dict[word_weight_arr[1]] = word_weight_arr[0]
            topic_list.append(topic_word_weight_dict)

            # build word topic distribution
            word_topic_weight_dict = {}
            if word_weight_arr[1] in word_dist_dict:
                word_topic_weight_dict = word_dist_dict[word_weight_arr[1]]
            word_topic_weight_dict[topic_num] = word_weight_arr[0]
            word_dist_dict[word_weight_arr[1]] = word_topic_weight_dict

        topics_dict[topic_num] = topic_list

f_topics_dict = open('topics_dict.pkl', 'wb')
f_word_dist_dict = open('word_dist_dict.pkl', 'wb')
pickle.dump(topics_dict, f_topics_dict)
pickle.dump(word_dist_dict, f_word_dist_dict)

# build word to topic list
