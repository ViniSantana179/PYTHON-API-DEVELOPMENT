Configuração do Ambiente Virtual e Instalação do FastAPI

Este guia fornece instruções para configurar um ambiente virtual em Python e instalar o framework FastAPI.

Requisitos

Certifique-se de ter o Python 3.7 ou superior instalado no seu sistema. Você pode verificar a versão instalada executando o seguinte comando:

python --version

Ou, dependendo do seu sistema:

python3 --version

Passo 1: Criar o Ambiente Virtual

Abra o terminal ou prompt de comando.

Navegue até o diretório onde você deseja criar o ambiente virtual.

Execute o seguinte comando para criar um ambiente virtual chamado venv:

python -m venv venv

Ou, se o comando acima não funcionar, tente:

python3 -m venv venv

Após a criação, ative o ambiente virtual:

Windows:

venv\Scripts\activate

Linux/MacOS:

source venv/bin/activate

Após a ativação, você verá o prefixo (venv) no início do seu terminal, indicando que o ambiente virtual está ativo.

Passo 2: Atualizar o pip (opcional)

Antes de instalar pacotes, é uma boa prática atualizar o pip para a versão mais recente:

pip install --upgrade pip

Passo 3: Instalar o FastAPI

Instale o FastAPI e um servidor ASGI (Uvicorn) com o comando:

pip install fastapi uvicorn

Confirme a instalação verificando as versões:

pip show fastapi uvicorn

Passo 4: Testar a Instalação

Crie um arquivo chamado main.py com o seguinte conteúdo:

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

Execute o aplicativo com o Uvicorn:

uvicorn main:app --reload

Abra seu navegador ou ferramenta de requisições HTTP (como o Postman ou cURL) e acesse:

http://127.0.0.1:8000: Para ver a resposta "Hello World".

http://127.0.0.1:8000/docs: Para acessar a documentação interativa do FastAPI.

Passo 5: Desativar o Ambiente Virtual

Após finalizar, você pode desativar o ambiente virtual com:

deactivate
