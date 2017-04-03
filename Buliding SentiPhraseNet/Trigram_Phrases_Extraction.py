
import nltk
import re
from collections import defaultdict
out=0
j=0
ne=0
p=0
keywords_neg_bi = defaultdict(lambda : 0)

with open("Train_data.txt","r",encoding='utf-8') as f1:
  with open("SentiPhraseNet/SentiPhraseNet_Trigram_Key.txt","a",encoding='utf-8') as f2:
     
       for line in f1:
         token = {}
         token = nltk.word_tokenize(line)
         n=len(token)
         j=j+1
         m=token[n-1]
         for i in range(5,n,2):
            
            if( (token[i-4]=='VM' and token[i-2]=='NN' and token[i]=='NN') or (token[i-4]=='NN' and token[i-2]=='VM' and token[i]=='NN') or (token[i-4]=='NN' and token[i-2]=='NN' and token[i]=='VM')):
               w=token[i-5]
               k=token[i-3]
               l=token[i-1]
               if not keywords_neg_bi[w+'\t'+k+'\t'+l]:
                       f2.write(w+'\t'+k+'\t'+l+'\n')
                       keywords_neg_bi[w+'\t'+k+'\t'+l] = 1
            else:
                 out=out+1
  
print(j,out)




          
               










