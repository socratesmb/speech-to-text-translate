# La joya de la corona o como digo yo: Esto es lo melo nea

import sounddevice as sd
from scipy.io.wavfile import write
import whisper
from googletrans import Translator
from gtts import gTTS
from playsound import playsound

traductor = Translator()

frecuencia, duracion = 44100, 7 # Tiempo de grabacion 7 segundos

print('Paso 1')
print('Grabacion iniciada...')
# Se activa el microfono para ser escuchado
gravacion = sd.rec(int(frecuencia * duracion), samplerate=frecuencia, channels=2)

# Se crea una pausa para analizar el audio
print('Paso 2')
sd.wait()
print('Grabacion detenida!!!')

# Se guarda la grabacion de la voz
print('Paso 3')
write('audio.wav', frecuencia, gravacion)

# Creamos el modelo con whisper, para procesar, asignando el nivel de procesado => # https://github.com/openai/whisper#available-models-and-languages
print('Paso 4')
modelo = whisper.load_model('large') # Cambiar large por tiny o base para que sea rapido

# Guardamos el modelo procesado con whisper
print('Paso 5')
resultado = modelo.transcribe('audio.wav')
print(resultado['text'])

# Identificamos lenguaje del texto
print('Paso 6')
lg_texto = traductor.detect(resultado['text'])
print(lg_texto)

# Si habla en otro idioa cambiar dest='es' para traducirlo a español
print('Paso 7')
texto_traducido = traductor.translate(resultado['text'], dest='en', src=lg_texto.lang)
print(texto_traducido.text)

# De igual manera cambiar lang='es' para sintetizar la voz en español, info de las voces => https://gtts.readthedocs.io/en/latest/module.html#localized-accents
print('Paso 8')
texto_voz = gTTS(texto_traducido.text, lang='en')

# Ahora guardamos y generamos el audio final
texto_voz.save('traduccion.mp3')
print('Fin Camino')

# Reproducimos el mensaje
# Recuerda cambiar la url de la carpeta para reproducir el audio, falla un monton si tiene nombres con -, evitar caracteres especiales
playsound('D:/CodigosparaAprender/speech-to-text-translate/traduccion.mp3')

# Tiempo de compilado actual 25 seg, se puede bajar. Disfrutalo