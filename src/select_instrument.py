import os
import subprocess
from pydub import AudioSegment

def isolate_drums(input_path, temp_dir="temp_demucs"):
    try:
        # Diretório temporário para Demucs
        os.makedirs(temp_dir, exist_ok=True)

        # Executa o Demucs com o modelo mdx_extra_q
        print("Executando Demucs com modelo mdx_extra_q...")
        subprocess.run(
            ["demucs", "-n", "mdx_extra_q", "--two-stems=vocals", "-o", temp_dir, input_path],
            check=True
        )

        # Caminho esperado para o arquivo no_drums.wav
        demucs_output_dir = os.path.join(temp_dir, "mdx_extra_q", os.path.splitext(os.path.basename(input_path))[0])
        no_drums_file_wav = os.path.join(demucs_output_dir, "no_drums.wav")

        # Conversão de WAV para MP3
        no_drums_mp3_path = os.path.join(temp_dir, "no_drums.mp3")
        if os.path.exists(no_drums_file_wav):
            print("Convertendo 'no_drums.wav' para 'no_drums.mp3'...")
            audio = AudioSegment.from_wav(no_drums_file_wav)
            audio.export(no_drums_mp3_path, format="mp3")

        # Retorna o caminho do arquivo MP3
        return no_drums_mp3_path
    except Exception as e:
        print(f"Erro ao isolar os instrumentos: {e}")
        return None
