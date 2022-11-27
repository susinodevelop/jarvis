from communication.speak import talk
from decouple import config
from datetime import datetime

USERNAME = config('USER')
BOTNAME = config('BOTNAME')

def initialization():
    #talk("Inicializando sistema")
    #talk("Sistema inicializado")
    welcome()
   
def welcome():    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        talk(f"Buenos días {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        talk(f"Buenas tardes {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        talk(f"Buenas noches {USERNAME}")
    else:
        talk(f"Buenas noches {USERNAME}. Debería dormir un poco.")