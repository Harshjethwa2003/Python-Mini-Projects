import requests
import json
import pyttsx3
engine=pyttsx3.init()
print("Welcome To Weather app , Created By Harsh ")
city=input("Enter the name of the city:")

url=f"https://api.weatherapi.com/v1/current.json?key=036c268c090347a4824134220240503&q={city}"

r= requests.get(url)

wdic= json.loads(r.text)
print(wdic["location"]["region"])
print(wdic["current"]["temp_c"])
print(wdic["location"]["localtime"])
a=wdic["location"]["region"]
b=wdic["current"]["temp_c"]
c=wdic["location"]["localtime"]
engine.say("the city name entered is" + city)
engine.say("the state of the current city is" + a)
engine.say("the temperature of the city is" + str(b) +"degree Celcius")
engine.say("the current time of the city is" + c)

engine.runAndWait()
print("Thank you ")