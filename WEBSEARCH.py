from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
import io
import urllib.request
def search_web(kewword):
    content=[]
    web=kewword
    for i in search(web, tld="co.in", num=1,stop=3, pause=0): #num/stop=number of websites
        #print(i) #prints the website links
        r=requests.get(i)
        s=BeautifulSoup(r.content,'html.parser')
        for each_text in s.find_all('body'):
            content.append(each_text.text)#adds content of web to list
            #print(content)
        for every in list(content):
            #print(every) #prints the content of the website  
            with io.open("web.txt","w",encoding="utf-8") as fi:
                fi.write(every)
                fi.close
        #noise_supp(s_percentage,f_percentage)

#search_web("cheetah")
'''
try:
    from googlesearch import search
    import requests
    from bs4 import BeautifulSoup
    import re
except ImportError:
    print("No module named 'google' found")
content=[]
web=input("Search: ")
for i in search(web, tld="co.in", num=1, stop=1, pause=0): #num/stop=number of websites
    print(i) #prints the website links
    r=requests.get(i)
    s=BeautifulSoup(r.content,'html.parser')
    try:
        for each_text in s.find_all('body'):
            content.append(each_text.text)#adds content of web to list
        #print(content)
        
        for every in list(content):
            print(every) #prints the content of the website  
    except:
        print("No text found")
#print(len(content))   
'''