#!/usr/bin/env python3

"""Hello World multi líguas

Dependendo da língua configurada no amvienteo programa exibe a mensagem 
correspondente

Como usar:

Tenha a variável LANG devidamente configurada. Ex:

    export LANG=pt_BR
    ou 
    sobrescreve a variavel no python: LANG=es_US python hello.py

Execução:

    python3 hello.py
    ou
    ./hello.py
    
"""

# metadados usando dunder
__version__ = "0.0.1"
__author__ = "Alciliano"
__license__ = "Unlicense"

# area de imports
import os  # para ler as variaveis de ambiente

# caso LANG não esteja setada, current_language = "pt_BR"
current_language = os.getenv("LANG", "pt_BR")[:5]  # as 5 primeiras letras

msg = "Hello, World! from ubuntu"

if current_language == "pt_BR":
    msg = "Olá, mundo!"
elif current_language == "it_IT":
     msg = "Ciao, mondo!"

print(msg)
