from pyparsing import White
import pytube
import whisper

Video = pytube.YouTube('https://www.youtube.com/watch?v=2_0yQDOYHTM')

print('Paso1')
Audio = Video.streams.get_audio_only()
Audio.download(filename='test.mp4')

print('Paso2')
modelo = whisper.load_model('tiny')
print('Paso3')
resultado = modelo.transcribe('test.mp4')

print('Paso4')
print(resultado['text'])

print('Paso5')
with open('texto.txt', 'w') as file:
    file.write(resultado['text'])
file.close()

print('Paso6')
print(type(resultado))
print(type(file))
print(file)