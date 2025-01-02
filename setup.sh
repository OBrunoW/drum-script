#!/bin/bash

# Mensagem inicial
echo "Inicializando configuração do ambiente..."

# Limpar saídas temporárias
echo "Limpando arquivos temporários..."
rm -rf temp_downloads/

# Garantir que a pasta de saída existe
mkdir -p output

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python3 não encontrado. Instale o Python3 para continuar."
    exit 1
fi

# Criação de um ambiente virtual
echo "Criando ambiente virtual Python..."
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate

# Atualizar o pip no ambiente virtual
echo "Atualizando o pip no ambiente virtual..."
pip install --upgrade pip

# Instalar dependências
echo "Instalando dependências Python..."
pip install yt-dlp pydub demucs diffq librosa numpy

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

# Configura o PYTHONPATH para incluir a pasta raiz do projeto
export PYTHONPATH=$(pwd)

# Executa o programa principal
echo "Iniciando o programa principal..."
python3 src/main.py

# Desativar o ambiente virtual após a execução
deactivate

echo "Processo concluído! Os arquivos de saída estão na pasta 'output/'."
