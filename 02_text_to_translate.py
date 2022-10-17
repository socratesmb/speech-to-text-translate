# Traductor de texto, usando el texto procesado con Whisper en 01

from googletrans import Translator  # Libreria de google para traducir

# Abrimos el documento por nombre, r => para leer
entrada = open('texto.txt', 'r')

if entrada.mode == 'r':
    texto = entrada.read()  # Almacenamos el texto del documento como str

print(type(texto))
print(texto)  # Imprimimos para ver si esta bien

# Instacciamos el modulo Translator para usarlo
traductor = Translator()  
lenguaje_texto = traductor.detect(texto)  # Verificamos el lenguaje del texto

# Mostramos el lenguaje si es correcto
print(lenguaje_texto.lang)  

# Realizamos la traduccion, pasamos texto, lenguaje destino "dest", y el lenguaje de origen no es indispensable
texto_traducido = traductor.translate(
    texto, dest='en', src=lenguaje_texto.lang)

# Mostramos para ver si quedo bien
print(texto_traducido.text)  

# Creamos documento de texto para guardar la traduccion
with open('texto-en.txt', 'w') as file:  
    file.write(texto_traducido.text)
file.close()

print('Paso6')
print(type(file))
print(file) # Revisamos si quedo bien
