import pyttsx3 #module
ai= pyttsx3.init() #init is attribute
voices = ai.getProperty('voices') # for girl voice
ai.setProperty('voice',voices[1].id)
ai.say("hello pyhton programers this is my first repo on github")
ai.runAndWait()
    