import datetime
from Speak import Say

#wish function
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        Say("good morning")
    elif hour>12 and hour<18:
        Say("good afternoon")
    else:
        Say("good evening")
    Say("Hello sir I am Neuro. how can i help you")