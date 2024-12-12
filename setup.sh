#!/bin/bash

# Mensagem inicial
echo "Inicializando configuração do ambiente..."

# Limpar saídas anteriores
echo "Limpando saídas anteriores..."
rm -rf output/
rm -rf temp_demucs/
mkdir -p output

# Verifica se a pasta output existe no diretório raiz, caso contrário, cria
if [ ! -d "/output" ]; then
    echo "Criando pasta /output no diretório raiz..."
    sudo mkdir -p /output
fi

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python3 não encontrado. Instale o Python3 para continuar."
    exit 1
fi

# Instala dependências via pip
echo "Instalando dependências Python..."
pip3 install --upgrade pip
pip3 install yt-dlp pydub demucs diffq librosa numpy

# Verifica instalação do ffmpeg
if ! command -v ffmpeg &> /dev/null
then
    echo "FFmpeg não encontrado. Instalando FFmpeg..."
    
    # Detecta o sistema operacional e instala o ffmpeg
    if [ "$(uname)" == "Darwin" ]; then
        # macOS
        if ! command -v brew &> /dev/null
        then
            echo "Homebrew não encontrado. Instale o Homebrew e tente novamente."
            exit 1
        fi
        brew install ffmpeg
    elif [ "$(uname)" == "Linux" ]; then
        # Linux (Ubuntu/Debian)
        sudo apt update
        sudo apt install -y ffmpeg
    elif [[ "$(uname)" == MINGW* || "$(uname)" == CYGWIN* ]]; then
        # Windows (MINGW/CYGWIN)
        echo "Por favor, baixe e instale o FFmpeg manualmente em https://ffmpeg.org/download.html."
        exit 1
    else
        echo "Sistema operacional não suportado para instalação automática do FFmpeg."
        exit 1
    fi
fi

# Verifica instalação do LilyPond
if ! command -v lilypond &> /dev/null
then
    echo "LilyPond não encontrado. Certifique-se de instalá-lo antes de continuar."
    echo "Para instalar LilyPond, visite: https://lilypond.org"
    exit 1
fi

# Configura o PYTHONPATH para incluir a pasta raiz do projeto
export PYTHONPATH=$(pwd)

# Executa o programa principal
echo "Iniciando o programa principal..."
python3 src/main.py
