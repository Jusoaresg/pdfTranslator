# Pdf Translator (Tradutor de pdf)

Pdf Translator é um programa CLI que tem o objetivo de traduzir PDFs de inglês para português.

## Instalação

Para instalar todas as dependencias do projeto, utilize esse comando:

```bash
pip install -r requirements.txt
```

Para rodar o projeto:

```bash
python main.py
```

## Como funciona

Esse projeto funciona da seguinte maneira:

 1. Primeiramente ele faz uma checagem de erros em cada página do arquivo pdf, normalmente para problemas de imagens não suportadas. (Consegui resolver esse problemas abrindo o pdf no libreoffice e exportando ele novamente como pdf)

 2. Depois ele começa a fazer uma conversão de pdf para docx, para facilitar a troca dos textos.

 3. Após isso, ele começa a verificar cada parágrafo dentro desse docx, faz uma verificação se é uma imagem, string vazia ou numero, e então troca cada parágrafo com a tradução feita pelo google tradutor.

## Dependencias
Python e pip. <br>
Pacotes do pip em Requirements.txt

## O que falta fazer

TO-DO:
 - [ ] Retornar o arquivo como um pdf novamente.
 - [ ] Traduzir do inglês para diversas linguagens.
