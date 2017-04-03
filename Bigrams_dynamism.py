from textblob import TextBlob
with open("SentiPhraseNet/Train_Test_Unknown_bigrams.txt",'r',encoding='utf-8') as f1:
    with open("dynmi_pos_bi.txt",'a',encoding='utf-8') as f2:
      with open("dynmi_neg_bi.txt",'a',encoding='utf-8') as f3:
           with open("dynmi_neu_bi.txt",'a',encoding='utf-8') as f4:
     
            for line in f1:
            
               blob = TextBlob(line)
               tran_blob = blob.translate(to = 'en' )
               pol = tran_blob.sentiment.polarity
               print(blob,tran_blob.sentiment.polarity)
               
               if(pol>0.0):
                   f2.write(str(blob.strip('\n'))+"\t"+(str(tran_blob))+"\t"+str(pol)+"\n")
               elif(pol<0.0):
                   f3.write(str(blob.strip('\n'))+"\t"+(str(tran_blob))+"\t"+str(pol)+"\n")
               else:
                   f4.write(str(blob.strip('\n'))+"\t"+(str(tran_blob))+"\t"+str(pol)+"\n")
       
