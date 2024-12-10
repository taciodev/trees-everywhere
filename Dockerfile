FROM python:3.11.3-alpine3.18
LABEL maintainer="taciano.dev@outlook.com"

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho
WORKDIR /app

# Copia todos os arquivos do projeto para o contêiner
COPY . .

# Instala dependências no ambiente global
RUN apk add --no-cache netcat-openbsd && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    adduser --disabled-password --no-create-home duser && \
    mkdir -p /data/web/static /data/web/media && \
    chown -R duser:duser /app /data/web/static /data/web/media && \
    chmod -R 755 /data/web/static /data/web/media && \
    chmod -R 755 /app/scripts

# Muda para o usuário criado
USER duser

# Expondo a porta 8000 para conexões externas
EXPOSE 8000

# Define o comando de inicialização
CMD ["scripts/commands.sh"]
