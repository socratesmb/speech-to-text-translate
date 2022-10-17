# Este codigo es para grabar audio y guardarlo, trabaja con tiempo y frecuencia, por lo cual tiene un tiempo para poder grabar el audio

import sounddevice as sd # Libreria para usar el microfono
import wavio as wv # Libreria para crear audio en formato wav
from scipy.io.wavfile import write # Lo mismo que arriba pero mas rapido

frecuencia = 44100 # Frecuencia, no la cambie si no sabe de sonido
duracion = 3 # Tiempo de grabacion

print('Paso 1')
gravacion = sd.rec(int(frecuencia * duracion), samplerate=frecuencia, channels=2) # Grabamos el audio

print('Paso 2')
print('Grabacion iniciada...')
sd.wait() # Creamos una pausa necesaria para procesar

print('Paso 3')
print('Grabacion detenida!!!')
write('audio.wav', frecuencia, gravacion) # Guardamos el audio 

#print('Paso 4')
#wv.write('audio1.wav', gravacion, frecuencia, sampwidth=2) # Lo mismo que la linea 19 pero mas largo