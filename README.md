# Trees Everywhere

Este projeto é uma aplicação web em Django que permite aos usuários registrar e rastrear o plantio de árvores ao redor do mundo. Foi criado como parte de um processo seletivo para a Youshop em 2024.

## Como Iniciar o Projeto

1. **Clone o repositório:**

   ```bash
   git clone <URL_DO_REPOSITÓRIO>
   ```

2. **Navegue até o diretório do projeto:**:

   ```bash
   cd trees-everywhere
   ```

3. **Crie e ative o ambiente virtual:**:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. **Inicie os containers:**:

   ```bash
   docker compose up --build 
   ```

## Tecnologias Utilizadas

* Django
* Python
* Docker
* Docker Compose
* PostgreSQL (assumindo, baseado na estrutura)

## Observações

* O projeto utiliza Docker Compose para orquestrar os containers.
* As migrações do banco de dados são executadas por um script dentro do container.
* Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.