import sounddevice as sd
import wavio as wv
from scipy.io.wavfile import write

frecuencia = 44100
duracion = 3

print('Paso 1')
gravacion = sd.rec(int(frecuencia * duracion), samplerate=frecuencia, channels=2)

print('Paso 2')
print('Grabacion iniciada...')
sd.wait()

print('Paso 3')
print('Grabacion detenida!!!')
write('audio.wav', frecuencia, gravacion)

#print('Paso 4')
#wv.write('audio1.wav', gravacion, frecuencia, sampwidth=2)