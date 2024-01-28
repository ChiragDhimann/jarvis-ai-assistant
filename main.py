import os
import random

# import os
#
# def say(text):
#     os.system(f"say {text}")
#

import speech_recognition as sr
import win32com.client
import webbrowser
import openai
import datetime
import os
import random
from openai import OpenAI
from config import apikey

speaker=win32com.client.Dispatch(("SAPI.SpVoice"))

chatStr=""
def chat(query):
    global chatStr
    print(chatStr)
    client = OpenAI(api_key=apikey)
    chatStr+=f"chirag: {query}\n Jarvis :"
    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # TODO:Wrap in try Catch
    speaker.Speak(response.choices[0].text)
    chatStr+= f"{response.choices[0].text}"
    return response.choices[0].text
    # if not os.path.exists("Openai"):
    #     os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)


def ai(prompt):

    client = OpenAI(api_key=apikey)
    text=f"Openai response for prompt:{prompt}\n************************\n\n"

    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # TODO:Wrap in try Catch
    # print(response["choice"][0]["text"])
    text+=response.choices[0].text
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt","w") as f:
        f.write(text)


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold=1.5
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said:{query}")
            return query
        except Exception as e:
            return "some error occured ! sorry from jarvis"

if __name__ == '__main__':
     print('PyCharm')
     speaker.Speak("hello i am Jarvis How can I help you")
     while True:
         print("Listening...")
         query=takeCommand()
         # TODO: add more sites
         sites=[["youtube","https://www.youtube.com"],["Google","https://www.google.com"],["wikipedia","https://www.wikipedia.com"],
                ["spotify","https://www.spotify.com"],["amazon","https://www.amazon.com"],["flipkart","https://www.flipkart.com"]
                ,["stackoverflow","https://www.stackoverflow.com"],["leetcode","https://www.leetcode.com"],
                ["codingNinja","https://www.codingninja.com"]
             ,["instagram","https://www.instagram.com"],["facebook","https://www.facebook.com"],["whatsapp","https://www.whatsapp.com"],
                ["codechef","https://www.codechef.com"],["linkedin","https://www.linkedin.com"],["hotstar","https://www.hotstar.com"],
                ["primevideo","https://www.primevideo.com"],["netflix","https://www.netflix.com"]]
         for site in sites:
             if f"Open {site[0]}".lower() in query.lower():
                 speaker.Speak(f"Opening {site[0]} Sir...")
                 webbrowser.open(site[1])
         if "play music".lower() in query.lower():
             musicpath= "/Users/91952/Download/svinee-heights-126947.mp3"
             os.system(f"open {musicpath}")

         # TODO: Feature for time
         elif "the time" in query:
            strfDate=datetime.datetime.now().strftime("%H:%M:%S")
            speaker.Speak(f"Sir Time is {strfDate}")

         elif "open MSword".lower() in query.lower():
             wordPath="/ProgramData/Microsoft/Windows/Start Menu/Programs"
             os.system(wordPath)

         elif "Using Artificial Intelligence".lower() in query.lower():
             ai(prompt=query)

         elif "jarvis Quit".lower() in query.lower():
             exit()

         elif "reset chat".lower() in query.lower():
             chatStr=""

         else:
             print("chating...")
             chat(query)
             # speaker.Speak(query+"Not found")






