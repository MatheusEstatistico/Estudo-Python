from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def baixador(url, local_arq):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        qualidade_stream = streams.get_highest_resolution()
        qualidade_stream.download(output_path=local_arq)
        print("Vídeo baixado!")
    except Exception as e:
        print(e)

def janela():
    arquivo = filedialog.askdirectory()
    if arquivo:
        print(f"Selecione a pasta: {arquivo}")

    return arquivo

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Link do vídeo: ")
    local_salvamento = janela()

    if local_salvamento:
        print("Iniciando download...")
        baixador(video_url, local_salvamento)
    else:
        print("Pasta de salvamento invalida")
