import plag_Word as f
def noise_supp(s_percent,f_percent):
    #print(s_percent, f_percent)
    s_percent=s_percent/100
    f_percent=f_percent/100
    plag_Sentence_1=0
    input_1=open("new.txt","r")
    read_File_1=input_1.read().splitlines()
    input_2=open("new1.txt","r")
    read_File_2=input_2.read().splitlines()

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

   #y = file ka % allowed
    if len(sentence_File_1) > len(sentence_File_2):
        if len(copy_Sentence_1) / len(sentence_File_1[:-1]) > f_percent:
            print("copied :")
            print(plag_Sentence_1 / len(sentence_File_1[:-1]),"%")
        else:
            print("Valid!!")

    elif len(sentence_File_1) <= len(sentence_File_2):
        if len(copy_Sentence_1) / len(sentence_File_2[:-1]) > f_percent:
            print("copied :")
            print((plag_Sentence_1 / len(sentence_File_2[:-1])*100),"%")
        else:
            print("Valid!!")

    #print(plag_Sentence_1)
    #print(copy_Sentence_1)