import pyttsx3

engine = pyttsx3.init('sapi5')

# get voices and set the first of them
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id)

# editing default configuration
engine. setProperty('rate', 190)
engine.setProperty('volume', 1)


def talk(text):
    engine.say(text)
    engine.runAndWait()