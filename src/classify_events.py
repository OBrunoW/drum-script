import librosa
import numpy as np

def classify_events(audio_path, onsets, sr=22050):
    """
    Classifica eventos detectados (bumbo, caixa, pratos) com base nas frequências.
    """
    y, sr = librosa.load(audio_path, sr=sr)
    classified_events = []

    for onset_time in onsets:
        # Converte o tempo para o índice no áudio
        onset_sample = int(onset_time * sr)

        # Extrai um pequeno trecho ao redor do onset
        window_size = 2048
        start = max(0, onset_sample - window_size // 2)
        end = min(len(y), onset_sample + window_size // 2)
        segment = y[start:end]

        # Calcula a FFT para análise de frequências
        spectrum = np.fft.fft(segment)
        freqs = np.fft.fftfreq(len(segment), 1 / sr)
        magnitude = np.abs(spectrum)

        # Classifica com base em frequências dominantes
        dominant_freq = freqs[np.argmax(magnitude)]
        if dominant_freq < 150:
            classified_events.append((onset_time, "bd"))  # Bumbo
        elif 150 <= dominant_freq < 250:
            classified_events.append((onset_time, "sn"))  # Caixa
        else:
            classified_events.append((onset_time, "hh"))  # Pratos

    return classified_events

if __name__ == "__main__":
    from spectrogram import process_audio

    drum_audio = "temp_demucs/mdx_extra_q/drum_song/drums.wav"
    _, onsets = process_audio(drum_audio)
    events = classify_events(drum_audio, onsets)
    print(f"Eventos classificados: {events}")
