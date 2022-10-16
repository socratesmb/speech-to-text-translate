from gtts import gTTS

entrada = open('texto-en.txt', 'r')

if entrada.mode == 'r':
    texto = entrada.read()

print(type(texto))
print(texto)

voz_texto = gTTS(texto, lang='en')

voz_texto.save('test-en.mp3')

print(type(voz_texto))
print(voz_texto)

entrada2 = open('texto.txt', 'r')

if entrada2.mode == 'r':
    texto2 = entrada2.read()

voz_texto2 = gTTS(texto2, lang='es-us')
voz_texto2.save('test-es.mp3')