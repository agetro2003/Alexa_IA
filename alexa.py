import pyttsx3 as voz
import speech_recognition as sr 
import  subprocess as sub
from datetime import datetime

voice = voz.init()
voices = voice.getProperty('voices')
voice.setProperty('voice', voices[2].id)
voice.setProperty('rate', 140)

def say(x):
    voice.say(x)
    voice.runAndWait()

while True:
    recognizer= sr.Recognizer()

    with sr.Microphone() as entrada:
        print('Escuchando...')
        audio = recognizer.listen(entrada, phrase_time_limit=3)

    try:
        texto = recognizer.recognize_google(audio, language='es-MX')
        print(f'usted ha dicho "{texto}"')
        
        texto = texto.lower()
        texto = texto.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
        if 'dispositivo' in texto:

            if 'abre' in texto or 'abrir' in texto:
                paginas = {
                    'whatsapp':'web.whatsapp.com',
                    'telegram':'web.telegram.org',
                    'google':'google.com',
                    'youtube':'youtube.com',
                    'instagram':'instagram.com',
                    'facebook':'facebook.com'
                }
                for i in list(paginas.keys()):
                    if i in texto:
                        sub.call(f'start chrome.exe {paginas[i]}', shell=True)
                        say(f'Abriendo {i}')
            elif 'hora' in texto:
                hora = datetime.now().strftime('%H:%M')
                say(f'Son las {hora}')

            elif 'finaliza' in texto:
                say('Sesion finalizada')
                break                
    except Exception as e:
        print (e)
        print('Error de interpretacion')
