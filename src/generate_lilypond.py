import subprocess
import os

def generate_lilypond(events, output_path="output/drum_script.ly"):
    """
    Gera o código LilyPond com base nos eventos classificados e cria um PDF automaticamente.
    """
    # Garante que o diretório de saída existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Gera o arquivo .ly
    with open(output_path, "w") as f:
        f.write("\\version \"2.22.1\"\n")
        f.write("\\drummode {\n")
        f.write("    \\time 4/4\n")
        f.write("    \\tempo 4 = 120\n\n")

        # Adiciona eventos ao LilyPond
        for onset, instrument in events:
            f.write(f"    {instrument}4 ")  # Adiciona cada evento
        f.write("\n}\n")

    print(f"Código LilyPond gerado em {output_path}")

    # Gera o PDF automaticamente usando LilyPond
    try:
        # Define o diretório de saída para o PDF
        pdf_dir = os.path.dirname(output_path)
        subprocess.run(["lilypond", "-o", pdf_dir, output_path], check=True)
        print(f"PDF gerado: {output_path.replace('.ly', '.pdf')}")
    except FileNotFoundError:
        print("Erro: LilyPond não encontrado. Certifique-se de que está instalado e no PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao gerar o PDF com LilyPond: {e}")

if __name__ == "__main__":
    from classify_events import classify_events
    from spectrogram import process_audio

    drum_audio = "temp_demucs/mdx_extra_q/drum_song/drums.wav"
    _, onsets = process_audio(drum_audio)
    events = classify_events(drum_audio, onsets)
    generate_lilypond(events)
