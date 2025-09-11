import pyttsx3
data=pyttsx3.init()
data.setProperty("rate",150)
data.setProperty("voice",data.getProperty('voices')[1].id)
data.say("hi full stack developer")
data.runAndWait()