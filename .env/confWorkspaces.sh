#!/bin/bash

# Instalar pyenv
curl https://pyenv.run | bash

# Adicionar configuração ao arquivo de inicialização do shell
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

# Recarregar o arquivo de configuração do shell
source ~/.bashrc

# Instalar a versão específica do Python
pyenv install 3.10.13

# Definir a versão global do Python
pyenv global 3.10.13

# Instalar pacotes a partir do requirements.txt
pip install -r requirements.txt
