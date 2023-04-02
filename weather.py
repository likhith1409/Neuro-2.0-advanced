import requests
from Speak import Say
from Listen import Listen
from bs4 import BeautifulSoup




def weather():
    Say('Which city weather report do you want:')
    city = input("Enter Here:>")
    
    url = 'https://www.google.com/search?q={}'.format("temparature in"+city)
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div",class_="BNeawe").text
    Say(f"current tempature in {city} is {temp}")
    print('displaying weather report for:' + city)
    Say('displaying weather report for:' + city)


    url2 = 'https://wttr.in/{}'.format(city)

    res = requests.get(url2)

    print(res.text)

