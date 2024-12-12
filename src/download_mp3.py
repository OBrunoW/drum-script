import yt_dlp
import os

def download_mp3(link, output_path="output/drum_song.mp3"):
    try:
        # Configurações do yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'temp_audio.%(ext)s',
            'noplaylist': True  # Baixa apenas o vídeo fornecido, não a playlist
        }

        # Baixa o vídeo
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

        # Renomeia e move o arquivo para a saída
        temp_file = "temp_audio.mp3"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        os.rename(temp_file, output_path)

        return output_path
    except Exception as e:
        print(f"Erro ao baixar o arquivo: {e}")
        return None
