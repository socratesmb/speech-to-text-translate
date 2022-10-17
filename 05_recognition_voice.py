# Siguiente nivel, este codigo es para reconocer la voz, si usa microfonos externos verifique en su consola tenerlo como prederminado, no tiene limite de tiempo para hablar creo

import speech_recognition as sr  # Libreria para usar microfono

r = sr.Recognizer()  # Instacionamos el modulo para identificar la voz o el audio

with sr.Microphone() as source:  # Activamos el microfono para escuchar
    print('Hable ahora..')
    audio = r.listen(source)  # Guardamos el audio

    try:
        text = r.recognize_google(audio) # Lo procesamos para ser reconocido y guardar lo que hablamos
        print('Usted dijo: {}'.format(text)) # Imprimimos
    except:
        print('No se reconocio la voz')

# Funciona bien con tros idiomas diferentes a español :\