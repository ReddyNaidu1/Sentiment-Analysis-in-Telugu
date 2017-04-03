import nltk
import os
import re
from collections import defaultdict

##def deleteContent(pfile):
##    pfile.seek(0)
##    pfile.truncate()

out=0
j=0
ne=0
p=0
c=0
o=0
up=0
pnu=0
nnu=0
amb=0
#temp = []
weights = {'RB':2,'JJ':3,'NN':1,'VM':1}
with open("Trail5_check.txt","r",encoding='utf-8') as f1:
    with open("SentiPhraseNet/Bigram_keywords_neg.txt","r",encoding='utf-8') as f2:
        with open("SentiPhraseNet/Bigram_keywords_pos.txt","r",encoding='utf-8') as f3:
            with open("SentiPhraseNet/Bigram_keywords_neu.txt","r",encoding='utf-8') as f4:
                with open("Train_Test_bigrams_crosscheck_after_dynam.txt","a",encoding='utf-8') as f7:
                       with open("Train_Test_Unknown_bigrams.txt","a",encoding='utf-8') as f8:
                              
                            neg_list_bi = [x.strip() for x in f2.readlines()]
                            pos_list_bi = [x.strip() for x in f3.readlines()]
                            neu_list_bi = [x.strip() for x in f4.readlines()]


                            keywords_neg_bi = defaultdict(lambda : 0)  
                            for line in f1:
                               token = {}
                               token = nltk.word_tokenize(line)
                               n=len(token)
                               j=j+1
                               m=token[n-1]
                               PS = 0
                               NS = 0
                               NU = 0
                               flag =0
                               sent = 0
                               x=0
                               temp =[]
                               temp1= []
                               for i in range(3,n,2):
                        
                                if((token[i-2]=='NN' and token[i]=='JJ') or (token[i-2]=='JJ' and token[i]=='NN') or (token[i-2]=='JJ' and token[i]=='VM') or (token[i-2]=='NN' and token[i]=='RB') or (token[i-2]=='RB' and token[i]=='NN') or (token[i-2]=='RB' and token[i]=='VM')):
                                     
                                     flag=1
                                     E=weights[token[i-2]]
                                     F=weights[token[i]]
                                     wgt = max(E,F)
                                     string1 = token[i-3]+"\t"+token[i-1]+"\t"+str(wgt)
                                     temp.append(string1)
                                     
                               if(flag==0):
                                   al =0
                                   #print("sentiment is unknown and no keywords")
                                   
                                   
                               else:
                                   out+=1
                                   for v in range(0,len(temp)):
                                        #flag=0
                                        
                                        gef= temp[v]
                                        bi1 = gef.split()[:2]
                                        we1 = gef.split()[2:]
                                        bi1 = '\t'.join(bi1)
                                        we1 = '\t'.join(we1)
                                        #print(bi1,we1)
                                        if bi1 in neg_list_bi:
                                            NS = NS + 1
                                            #print("1 neg")                                          
                                        elif bi1 in pos_list_bi:
                                            PS = PS + 1
                                            #print("1 pos")
                                        elif bi1 in neu_list_bi:
                                             NU = NU + 1
                                             #print("1 neutral")
                                        else:
                                             if not keywords_neg_bi[bi1]:
                                                   f8.write(bi1+'\n')
                                                   keywords_neg_bi[bi1] = 1

                                   if(NS==len(temp)):
                                        print("negative")
                                        f7.write(line)
                                        f7.write("negative"+'\n')
                                        c+=1
                                   elif(PS==len(temp)):
                                        print("positive")
                                        f7.write(line)
                                        f7.write("positive"+'\n')
                                        o+=1
                                   elif(NU==len(temp)):
                                        print("neutral")
                                        f7.write(line)
                                        f7.write("neutral"+'\n')
                                        p+=1
                                   elif(PS>0 and NU>=0 and NS==0):
                                        print("positive")
                                        f7.write(line)
                                        f7.write("positive"+'\n')
                                        pnu+=1
                                   elif(NS>0 and NU>=0 and PS==0):
                                        print("negative")
                                        f7.write(line)
                                        f7.write("negative"+'\n')
                                        nnu+=1
                                   elif(PS>0 and NS>0 and NU>=0):
                                        print("ambiguous")
                                        f7.write(line)
                                        f7.write("ambiguous"+'\n')
                                        amb+=1
                                   elif(PS>0 and NS>0 and NU>=0):
                                        print("ambiguous")
                                        f7.write(line)
                                        f7.write("ambiguous"+'\n')
                                        amb+=1 
                                   else:
                                       #print(NS,PS,NU,bi1)
                                       print("unknown but keywords are present")
                                       up+=1
                                   
                               
        
print(j,out,x,c,o,p,pnu,nnu,amb,up)




















                                        

          
    
              
              

              
          
               










