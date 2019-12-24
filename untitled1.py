import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('data-question.csv',header=None,sep='\t')

import wikipedia

import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("Hello World")


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

#################################################################################
def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.
    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source) # #  analyze the audio source for 1 second
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #   update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable/unresponsive"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

import speech_recognition as sr
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=1)
    response = recognize_speech_from_mic(recognizer, mic)
    print('\nSuccess : {}\nError   : {}\n\nText from Speech\n{}\n\n{}' \
          .format(response['success'],
                  response['error'],
                  '-'*17,
                  response['transcription']))
    

speak.Speak(response['transcription'])    



