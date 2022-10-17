import whisper
import pytube
from googletrans import Translator
from gtts import gTTS

traductor = Translator()

# Primero necesitamos ubicar la url del video
print('Paso 1')
video = pytube.YouTube('https://www.youtube.com/watch?v=2_0yQDOYHTM')

# Obtenemos el audio del video
print('Paso 2')
audio = video.streams.get_audio_only()

# Guardamos el audio para procesarlo
print('Paso 3')
audio.download(filename='set.mp3')

# Leeamos el modelo con whisper, para procesar, asignando el nivel de procesado
print('Paso 4')
modelo = whisper.load_model('small')

# Guardamos el modelo procesado con whisper
print('Paso 5')
resultado = modelo.transcribe('set.mp3')
print(resultado['text'])

# Identificamos lenguaje del texto
print('Paso 6')
lg_texto = traductor.detect(resultado['text'])
print(lg_texto)

# Ahora traducimos a ingles en este caso
print('Paso 7')
texto_traducido = traductor.translate(resultado['text'], dest='en', src=lg_texto.lang)
print(texto_traducido.text)

# Ahora vamos a sintetizar el texto en voz
print('Paso 8')
texto_voz = gTTS(texto_traducido.text, lang='en')

# Ahora guardamos y generamos el audio final
print('Fin Camino')
texto_voz.save('traduccion.mp3')