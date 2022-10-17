# Sintetizador de voz para leer el texto

from gtts import gTTS # Libreria necesaria para leer texto

entrada = open('texto-en.txt', 'r') # Abrimos documento

if entrada.mode == 'r': # Alamacenamos el texto del documento como str
    texto = entrada.read()

print(type(texto))
print(texto) # Verificamos texto correcto

voz_texto = gTTS(texto, lang='en') # Creamos la voz artificial, con lang le asignamos el lenguaje

voz_texto.save('test-en.mp3') # Guardamos el audio

print(type(voz_texto))
print(voz_texto) # Verificamos si quedo bien

# Repetimos para que lo sintetice en español
entrada2 = open('texto.txt', 'r') 

if entrada2.mode == 'r':
    texto2 = entrada2.read()

voz_texto2 = gTTS(texto2, lang='es-us')
voz_texto2.save('test-es.mp3')