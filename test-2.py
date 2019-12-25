 
def ask_google(query):

    # Search for query
    query = query.replace(' ', '+')

    driver.get('http://www.google.com/search?q=' + query)

    # Get text from Google answer box

    answer = driver.execute_script(
            "return document.elementFromPoint(arguments[0], arguments[1]);",
            350, 230).text
    print(answer)

     


pip install webdriver-manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

ask_google("what is the weather in chennai")
















######################################################
import wikipedia
from googlesearch import search 

print(wikipedia.summary("door key",sentences=10))


query = "sql code -181"
for j in search(query, tld="com", stop=2): 
    result.append(j)

for i in range(0,2):
        import webbrowser
        webbrowser.open(result[i])
        
print('\n')
print('Bot: Welcome Madhu..,i am here to help you')
print('Bot: Type "Quit" to stop ')
import wikipedia
from googlesearch import search 
     
while True:
#welcome block    
    ip = input('Madhu:')
#google block    
    if ('google' in ip) or ('Google' in ip): 
        
        print ('Bot: You are Now inside Google session:')
        google = input('Bot: Please enter search word:')
        if google == 'quit' or google == 'Quit':
            print('Bot: Bye')
            break; 
        result=[]
        for i in search(google, tld="com", stop=2): 
            result.append(i)
        print('Bot: Please check your default browser,if you are not satisfied with result try some different keyword')    
        for i in range(0,2):
                import webbrowser
                webbrowser.open(result[i])
#wikipedia block    
    elif ('wiki' in ip) or ('Wiki' in ip) or ('Wikipedia' in ip) or ('wikipedia' in ip):
        
        print ('Bot: You are Now inside Wiki session:')
        wiki = input('Bot: Please enter search word:')
        if wiki == 'quit' or wiki == 'Quit':
            print('Bot: Bye')
            break; 
        print('Bot:'+ wikipedia.summary(wiki,sentences=10))
#translator
    elif ('translate' in ip) or ('Translate' in ip):
        
        from googletrans import Translator
        translator = Translator()
        
        tran = input('Bot: Please enter text to translate: ' )
        lang = input('Bot: please enter destination language: ')
        
        trans = translator.translate(tran,dest=lang)
        print('Bot: '+trans.text)
#dictionary
    elif ('dict' in ip) or ('Dict' in ip) or ('dictionary' in ip) or ('Dictionary' in ip):
        
        from PyDictionary import PyDictionary
        dictionary=PyDictionary()
        
        find = input('Bot: Please enter the word: ')
        print ('Bot: ',dictionary.meaning(find))
        
    if ip == 'quit' or ip == 'Quit':
        print('Bot: Bye')
        break;   
    
ip = input('Enter:')

if ('google' in ip) or ('Google' in ip): 
   print ('success')




