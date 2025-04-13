from playsound import playsound
import eel
import os
import requests
from backend.constant import ASSISTANT_NAME
from backend.command import speak
import pywhatkit as kit
import re
from backend.database import cursor
import webbrowser
from dotenv import load_dotenv


load_dotenv()

# Chatbot function
def chat_with_openrouter(prompt):
    try:
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "Friday AI"
        }

        payload = {
            "model": "deepseek/deepseek-r1-distill-llama-70b:free",
            "messages": [
                {"role": "system", "content": "You are FridayAI, a helpful assistant."},
                {"role": "user", "content": f"Answer briefly in 3 to 4 lines: {prompt}"}
            ]
        }

        response = requests.post(url, headers=headers, json=payload)
        data = response.json()

        if "choices" in data:
            # Handle potential encoding issues
            return data["choices"][0]["message"]["content"].strip()
        else:
            return "Unexpected response format from OpenRouter."

    except Exception as e:
        return f"OpenRouter error: {e}"
    

@eel.expose
def playAssistantSound():
   music_dir ="web\\assets\\audio\\sound.mp3"
   playsound(music_dir)

def openCommand(query):
   query = query.replace(ASSISTANT_NAME, "")
   query = query.replace("open", "")
   query.lower()

   app_name = query.strip()
   
   if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name = ?', (app_name,))
            results = cursor.fetchall()
            print(f"results for '{app_name}':", results)

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening "+query)
                    try:
                        os.system('start '+query)
                    except:
                        speak("not found")
        except:
            speak("some thing went wrong")
  

def PlayYoutube(query):
  search_term = extract_yt_term(query)
  speak("Playing "+search_term+" on YouTube")
  kit.playonyt(search_term)

def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None

     
