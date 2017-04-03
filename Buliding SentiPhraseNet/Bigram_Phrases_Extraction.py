
import nltk
import re
from collections import defaultdict
out=0
j=0
ne=0
p=0
keywords_neg_bi = defaultdict(lambda : 0)
with open("Train_data.txt","r",encoding='utf-8') as f1:
  with open("SentiPhraseNet_Bigram_Key.txt","a",encoding='utf-8') as f2: 
     
       for line in f1:
           token = {}
           token = nltk.word_tokenize(line)
           n=len(token)
           j=j+1
           m=token[n-1]
           for i in range(3,n,2):
                if( (token[i-2]=='NN' and token[i]=='JJ') or (token[i-2]=='JJ' and token[i]=='NN') or (token[i-2]=='JJ' and token[i]=='VM') or (token[i-2]=='NN' and token[i]=='RB') or (token[i-2]=='RB' and token[i]=='NN') or (token[i-2]=='RB' and token[i]=='VM') ):
              
                   k=token[i-3]
                   l=token[i-1]
                   print(k,l)
                   if not keywords_neg_bi[k+'\t'+l]:
                         f2.write(k+'\t'+l+'\n')
                         keywords_neg_bi[k+'\t'+l] = 1
                else:
                   out=out+1
    
print(j,out)
              
              

              
          
               










