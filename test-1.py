#installations required
'''pip install beautifulsoup4
pip install google
pip install wikipedia
pip install googletrans
pip install PyDictionary
install keras also
pip install webdriver-manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
pip install speech
'''
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
import wikipedia
from googletrans import Translator
translator = Translator()
from PyDictionary import PyDictionary
dictionary=PyDictionary()
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
import time
import speech_recognition as sr 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install()) 
r = sr.Recognizer()

#training data
dataset = pd.read_csv('data-question.csv',header=None,sep='\t')
dataset1 = pd.read_csv('data-answer.csv',header=None,sep='\t')
x = dataset.iloc[:,1].values
y = dataset.iloc[:,0].values
#countvectorizer
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(x).toarray()

a=len(X[1])
b=len(y)
b=b+1
#model training
model = Sequential()
model.add(Dense(units = (a+50), activation = 'relu', input_dim = a))
model.add(Dense(units = 1000, activation = 'relu'))
model.add(Dense(units = b, activation = 'softmax'))
model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(X,y, batch_size = 10, epochs = 100)
#############

#google searchbox
def get_results(query):
    query = query.replace(' ', '+')
    driver.get('http://www.google.com/search?q=' + query)
    answer = driver.execute_script(
            "return document.elementFromPoint(arguments[0], arguments[1]);",
            350, 230).text
    print('Bot: '+answer)
    speak.Speak(answer)
    
#Write function 
def perform_training():
     questions_num = dataset.iloc[-1,0]
     answers_num = dataset1.iloc[-1,0]
     questions_cnt = questions_num + 1
     answers_cnt   = answers_num + 1
#Input question
     while True: 
         speak.Speak('Enter the question')
         question_train = input('Bot: ')
         if (question_train == 'quit') or (question_train == 'Quit'):
            speak.Speak('Training Stopped')
            print('Bot: Training Stopped')         
            break; 
    #Writing question part
         file = open('data-question.csv','a') 
         file.write("\n")
         file.write(str(questions_cnt)) 
         file.write("\t")
         file.write(str(question_train))      
         file.close()
         questions_cnt = questions_cnt + 1
      
    #Input answer
         speak.Speak('Enter the answer')
         answer_train = input('Bot: ')
         file = open('data-answer.csv','a') 
         file.write("\n")
         file.write(str(answers_cnt))
         file.write("\t")
         if (answer_train == 'quit') or (answer_train == 'Quit'):
            print('Bot: Training Stopped...For the above question blank wil be the answer, you have to over-ride answer by editing file')   
            speak.Speak('Training Stopped...For the above question blank wil be the answer, you have to over-ride answer by editing file')
            break; 
    #Writing answer part      
         file.write(str(answer_train))      
         file.close()
         answers_cnt = answers_cnt + 1

def bot_session():        
#Bot session starts from here
    print('\n')
    print('Bot: Welcome Madhu Manivannan..,i am here to help you')
    speak.Speak('Welcome Madhu Manivannan..,i am here to help you')
    print('Bot: Type "Quit" to stop ')
    speak.Speak('Type "Quit" to stop ')
    prev_pred = 0     
    while True:
#welcome block    
        ip = input('Madhu:')
    #wikipedia block    
        if ('wiki' in ip) or ('Wiki' in ip) or ('Wikipedia' in ip) or ('wikipedia' in ip):
            
            print ('Bot: You are Now inside Wiki session:')
            speak.Speak('You are Now inside Wiki session:')
            speak.Speak('Please enter search word:')
            wiki = input('Bot: Please enter search word:')
            if wiki == 'quit' or ip == 'Quit':
                print('Bot: Bye')
                speak.Speak('Bye')
                break; 
            print('Bot:'+ wikipedia.summary(wiki,sentences=10))
            speak.Speak(wikipedia.summary(wiki,sentences=2))
    #translator
        elif ('translate' in ip) or ('Translate' in ip):
                   
            speak.Speak('Please enter text to translate:')
            tran = input('Bot: Please enter text to translate: ' )
            speak.Speak('please enter destination language:')
            lang = input('Bot: please enter destination language: ')
                   
            trans = translator.translate(tran,dest=lang)
            print('Bot: '+trans.text)
            speak.Speak(trans.text)
    #dictionary
        elif ('dict' in ip) or ('Dict' in ip) or ('dictionary' in ip) or ('Dictionary' in ip):
            
            
            speak.Speak('Please enter the word:')
            find = input('Bot: Please enter the word: ')
            print ('Bot: ',dictionary.meaning(find))
            speak.Speak(dictionary.meaning(find))  
    #mike section        
        elif ('activate mike' in ip) or ('Activate mike' in ip):
                                                                                          
            with sr.Microphone() as source:                                                                       
                print("Speak:")                                                                                   
                audio = r.listen(source)          
            try:
                print("You said " + r.recognize_google(audio))
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
                
            ip_1=np.append(r.recognize_google(audio),1)
            x1 = cv.transform(ip_1).toarray()
            pred = model.predict_classes(x1)
            pred = pred[0]-1
            op = str(dataset1.iloc[pred,1])
            print('Bot: '+op)
            speak.Speak(op)
    #selinium google searchbox    
        elif ('chitti' in ip) or ('chiti' in ip) or ('Chitti' in ip) or ('Chiti' in ip):
            ip=ip.split()
            z=len(ip)
            for i in range(z):
                if ip[i] == 'chitti' or ip[i] == 'Chitti' or ip[i] == 'chiti' or ip[i] == 'Chiti':
                    ip[i]= ' '
            ip = ' '.join(ip)
            get_results(ip)
                    
        else:
            ip_1=np.append(ip,1)
            x1 = cv.transform(ip_1).toarray()
            pred = model.predict_classes(x1)
            pred = pred[0]-1
    #Ask user want to train or not     
            if (pred == prev_pred):
                speak.Speak('if you want to train previous question type Tain below')
                ask = input('Bot: ')
                if (ask == 'train') or (ask =='Train') or(ask == 'yes') or(ask == 'Yes'):
                     speak.Speak('Training session started')
                     speak.Speak('Please enter the password to start training') 
                     password = input('Enter the password: ')
                     if (password == 'erfinder'):
                       perform_training()
                     else:
                       speak.Speak('Incorrect password')
                       break;               
            prev_pred = pred         
            op = str(dataset1.iloc[pred,1])
            if (op == '00001'):
                 speak.Speak('Please enter the word:')
                 find = input('Bot: Please enter the word: ')
                 print ('Bot: ',dictionary.meaning(find))
                 speak.Speak(dictionary.meaning(find)) 
            elif (op == '00002'):
                 speak.Speak('Please enter search word:')
                 wiki = input('Bot: Please enter search word:')
                 if wiki == 'quit' or ip == 'Quit':
                   print('Bot: Bye')
                   speak.Speak('Bye')
                   break; 
                 print('Bot:'+ wikipedia.summary(wiki,sentences=10))
                 speak.Speak(wikipedia.summary(wiki,sentences=2))
            elif (op == '00003'):
                 speak.Speak('Training session started')
                 speak.Speak('Please enter the password to start training') 
                 password = input('Enter the password: ')
                 if (password == 'erfinder'):
                   perform_training()
                 else:
                   speak.Speak('Incorrect password')
                   break;
     
            time.sleep(1)
            print('Bot: '+op)
            speak.Speak(op)
            
        
        if ip == 'quit' or ip == 'Quit':
            print('Bot: Bye')
            speak.Speak('Bye')
            break;   
            
 
 bot_session()        
      
#end -------------------------------------------------------------------

##########################################################################
get = input('Enter:')

get=np.append(get,1)
x1=cv.transform(get).toarray()

pred=model.predict_classes(x1)
pred = pred[0]-1
print(str(dataset1.iloc[pred,1]))

pred=classifier.predict(x1)

pred=sorted(pred[0], key=pred[0].get, reverse=True)[:3]