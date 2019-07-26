# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 12:42:05 2019

@author: zhaomen
"""


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
        

def main():
    data_list=[]
    all_data=[]
    data_list=read_file()
    make_data(data_list,all_data)
    print("------------------------")
    add_label(all_data)
    print("------------------------")

def add_label(all_data):
    for item in all_data:
        if item[2]==item[6]:
            if item[5]>item[4]:
                item.append(0)
            else:
                item.append(1)
        else:
            item.append(1)
    
    

if __name__=='__main__':
    main()
    
    
    
