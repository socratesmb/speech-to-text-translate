import pytube
import whisper

Video = pytube.YouTube('https://www.youtube.com/watch?v=2_0yQDOYHTM')

print('Paso1')
Audio = Video.streams.get_audio_only()
Audio.download(filename='test.mp4')

print('Paso2')
modelo = whisper.load_model('base')
print('Paso3')
resultado = modelo.transcribe('test.mp4')

print(resultado['text'])