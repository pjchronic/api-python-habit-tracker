# API de Gerenciamento de Hábitos

## Uma API para ajudar usuários a criar, acompanhar e analisar hábitos diários.

**Funcionalidades**:

- Autenticação de Usuário (registro, login, JWT)

- CRUD de Hábitos (criação, leitura, atualização e exclusão)

- Rastreamento de Hábitos (marcar como concluído por dia)

- Relatórios e Estatísticas (quantidade de dias consecutivos, taxa de sucesso, progresso semanal/mensal)

**Stack**:

- Backend: Python + Flask

- Banco de Dados: SQLite

- Autenticação: Flask-JWT-Extended

- ORM: SQLAlchemy

*Isso te dá prática com autenticação, banco de dados, estruturação de API e boas práticas de desenvolvimento.*

# Aqui está uma estrutura de pastas organizada para sua API REST com Flask e SQLite:

habit-tracker-api/  
│── app/  
│   ├── models/               # Definição dos modelos SQLAlchemy  
│   │   ├── __init__.py  
│   │   ├── user.py  
│   │   ├── habit.py  
│   ├── routes/               # Rotas da API  
│   │   ├── __init__.py  
│   │   ├── auth_routes.py  
│   │   ├── habit_routes.py  
│   ├── services/             # Lógica de negócios  
│   │   ├── __init__.py  
│   │   ├── auth_service.py  
│   │   ├── habit_service.py  
│   ├── utils/                # Funções auxiliares  
│   │   ├── __init__.py  
│   │   ├── jwt_helper.py  
│   ├── __init__.py           # Inicializa a aplicação Flask  
│   ├── config.py             # Configurações do Flask  
│   ├── database.py           # Conexão com SQLite  
│── migrations/               # Arquivos de migração do banco  
│── .env                      # Variáveis de ambiente  
│── requirements.txt          # Dependências do projeto  
│── run.py                    # Arquivo principal para rodar a API  
│── README.md                 # Documentação do projeto

## Explicação:

- app/models/: Contém os modelos do banco de dados.

- app/routes/: Define as rotas da API.

- app/services/: Contém a lógica de negócios.

- app/utils/: Funções auxiliares, como autenticação JWT.

- config.py: Configuração da aplicação.

- database.py: Inicializa o banco de dados SQLite.

- migrations/: Armazena as migrações do banco.

- tests/: Testes unitários para garantir a estabilidade da API.

- .env: Configurações sensíveis, como chaves secretas.

*Essa estrutura modulariza bem o código e facilita a manutenção do projeto.*



## Estrutura de banco:

Neste projeto teremos uma tabela para lidar com o registro de usuários e sua autenticação (`users`) , uma tabela para armazenar informações sobre os hábitos (`habits`) e uma última tabela para armazenar os registros dos hábitos (`habit_completions`).

#### Esquema de tabelas à ser construído...
