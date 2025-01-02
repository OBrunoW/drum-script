import os
import subprocess
from pydub import AudioSegment

def isolate_drums(input_path, temp_dir):
    try:
        # Diretório temporário para Demucs
        os.makedirs(temp_dir, exist_ok=True)

        # Executa o Demucs com o modelo mdx_extra_q
        print("Executando Demucs com modelo mdx_extra_q...")
        subprocess.run(
            ["demucs", "-n", "mdx_extra_q", "-o", temp_dir, input_path],
            check=True
        )
        
    except Exception as e:
        print(f"Erro ao isolar os instrumentos: {e}")
        return None
