from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
import io
import urllib.request
import plag_Word as f
def noise_supp_web(s_percent,f_percent,flag):
    #print(s_percent, f_percent)
    s_percent=s_percent/100
    f_percent=f_percent/100
    plag_Sentence_1=0
    #input("troubleshoot")
    if flag==1:
        with open("new.txt","r",encoding='utf-8') as input_1:
            read_File_1=input_1.read().splitlines()
    elif flag==2:
        with open("new1.txt","r",encoding='utf-8') as input_1:
            read_File_1=input_1.read().splitlines()
    
    with open("web.txt",'r',encoding='utf-8') as fi:
        read_File_2=fi.read().splitlines()
    

    #input_2=open("LIST.txt","r")
    #read_File_2=input_2.read().splitlines()

    string_File_1=''.join(read_File_1)
    string_File_2=''.join(read_File_2)
    
    sentence_File_1=string_File_1.split('. ')
    sentence_File_2=string_File_2.split('. ')
    #input()
    #print(sentence_File_2)
    for m in range(len(sentence_File_2)):
        if sentence_File_2[m]=='':
            del sentence_File_2[m]
    #print(sentence_File_2)
    copy_Sentence_1=[]
    for x in sentence_File_1[:-1]:
        for y in sentence_File_2[:-1]:
            if x==y:
                plag_Sentence_1=plag_Sentence_1+1
                copy_Sentence_1.append(x)
                break
            else:
                if f.similar_Sentence(x,y,s_percent)==True:
                    plag_Sentence_1=plag_Sentence_1+1
                    copy_Sentence_1.append(x)
                    break

    if len(sentence_File_1) > len(sentence_File_2):
        if (len(copy_Sentence_1) / len(sentence_File_1[:-1])*100) > f_percent:
            print("copied :")
            print((plag_Sentence_1 / len(sentence_File_1[:-1])*100),"%")
        else:
            print("Valid!!")

    elif len(sentence_File_1) <= len(sentence_File_2):
        if (len(copy_Sentence_1) / len(sentence_File_2[:-1])*100) > f_percent:
            print("copied :")
            print((plag_Sentence_1 / len(sentence_File_2[:-1])*10000),"%")
        else:
            print("Valid!!")
    #print(copy_Sentence_1)

#f=open("new.txt","r")
#noise_supp_web(10,10,1)
