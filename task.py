'''using two types of functions
1.non-input
eg:time,date,speedtest
2.input
eg:google search,wikipedia,wikihow'''

#non input function
from asyncio.base_tasks import _task_get_stack
from ctypes.wintypes import tagRECT
import datetime
from flask import g

from importlib_metadata import pass_none
from Speak import Say
import pyautogui

def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)

def volumeup():
    pyautogui.press("volumeup")

def volumedown():
    pyautogui.press("volumedown")
def volumemute():
    pyautogui.press("volumemute")

def noninput(query):  #execution
    query = str(query)

    if "time" in query:
        Time()
    
    elif "date" in query:
        Date()
    
    elif "day" in query:
        Day()
    
    elif "volume up" in query:
        volumeup()
    
    elif "volume down" in query:
        volumedown()
    
    elif "volume mute" in query:
        volumemute()

#main inputs functions comes here
#news
#input function
import json
import requests
from Speak import Say
from Listen import Listen
import pywhatkit
import random
from weather import weather
from command import batteryinfo, systeminfo 
 

def inputfun(tag,query):
    if "wikipedia" in tag:
      name = str(query).replace("who is","").replace("about","").replace("what is","").replace("wikipedia","")
      import wikipedia
      result = wikipedia.summary(name)
      Say(result)
    
    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search","")
        pywhatkit.search(query)
    
    elif "youtube" in tag:
        query = str(query).replace("youtube","")
        query = query.replace("play","")
        pywhatkit.playonyt(f"{query}")
    
    elif "news" in tag:
        
        apidict = {"bussiness": "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=3f1b69dbff0b4bf58ca4acb2688331e3",
               "sports": "https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=3f1b69dbff0b4bf58ca4acb2688331e3",
               "entertainment": "https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=3f1b69dbff0b4bf58ca4acb2688331e3",
               "science": "https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=3f1b69dbff0b4bf58ca4acb2688331e3",
               "health": "https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=3f1b69dbff0b4bf58ca4acb2688331e3"
                }
        content = None
        url = None
        Say("Which field news do you want, [bussiness] , [health] , [technology], [sports] , [entertainment] , [science]")
        field = Listen().lower()
        if str(field) == "bussiness" or str(field) == "health" or str(field) == "technology" or str(field) == "sports" or str(field) == "entertainment" or str(field) == "science":
            for key, value in apidict.items():
                if key.lower() in field.lower():
                    url = value
                    print(url)
                    print("url was found")
                    break
                else:
                    url = True
            if url is True:
                print("url not found")

            news = requests.get(url).text
            news = json.loads(news)
            Say("Here is the first news.")

            arts = news["articles"]
            for articles in arts:
                article = articles["title"]
                Say(article)
                news_url = articles["url"]
                print(f"for more info visit: {news_url}")
                Say("Do you Want to Know another news")
                cm= Listen().lower()
                if str(cm) == "yes":
                    pass
                elif str(cm) == "no":
                    break
            Say("thats all")
        else:
            pass
    
    elif "game" in tag:
        Say("Lets Play ROCK PAPER SCISSORS !!")
        print("LETS PLAYYYYYYYYYYYYYY")
        i = 0
        Me_score = 0
        Com_score = 0
        while(i < 5):
            choose = ("rock", "paper", "scissors")  # Tuple
            com_choose = random.choice(choose)
            query = Listen().lower()
            if (query == "rock"):
                if (com_choose == "rock"):
                    Say("ROCK")
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                elif (com_choose == "paper"):
                    Say("paper")
                    Com_score += 1
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                else:
                    Say("Scissors")
                    Me_score += 1
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

            elif (query == "paper"):
                if (com_choose == "rock"):
                    Say("ROCK")
                    Me_score += 1
                    print(f"Score:- ME :- {Me_score+1} : COM :- {Com_score}")

                elif (com_choose == "paper"):
                    Say("paper")
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                else:
                    Say("Scissors")
                    Com_score += 1
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")

            elif (query == "scissors" or query == "scissor"):
                if (com_choose == "rock"):
                    Say("ROCK")
                    Com_score += 1
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                elif (com_choose == "paper"):
                    Say("paper")
                    Me_score += 1
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
                else:
                    Say("Scissors")
                    print(f"Score:- ME :- {Me_score} : COM :- {Com_score}")
            i += 1

        print(f"FINAL SCORE :- ME :- {Me_score} : COM :- {Com_score}") 
    
    elif "weather" in tag:
        weather()

    elif "system info" in tag:
        if "battery info" in query:
            batteryinfo()
        if "system info" in query:
            systeminfo()

