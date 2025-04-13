import re
import pyttsx3
import speech_recognition as sr
import eel
import time


# Text-to-speech setup
def speak(text):
  #remove karega non-ASCII characters ko
  text = re.sub(r'[^\x00-\x7F]+', '', text) #remove non-ASCII characters like emojies
  
  text = str(text) #dekhega ki test string hai ki nhi
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('rate', 165)
  engine.setProperty('volume', 1.0)
  engine.setProperty('voice', voices[2].id)
  eel.DisplayMsg(text)
  engine.say(text)
  eel.receiverText(text)
  engine.runAndWait()



def takecommand():

  r=sr.Recognizer()

  with sr.Microphone() as source:
    print('listenning..')
    eel.DisplayMsg('listenning..')
    r.pause_threshold = 1
    r.adjust_for_ambient_noise(source)

    audio = r.listen(source, 20 ,10)


  try:
         print('recognizing')
         eel.DisplayMsg('recognizing..')
         query = r.recognize_google(audio, language='en-in')
         print(f"user said: {query}")
         eel.DisplayMsg(query)
         time.sleep(2)
         

  except Exception as e:
      return ""
  return query.lower()
  
@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    if query:
        try:
            if "open" in query:
                from backend.features import openCommand
                openCommand(query)

            elif "on youtube" in query:
                from backend.features import PlayYoutube
                PlayYoutube(query)
            else:
                #chatbot deature trigger hoga
                from backend.features import chat_with_openrouter
                response = chat_with_openrouter(query)
                print(response)
                eel.DisplayMsg(response)
                speak(response)

        except Exception as e:
            print("error", e)
    else:
        print("No valid command received.")

    eel.ShowHood()
  