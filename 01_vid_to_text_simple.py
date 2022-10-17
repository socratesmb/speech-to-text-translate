from fnmatch import translate
import pytube
import whisper

Video = pytube.YouTube('https://www.youtube.com/watch?v=2_0yQDOYHTM')

print('Paso1')
Audio = Video.streams.get_audio_only()
Audio.download(filename='test.mp3')

print('Paso2')
modelo = whisper.load_model('tiny')
print('Paso3')
resultado = modelo.transcribe('test.mp3')

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


'''
print('Paso4.1')
audio = whisper.load_audio('test.mp3')
print(audio)
audio = whisper.pad_or_trim(audio)
print(audio)

print('Paso4.2')
mel = whisper.log_mel_spectrogram(audio).to(modelo.device)
print(mel)

print('Paso4.3')
_, lg_audio = modelo.detect_language(mel)
print(lg_audio)
print('Paso4.3.1')
print(f"Deteccion de lenguaje: {max(lg_audio, key=lg_audio.get)}")cls
'''