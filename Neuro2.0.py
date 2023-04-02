import random
import json
import torch
import numpy as np
import os
from Brain import neuralnetwork
from Neural import bag_of_words ,tokenize


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
with open("emotions.json","r") as json_data:
    intents = json.load(json_data)

FILE = "TrainData.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = neuralnetwork(input_size,hidden_size,output_size).to(device)
model.load_state_dict(model_state)
model.eval()

#########################-->Neuro starts here
Name = "Neuro"

from Listen import Listen
from Speak import Say
from task import noninput
from task import inputfun 
import pyautogui as p

Say("verification successful")
Say("welcome back Likhith sir")
def Main():
  sentence = Listen()
  result = str(sentence)

  if sentence == "Turn off":
              Say("thanks for using me sir, have a good day.")
              Say("Neuro, powering off")
              exit()
      
  sentence = tokenize(sentence)
  x = bag_of_words(sentence,all_words)
  x = x.reshape(1,x.shape[0])
  x = torch.from_numpy(x).to(device)

  output = model(x)

  _, predicted = torch.max(output,dim=1)

  tag = tags[predicted.item()]

  probs = torch.softmax(output,dim=1)
  prob = probs[0][predicted.item()]

  if prob.item() > 0/75:
    for intent in intents['intents']:
              if tag == intent["tag"]:
                  reply = random.choice(intent["responses"])
              
                  if "time" in reply:
                    noninput(reply)

                  elif "date" in reply:
                    noninput(reply)
              
                  elif "day" in reply:
                    noninput(reply)
                  
                  elif "volume up" in reply:
                    noninput(reply)
                  
                  elif "volume down" in reply:
                    noninput(reply)
                  
                  elif "volume mute" in reply:
                    noninput(reply)
                  
                  elif "weather" in reply:
                      inputfun(reply,result)
                    
                  elif "wikipedia" in reply:
                    inputfun(reply,sentence)

                  elif "google" in reply:
                    inputfun(reply,result)
                  
                  elif "youtube" in reply:
                      inputfun(reply,result)
                  
                  elif "news" in reply:
                      inputfun(reply,result)
                  
                  elif "game" in reply:
                      inputfun(reply,result)
                  
                  elif "system info" in reply:
                      inputfun(reply,result)
                      
                  else:
                      Say(reply)

while True:
    Main()