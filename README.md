# Alura Space

Este é um projeto desenvolvido durante os cursos da Alura para fortalecer o meu conhecimento em Django. O projeto consiste em uma galeria de fotografias espaciais onde os usuários podem visualizar, buscar e gerenciar fotografias.

## Funcionalidades

- Autenticação de usuários (login e logout)
- Cadastro de novos usuários
- Visualização de fotografias publicadas
- Busca de fotografias por nome
- Mensagens de feedback para ações do usuário

## Tecnologias Utilizadas

- Python
- Django
- HTML
- CSS
- JavaScript

## Como Executar o Projeto

### Pré-requisitos

- Python 3.x
- Pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)

### Passos para Configuração

1. Clone o repositório para sua máquina local:
   ```sh
   git clone https://github.com/leoAraujo20/alura-space.git

2. Navegue até o diretório do projetio:
   ```sh
   cd alura-space

3. Crie um ambiente virtual:
   ```sh
   python -m venv .venv

4. Ativar o ambiente virtual:
   ```sh
   # No Windows:
   .venv\Scripts\activate

   # No macOS e Linux:
   source .venv/bin/activate
   ```

5. Instale as dependências do projeto:
   ```sh
   pip install -r requirements.txt
   ```
6. Crie um arquivo `.env` na raiz do projeto e entre no shell interativo do django com o comando:
   ```sh
   python manage.py shell
   ```

7. Gere uma chave secreta aleatória usando o codigo:
   ```sh
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
   ```

8. Copie a saída do comando acima e cole no arquivo `.env`, ficando assim:
   ```sh
   SECRET_KEY=sua_chave_secreta_gerada_aqui
   ```

9. Realize as migrações do banco de dados:
   ```sh
   python manage.py migrate
   ```

10. Crie um superusuário para acessar o painel administrativo (opcional, mas recomendado):
      ```sh
      python manage.py createsuperuser
      ```

11. Inicie o servidor de desenvolvimento:
      ```sh
      python manage.py runserver
      ```

12. Acesse o projeto no navegador:
      ```sh
      http://127.0.0.1:8000
      ```
