from src.download_mp3 import download_mp3
from src.select_instrument import isolate_drums
from src.spectrogram import process_audio
from src.classify_events import classify_events
from src.generate_lilypond import generate_lilypond
import os

def main():
    # Caminho para o áudio final do Demucs
    drum_audio = "temp_demucs/mdx_extra_q/drum_song/drums.wav"

    # Passo 1: Baixar música do YouTube
    link = input("Digite o link do YouTube da música: ")
    print("Baixando música...")
    mp3_path = download_mp3(link)
    if not mp3_path:
        print("Erro ao baixar a música.")
        return

    # Passo 2: Isolar a bateria
    print("Isolando bateria...")
    drums_path = isolate_drums(mp3_path)
    if not drums_path:
        print("Erro ao isolar a bateria.")
        return

    # Verifica se o arquivo isolado foi gerado
    if not os.path.exists(drum_audio):
        print(f"Erro: Arquivo de bateria não encontrado em '{drum_audio}'")
        return

    # Passo 3: Processar o áudio
    print("Processando áudio...")
    _, onsets = process_audio(drum_audio)

    # Passo 4: Classificar eventos
    print("Classificando eventos...")
    events = classify_events(drum_audio, onsets)

    # Passo 5: Gerar partitura em LilyPond
    print("Gerando partitura...")
    generate_lilypond(events)

    print("Processo concluído! Verifique a saída na pasta 'output/'.")

if __name__ == "__main__":
    main()
