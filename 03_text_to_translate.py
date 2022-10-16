from googletrans import Translator

entrada = open('texto.txt', 'r')

if entrada.mode == 'r':
    texto = entrada.read()

print(type(texto))
print(texto)

traductor = Translator()
lenguaje_texto = traductor.detect(texto)

print(lenguaje_texto.lang)

texto_traducido = traductor.translate(texto, dest='en', src=lenguaje_texto.lang)

print(texto_traducido.text)