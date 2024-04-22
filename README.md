# Auto Watermark

O Auto Watermark é um projeto Python que automatiza a aplicação de marcas d'água em vídeos usando imagens correspondentes.

## Pré-requisitos

Antes de começar, certifique-se de ter Python instalado em sua máquina. Você pode baixar e instalar Python em [python.org](https://www.python.org/) ou em [pyenv](https://github.com/pyenv/pyenv) (recomendado).

## Preparando o ambiente do projeto

Para preparar o ambiente do projeto, siga estas etapas:

1. **Exclua os arquivos .gitkeep:**
   Antes de começar, você precisa excluir os arquivos `.gitkeep` das pastas "video" e "watermark". Esses arquivos são usados apenas para manter o controle de versão das pastas vazias e não são necessários para o funcionamento do projeto.

   ```bash
   rm video/.gitkeep
   rm watermark/.gitkeep

2. **Instale as dependências:**
   Use o comando pip para instalar todas as dependências necessárias listadas no arquivo requirements.txt.

   ```bash
   pip install -r requirements.txt

3. **Instale as dependências:**
   Para inicializar o projeto e aplicar a marca d'água nos vídeos, execute o seguinte comando:

   ```bash
   python auto_watermark.py


Isso iniciará o script auto_watermark.py, que automatizará o processo de aplicação de marcas d'água nos vídeos usando imagens correspondentes.