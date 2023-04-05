#check modules
try:
    from googlesearch import search
    import requests
    from bs4 import BeautifulSoup 
    import re
    import io
    import urllib.request
    import plag_Word as f
except ImportError:
    print("MODULES NOT FOUND")
def noise_suppp(s_percent,f_percent):
    print(s_percent, f_percent)
    s_percent=s_percent/100
    f_percent=f_percent/100
    plag_Sentence_1=0
    input_1=open("new.txt","r")
    read_File_1=input_1.read().splitlines()

    with open("web.txt",'r',encoding='utf-8') as fi:
        read_File_2=fi.read().splitlines()

    #input_2=open("LIST.txt","r")
    #read_File_2=input_2.read().splitlines()

    string_File_1=''.join(read_File_1)
    string_File_2=''.join(read_File_2)

    sentence_File_1=string_File_1.split('.')
    sentence_File_2=string_File_2.split('.')

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

    if plag_Sentence_1/len(sentence_File_1[:-1])>f_percent:#y = file ka % allowed
       print("copied :")
    else:
        print("Valid!!")

    #print(plag_Sentence_1)
    #print(copy_Sentence_1)

#websearch    
content=[]
web=input("Search: ")
s_percentage=90
f_percentage=90
for i in search(web, tld="co.in", num=0, stop=1, pause=0): #num/stop=number of websites
    #print(i) #prints the website links
    r=requests.get(i)
    s=BeautifulSoup(r.content,'html.parser')
    for each_text in s.find_all('body'):
        content.append(each_text.text)#adds content of web to list
        #print(content)
    for every in list(content):
        #print(every) #prints the content of the website  
        with io.open("LIST.txt","w",encoding="utf-8") as fi:
            fi.write(every)
            fi.close
    noise_suppp(s_percentage,f_percentage)

