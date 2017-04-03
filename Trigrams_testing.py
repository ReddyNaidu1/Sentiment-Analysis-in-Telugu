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
    with open("SentiPhraseNet/Trigram_keywords_neg.txt","r",encoding='utf-8') as f2:
        with open("SentiPhraseNet/Trigram_keywords_pos.txt","r",encoding='utf-8') as f3:
            with open("SentiPhraseNet/Trigram_keywords_neu.txt","r",encoding='utf-8') as f4:
                with open("Train_Test_Trigrams_crosschecks.txt","a",encoding='utf-8') as f7:
                       with open("Train_Test_Unknown_Trigrams.txt","a",encoding='utf-8') as f8:
                              
                            neg_list_tri = [x.strip() for x in f2.readlines()]
                            pos_list_tri = [x.strip() for x in f3.readlines()]
                            neu_list_tri = [x.strip() for x in f4.readlines()]


                            keywords_neg_tri = defaultdict(lambda : 0)  
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
                               
                               temp= []
                               for i in range(5,n,2):
                        
                                if((token[i-4]=='VM' and token[i-2]=='NN' and token[i]=='NN') or (token[i-4]=='NN' and token[i-2]=='VM' and token[i]=='NN') or (token[i-4]=='NN' and token[i-2]=='NN' and token[i]=='VM')):
                                     flag=1
                                     E=weights[token[i-4]]
                                     F=weights[token[i-2]]
                                     G=weights[token[i]]
                                     wgt = max(E,F,G)
                                     string1 = token[i-5]+"\t"+token[i-3]+"\t"+token[i-1]+"\t"+str(wgt)
                                     temp.append(string1)
                                
                               if(flag==0):
                                   al =0
                                   #print("sentiment is unknown and no keywords")
                                   
                                   
                               else:
                                   out+=1
                                   for v in range(0,len(temp)):
                                        #flag=0
                                        
                                        gef= temp[v]
                                        tri1 = gef.split()[:3]
                                        we1 = gef.split()[3:]
                                        tri1 = '\t'.join(tri1)
                                        we1 = '\t'.join(we1)
                                        #print(bi1,we1)
                                        if tri1 in neg_list_tri:
                                            NS = NS + 1
                                            #print("1 neg")                                          
                                        elif tri1 in pos_list_tri:
                                            PS = PS + 1
                                            #print("1 pos")
                                        elif tri1 in neu_list_tri:
                                             NU = NU + 1
                                             #print("1 neutral")
                                        else:
                                             if not keywords_neg_tri[tri1]:
                                                   f8.write(tri1+'\n')
                                                   keywords_neg_tri[tri1] = 1

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
                                       print(NS,PS,NU,tri1)
                                       print("unknown but keywords are present")
                                       up+=1
                                   
                               
        
print(j,out,x,c,o,p,pnu,nnu,amb,up)




















                                        
##                                   for h in range(0,len(temp1)):
##                                              gef= temp1[h]
##                                              bi2 = gef.split()[:3]
##                                              we2 = gef.split()[3:]
##                                              bi2 = '\t'.join(bi2)
##                                              we2 = '\t'.join(we2)  
##                                              if bi2 in neg_list_tri:
##                                                NS = NS + int(we2)
##                                                vbr = bi2
##                                            #print("1")
##                                              elif bi2 in pos_list_tri:
##                                                vbr = bi2
##                                                PS = PS + int(we2)
##                                                #print("1")
##                                              elif bi2 in neu_list_tri:
##                                                vbr=bi2
##                                                NU = NU + 1
##                                                #print("1")
##                                        
##                                              else:
##                                                 if not keywords_neg_bi[bi2]:
##                                                   f8.write(bi2+'\n')
##                                                   keywords_neg_bi[bi2] = 1
##                                        
##
##                                   sent = PS - NS
##                                   print(PS,NS,sent)
##                                   if(sent<0):
##                                       print(vbr,line,"negative")
##                                       out+=1
##                                       
##                                   elif(sent>0):
##                                       print(vbr,line,"positive")
##                                       out+=1
##                                       
##                                   elif(NU > 0):
##                                       print(vbr,line,"neutral")
##                                       out+=1
##                                       
                                   
                        
                                    #print(line)
##                               flag=0
##                               PS = 0
##                               NS = 0
##                               NU = 0 
##                               sent=0
                              # break 
                               
          
    
              
              

              
          
               










