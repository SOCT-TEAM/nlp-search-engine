# Setup Guide

This guide provides a step-by-step process to set up the `nlp-search-engine` repository.

## Prerequisites

Before proceeding with the setup, ensure that you have the following:

- Python 3.x installed on your system
- Access to the internet

## Step 1: Clone the Repository

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command to clone the repository:

    ```
    git clone git@github.com:felipebpl/nlp-search-engine.git
    ```

## Step 2: Create the `pg_env` Virtual Environment

1. Navigate to the cloned repository's directory:

    ```
    cd nlp-search-engine
    ```

2. Create a virtual environment named `pg_env` by running the following command:

    ```
    python3 -m venv pg_env
    ```

3. Activate the virtual environment:

    - For Windows:

      ```
      pg_env\Scripts\activate
      ```

    - For macOS/Linux:

      ```
      source pg_env/bin/activate
      ```

## Step 3: Install the Requirements

1. Ensure that you are in the `nlp-search-engine` directory and the `pg_env` virtual environment is activated.

2. Run the following command to install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Step 4: Run `pg.py` to Retrieve Essays

1. Make sure you are still in the `nlp-search-engine` directory and the `pg_env` virtual environment is activated.

2. Run the following command to execute the `pg.py` script:

    ```
    python pg.py
    ```

    This script will retrieve the essays and store them in a suitable format.

Congratulations! You have successfully set up the `nlp-search-engine` repository. You can now explore and utilize the essays as per your requirements.

## How to Run the FastAPI Application

1. Certifique-se de que você concluiu todas as etapas de configuração no guia anterior e que o ambiente virtual `pg_env` está ativado.

2. No terminal, navegue até o diretório do projeto `nlp-search-engine`.

3. Execute o servidor FastAPI com o Uvicorn:

    ```
    uvicorn main:app --host 0.0.0.0 --port 8888
    ```

    Substitua `8888` por qualquer porta disponível de sua escolha.

4. Agora você pode acessar o servidor via `http://10.103.0.28:8888/query` em seu navegador ou através de ferramentas como o Postman.

## How It Works

A aplicação FastAPI implementa um sistema de recomendação baseado em TF-IDF (Term Frequency-Inverse Document Frequency). Todos os essays de Paul Graham foram extraídos e armazenados em arquivos `.txt`, que são processados para calcular os vetores TF-IDF. Quando uma consulta é feita via `/query`, a aplicação calcula a similaridade da consulta com os documentos e retorna os mais relevantes.

- **TF-IDF**: Calcula a relevância dos termos no contexto dos documentos.
- **Busca**: Utiliza a similaridade de cosseno para comparar a consulta com os documentos processados, retornando os documentos mais relevantes.
  
## Where You Got Data From

Os dados foram obtidos dos essays disponíveis no site [Paul Graham](https://www.paulgraham.com/). O script `pg.py` foi utilizado para extrair os textos dos essays diretamente do site e salvá-los em arquivos `.txt` no diretório `essays/`.

## How to Test

Aqui estão três exemplos de testes que você pode realizar para verificar o funcionamento da aplicação:

1. **Teste com 10 resultados:**
   - **URL**: `http://10.103.0.28:8888/query?query=users`
   - **Descrição**: Esta consulta retorna 10 resultados relevantes relacionados ao termo "users", que é um tema comum nos essays de Paul Graham.

2. **Teste com menos de 10 resultados:**
   - **URL**: `http://10.103.0.28:8888/query?query=love`
   - **Descrição**: Esta consulta utiliza um termo raro que aparece em menos de 10 documentos, resultando em um número menor de resultados (2).

3. **Teste com resultado não óbvio:**
   - **URL**: `http://10.103.0.28:8888/query?query=writing`
   - **Descrição**: A consulta por "writing" retorna resultados que não são imediatamente aparentes como relevantes para startups ou negócios, mas que abordam a simplicidade e qualidade da escrita como um motor para criatividade e comunicação.

