# Traduccion y reproduccion de voz sin whisper, funciona muy bien cuando se habla en ingles, no tiene limite para hablar

import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound

r = sr.Recognizer()
traductor = Translator()

# while True:

with sr.Microphone() as source:
    print('Hable ahora...')
    audio = r.listen(source)

    try:
        voz_texto = r.recognize_google(audio)
        print('Usted dijo: ' + voz_texto)
        # if (voz_texto == "exit" or voz_texto == "salir"): break
    except sr.UnknownValueError:
        print('No se reconocio la voz')
    except sr.RequestError:
        print('El servidor no responde')

    # Si habla en ingles cambiar dest='es' para traducirlo a español
    texo_traducido = traductor.translate(voz_texto, dest='en')
    print('Texto traducido: ' + texo_traducido.text)

    # De igual manera cambiar lang='es' para sintetizar la voz en español, info de las voces => https://gtts.readthedocs.io/en/latest/module.html#localized-accents
    voz_traducida = gTTS(texo_traducido.text, lang='en')
    voz_traducida.save('test-translate.mp3')

    # Recuerda cambiar la url de la carpeta para reproducir el audio, falla un monton si tiene nombres con -, evitar caracteres especiales
    playsound('D:/CodigosparaAprender/speech-to-text-translate/test-translate.mp3')

# Si se quiere hacer traduccion en bucle poner todo el with dentro de un While Tru:, agregar el siguiente if en el try: if (voz_texto == 'exit'): break
