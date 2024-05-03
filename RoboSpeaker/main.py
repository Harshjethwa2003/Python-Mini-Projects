import pyttsx3
engine = pyttsx3.init()
print()
print("This is RoboSpeaker 1.1, Created By Harsh Jethwa")
print()
while True:
    speak = input("What do you want me to speak?  :")
    if speak!='stop':
        engine.say(speak)
        engine.runAndWait()
    else:
        print()
        print("Thank you for using RoboSpeaker")
        print()
        break
