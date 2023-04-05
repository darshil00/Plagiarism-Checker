import re
import noiseSuppression as ns
import whitespace as ws
import WEBSEARCH as web
import noiseSupression_web as ns_web
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
import io
import urllib.request

'''
1. compare 2 .txt files with each other
2. compare 2 .txt files with web


for choice 1
file 1 ka input
file 2 ka input
% of plagiarized content allowed

for choice 2
file 1 ka input
file 2 ka input 
keyword to search on web

'''
while True:
    ch=int(input("Please Choose from the Following: \n 1. Comapre 2 .txt Files with Each Other\n 2. Compare 2 .txt Files with Web\n 3. Exit\n "))
    if ch==1:
        f1=open("testcase1.txt","r")
        f2=open("testcase2.txt","r")
        sentence_plagiarizm_allowed=int(input("Enter the amount of plagiarized content in a sentence is allowed(in %): "))
        file_plagiarizm_allowed=int(input("Enter the amount of plagiarized content in a file is allowed(in %): "))
        ws.whitespace_insensitivity(f1,f2)
        ns.noise_supp(sentence_plagiarizm_allowed,file_plagiarizm_allowed)
        continue
    elif ch==2:
        f1=open("testcase1.txt","r")
        f2=open("testcase2.txt","r")
        ws.whitespace_insensitivity(f1,f2)
        n1=open("new.txt","r")
        n2=open("new1.txt","r")
        keyword=input("Enter the Keyword for which you want to compare the files with: ")
        web.search_web(keyword)
        sentence_plagiarizm_allowed=int(input("Enter the amount of plagiarized content in a sentence is allowed(in %): "))
        file_plagiarizm_allowed=int(input("Enter the amount of plagiarized content in a file is allowed(in %): "))
        ns_web.noise_supp_web(sentence_plagiarizm_allowed,file_plagiarizm_allowed,1)
        ns_web.noise_supp_web(sentence_plagiarizm_allowed,file_plagiarizm_allowed,2)
        continue
    else:
        print("Thank you for using our Services:)")
        break

    
                



    


