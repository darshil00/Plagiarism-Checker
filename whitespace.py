import re

def whitespace_insensitivity(file1,file2):
    ans=file1.read()
    t=list(ans.split("\n"))
    #print(t)
    n=open("new.txt", "w")
    for i in range(len(t)):
        temp=t[i]
        temp.strip()
        final=re.sub(' +',' ',temp)
        temp=list(final)
        m=""
        for i in range(len(temp)-1):
            if i==0:
                if temp[i]==temp[i+1]==".":
                    del temp[i+1]
                else:
                    m=m+temp[i]
            else:
                if temp[i]==temp[i-1]==".":
                    del temp[i]
                else:
                    m=m+temp[i]


        n.write(m)
        n.write("\n")

    file1.close()
    n.close()

    ans1=file2.read()
    t1=list(ans1.split("\n"))
    #print(t)
    k=open("new1.txt", "w")
    for i in range(len(t1)):
        temp1=t1[i]
        temp1.strip()
        final2=re.sub(' +',' ',temp1)
        temp1=list(final2)
        p=""
        #print(temp1)
        for i in range(len(temp1)-1):
            if i==0:
                if temp1[i]==temp1[i+1]==".":
                    del temp1[i+1]
                else:
                    p=p+temp1[i]
            else:
                if temp1[i]==temp1[i-1]==".":
                    del temp1[i]
                else:
                    p=p+temp1[i]


        k.write(p)
        k.write("\n")

    file2.close()
    k.close()

f1=open("testcase1.txt","r")
f2=open("testcase2.txt","r")
whitespace_insensitivity(f1,f2)
'''
f=open("new.txt","r")
f1=open("new1.txt","r")
print(f.read())
print(f1.read())
'''