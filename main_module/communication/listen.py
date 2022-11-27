import speech_recognition as recognition

listener = recognition.Recognizer()

def listen():
    print('Escuchando....')
    with recognition.Microphone() as source:
        voice = listener.listen(source)
        processed_voice = listener.recognize_google(voice, language='es-es')
        print("You: {}".format(processed_voice))
        return processed_voice.lower()