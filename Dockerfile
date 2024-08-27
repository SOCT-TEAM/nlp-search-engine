# Usando uma imagem oficial do Python como base
FROM python:3.11

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar os arquivos de requisitos para o contêiner
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo o código da aplicação para o contêiner
COPY . .

# Expor a porta que a aplicação vai usar
EXPOSE 8888

# Comando para rodar a aplicação usando Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888"]
