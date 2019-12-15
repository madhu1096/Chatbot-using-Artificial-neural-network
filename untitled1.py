import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('data-question.csv',header=None,sep='\t')

import wikipedia


print(wikipedia.search("Bill"))
print(wikipedia.search("Bill", results=2))

print(wikipedia.summary("door key",sentences=10))

print(wikipedia.page("door key"))
'''
pip install wikipedia
pip install --upgrade google-api-python-client

'''

 
import wikipedia
from googlesearch import search 
query = "door key"
for j in search(query, tld="com", num=10, stop=1, pause=2): 

    import webbrowser
webbrowser.open(j)


from googletrans import Translator
translator = Translator()
z = translator.translate('bye',dest='Tamil')
z.text

from PyDictionary import PyDictionary
dictionary=PyDictionary()
print ('Bot: ',dictionary.meaning(find))



#training data
dataset = pd.read_csv('chatbot-data/science.yml',header=None,sep='\t')

counter=273
for i in range(3,200):
    if(i%2==0):
        
        file = open('data-answer.csv','a') 
        file.write(str(counter)) 
        file.write("\t")
        file.write(str(dataset.iloc[i,:].values)) 
        file.write("\n")
        file.close()
    else:
        counter=counter+1
        file = open('data-question.csv','a')
        file.write(str(counter)) 
        file.write("\t")
        file.write(str(dataset.iloc[i,:].values)) 
        file.write("\n")
        file.close()
        
#use google sheets
        


counter=1
file = open('data-copy.csv','a')
file.write(str(counter)) 
file.write("\t")
file.write(str(dataset.iloc[2,0:].values)) 
file.write("\n")
file.close() 

print(str(dataset.iloc[8,0:].values))