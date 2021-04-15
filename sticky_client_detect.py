# -*- coding: utf-8 -*-
"""
"""
import random
import sklearn
import numpy
import pandas as pd
from sklearn.naive_bayes import GaussianNB
#from sklearn.naive_bayes import BernoulliNB
#from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def read_file():
    f=open("C:/data")
    line = f.readline()
    data_list=[]
    while line:
        data_list.append(line)
        line = f.readline()
    f.close()
    return data_list

def make_data(data_list,all_data):
    for item in data_list:
        temp=item.split()
        if(len(temp)==7):
            all_data.append(temp)
        
def add_label(all_data):
    for item in all_data:
        if item[2]==item[6]:
            if item[5]>item[4]:
                item.append(0)
            else:
                item.append(1)
        else:
            item.append(1)



#def split_data_set(data_set, split_ratio):
#    train_size = int(len(data_set) * split_ratio)
#    train_set = []
#    data_set_copy = list(data_set)
#    while len(train_set) < train_size:
#        index = random.randrange(len(data_set_copy))
#        train_set.append(data_set_copy.pop(index))
#    return [train_set, data_set_copy]

#def n_bayes():
    
    
    
def main():
    data_list=[]
    all_data=[]
    client_feature=[]
    client_target=[]
    
    data_list=read_file()
    make_data(data_list,all_data)
    add_label(all_data)
    vectorizer = TfidfVectorizer()
    for i in all_data:
        if len(i)!=0:
            i=list(map(str,i))
            temp=[]
            temp.append(i[0])
            temp.append(i[1])
            temp.append(i[3])
            client_feature.append(temp)
            client_target.append(i[-1])
    feature_train, feature_test, target_train, target_test = train_test_split(client_feature, client_target, test_size=0.3,random_state=0)
    feature_train=vectorizer.fit_transform(d for d in feature_train)
    NB=GaussianNB()
    #numpy.asarray(target_train).astype(numpy.float64)
    NB.fit(numpy.array(feature_train),numpy.array(target_train))
    predict_results=NB.predict(feature_test)
    print(accuracy_score(predict_results, target_test))
    conf_mat = confusion_matrix(target_test, predict_results)
    print(conf_mat)
    print(classification_report(target_test, predict_results))
#    test=pd.DataFrame(data=all_data)
#    test.to_csv('C:/code_aruba/testcsv.csv',encoding='gbk')
    

if __name__=='__main__':
    main()
    
    
    
