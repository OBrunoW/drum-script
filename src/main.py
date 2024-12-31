import os
import shutil
from src.download_mp3 import download_mp3
from src.select_instrument import isolate_drums

def main():
    while True:
        # Diretórios de trabalho
        temp_dir = "temp_downloads"
        demucs_temp_dir = "temp_demucs"
        output_dir = "output"
        os.makedirs(temp_dir, exist_ok=True)
        os.makedirs(output_dir, exist_ok=True)

        # Solicitar link do usuário
        link = input("Digite o link do YouTube da música (ou 'sair' para encerrar): ")
        if link.lower() == "sair":
            print("Encerrando...")
            break

        # Passo 1: Baixar música do YouTube
        print("Baixando música...")
        mp3_path = download_mp3(link, output_path=os.path.join(temp_dir, "input.mp3"))
        if not mp3_path:
            print("Erro ao baixar a música.")
            continue

        # Passo 2: Separar instrumentos com Demucs
        print("Separando instrumentos com Demucs...")
        no_drums_path = isolate_drums(mp3_path, temp_dir=demucs_temp_dir)
        if not no_drums_path:
            print("Erro ao processar a música.")
            continue

        # Verificar se o arquivo no_drums.mp3 foi gerado
        if not os.path.exists(no_drums_path):
            print("Erro: Arquivo 'no_drums.mp3' não encontrado.")
            continue

        # Passo 3: Mover o arquivo para o diretório final
        try:
            shutil.move(no_drums_path, os.path.join(output_dir, "no_drums.mp3"))
            print(f"Arquivo 'no_drums.mp3' salvo em '{output_dir}'")
        except Exception as e:
            print(f"Erro ao mover o arquivo processado: {e}")

        # Passo 4: Limpeza de arquivos temporários
        print("Limpando arquivos temporários...")
        shutil.rmtree(temp_dir, ignore_errors=True)
        shutil.rmtree(demucs_temp_dir, ignore_errors=True)

        print("Processo concluído! Aguardando próximo link...\n")

if __name__ == "__main__":
    main()
