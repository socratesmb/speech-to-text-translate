# Este es un codigo para ver las capacidades de whisper y tener una base para entender al traduccion de audio

# Necesitamos minimo python 3.9 e instalar Whisper, Pytube y ffmpeg

# pip install git+https://github.com/openai/whisper.git
# pip install pytube
# https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/

 # Ya estamos melos, ahora a codificar

import logging
import pytube
import whisper
import sys
import argparse


analizador = argparse.ArgumentParser(description='Transcripcion de video de YouTube a texto usando whisper')

analizador.add_argument("--video", help = "https://www.youtube.com/watch?v=2_0yQDOYHTM")
analizador.add_argument("--model", help = "base")
argumentos = analizador.parse_args()

logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s [%(levelname)s] %(message)s",
  handlers=[
    logging.StreamHandler(sys.stdout)
  ]
)

logging.info("Descargando modelo de whisper...")
modelo = whisper.load_model(argumentos.model)

logging.info("Descargando video de Yotube...")
VideoYoutube = pytube.YouTube(argumentos.video)

logging.info("Obteniendo el audio del video..")
audio = VideoYoutube.streams.get_audio_only()
audio.download(filename="test2.mp4")

logging.info("Transcribiendo el audio")
resultado = modelo.transcribe("test2.mp4")

print(resultado["text"])