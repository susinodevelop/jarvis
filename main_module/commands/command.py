from communication.speak import talk
from communication.listen import listen
from commands.actions import *
from decouple import config
from random import choice

import pywhatkit
import urllib.request
import json
import datetime
import wikipedia

#TODO no carga los textos(no los dice)
OPENING_TEXT = config('OPENING_TEXT')

def execute(command):
    if 'reproduce' in command:
        music = command.replace('reproduce', '')
        talk('Reproduciendo ' + music)
        pywhatkit.playonyt(music)
    elif 'cuantos suscriptores tiene' in command:
        name_subs = command.replace('cuantos suscriptores tiene', '')
        data = urllib.request.urlopen(
            f'https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername={name_subs.strip()}&key={key}').read()
        subs = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
        talk(name_subs + " tiene {:,d}".format(int(subs)) + " suscriptores!")
    elif 'hora' in command:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
    elif 'busca' in command:
        order = command.replace('busca', '')
        wikipedia.set_lang("es")
        info = wikipedia.summary(order, 1)
        talk(info)
    elif 'ip' in command:
        my_ip = find_my_ip()
        talk(f"La ip del sistema es {my_ip} señor")
    elif 'calculadora' in command:
        talk(choice(OPENING_TEXT))
        open_calculator()
    elif 'comandos' in command:
        talk(choice(OPENING_TEXT))
        open_cmd()
    elif 'notas' in command:
        talk(choice(OPENING_TEXT))
        open_notepad()
    elif 'discord' in command:
        talk(choice(OPENING_TEXT))
        open_discord()
    elif 'cámara' in command:
        talk(choice(OPENING_TEXT))
        open_camera()
    else:
        talk("No entiendo su orden señor")
        talk("¿Puede repetir?")


def run():
    running = True
    while running:
        talk("¿Cómo puedo ayudarle?")
        command = listen()
        if not "salir" in command:
            execute(command)
        else:
            running = False
    talk("Desconectando sistema")
    talk("Que tenga buen día señor")
