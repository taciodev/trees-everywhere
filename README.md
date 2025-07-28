# Trees Everywhere

Este projeto é uma aplicação web em Django que permite aos usuários registrar e rastrear o plantio de árvores ao redor do mundo.

## Como Iniciar o Projeto

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITÓRIO>
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd trees-everywhere
   ```

3. Crie e ative o ambiente virtual (opcional, caso não use Docker):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente:

   - Copie o arquivo de exemplo `.env.example` para `.env` e ajuste os valores conforme necessário.

   ```bash
   cp .env.example .env
   ```

5. Inicie os containers:

   ```bash
   docker compose up --build
   ```

## Tecnologias Utilizadas

- Django
- Python
- Docker
- Docker Compose
- PostgreSQL

## Observações

- O projeto utiliza Docker Compose para orquestrar os containers.
- As migrações do banco de dados são executadas automaticamente na inicialização.
- Um superusuário padrão é criado automaticamente com:
  - Usuário: admin
  - Senha: admin
- Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.