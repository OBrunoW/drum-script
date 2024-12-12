import os
import subprocess
from pydub import AudioSegment

def isolate_drums(input_path, output_path="output/drum_song.mp3"):
    try:
        # Diretório temporário para Demucs
        temp_dir = "temp_demucs"
        os.makedirs(temp_dir, exist_ok=True)

        # Executa o Demucs com o modelo mdx_extra_q
        print("Executando Demucs com modelo mdx_extra_q...")
        subprocess.run(
            ["demucs", "-n", "mdx_extra_q", "--two-stems=drums", "-o", temp_dir, input_path],
            check=True
        )

        # Caminho esperado para o arquivo de bateria
        demucs_output_dir = os.path.join(temp_dir, "mdx_extra_q", os.path.splitext(os.path.basename(input_path))[0])
        drums_file_wav = os.path.join(demucs_output_dir, "drums.wav")
        drums_file_mp3 = os.path.join(demucs_output_dir, "drums.mp3")

        # Verifica se o arquivo foi gerado como WAV ou MP3
        if os.path.exists(drums_file_wav):
            print("Convertendo WAV para MP3...")
            audio = AudioSegment.from_wav(drums_file_wav)
            audio.export(output_path, format="mp3")
        elif os.path.exists(drums_file_mp3):
            os.rename(drums_file_mp3, output_path)
        else:
            raise FileNotFoundError(f"Arquivo de bateria não encontrado: {drums_file_wav} ou {drums_file_mp3}")

        # Retorna o caminho de saída
        return output_path
    except Exception as e:
        print(f"Erro ao isolar a bateria: {e}")
        return None
