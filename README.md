# **DrumScript** 🎵

> Projeto para transcrever partitura de bateria a partir de uma musica do youtube.

![Badge](https://img.shields.io/badge/Version-0.0.1-blue)  
![Badge](https://img.shields.io/badge/Language-Pyhton-orange)  

---

## **📌 Objetivo**  
Este projeto é uma solução automatizada para processar músicas do YouTube, isolar a bateria, e gerar partituras transcritas em formato LilyPond e PDF. Ele utiliza ferramentas modernas para separação de áudio, análise musical, e notação, permitindo a transcrição de ritmos de bateria com precisão e eficiência.  

---

### **📂 Pastas e Estrutura**

| **Pasta**            | **Descrição**             |
|----------------------|---------------------------|
| `output/`            | Saída do .mp3 .pdf e .ly. |
| `src/`               | Código fonte do projeto.  |

### **📁 Estrutura do Projeto**

```plaintext
project/
│
├── setup.sh                   # Configuração do ambiente
├── src/                       # Scripts do projeto
│   ├── spectrogram.py         # Geração de espectrogramas ou eventos básicos
│   ├── classify_events.py     # Classificação de eventos musicais
│   ├── generate_lilypond.py   # Geração de notação LilyPond
│   ├── main.py                # Integração e execução geral
│   ├── download_mp3.py        # Download do áudio (já existente)
│   ├── select_instrument.py   # Isolamento do áudio da bateria (já existente)
├── temp_demucs/               # Gerado pelo Demucs
│   ├── mdx_extra_q/
│       ├── drum_song/
│           ├── drums.wav      # Áudio isolado da bateria
├── output/                    # Saída
│   ├── drum_script.ly         # LilyPond
│   ├── drum_script.pdf        # Partitura gerada pelo LilyPond
```
---

👤 **Desenvolvido por Or1on**  
