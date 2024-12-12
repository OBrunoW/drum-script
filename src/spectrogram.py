import librosa
import numpy as np

def process_audio(audio_path, sr=22050):
    """
    Carrega o áudio e detecta eventos básicos.
    Retorna o espectrograma e os tempos de ataque (onsets).
    """
    # Carrega o áudio
    y, sr = librosa.load(audio_path, sr=sr)

    # Gera espectrograma
    spectrogram = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=8000)
    log_spectrogram = librosa.power_to_db(spectrogram, ref=np.max)

    # Detecta onsets (início de batidas)
    onset_frames = librosa.onset.onset_detect(y=y, sr=sr, backtrack=True)
    onset_times = librosa.frames_to_time(onset_frames, sr=sr)

    return log_spectrogram, onset_times

if __name__ == "__main__":
    drum_audio = "temp_demucs/mdx_extra_q/drum_song/drums.wav"
    spectrogram, onsets = process_audio(drum_audio)
    print(f"Onsets detectados: {onsets}")
