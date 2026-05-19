# Checkout Commerce Microservice

Microserviço de processamento de checkout para plataforma de e-commerce, desenvolvido com FastAPI, PostgreSQL e integração com múltiplos serviços externos.

## 📋 Visão Geral

Este projeto implementa um serviço robusto de checkout que gerencia:

- **Processamento de Pedidos**: Validação e criação de pedidos de compra
- **Gerenciamento de Inventário**: Verificação de disponibilidade de produtos
- **Processamento de Pagamentos**: Integração com serviço de pagamento
- **Persistência de Dados**: Armazenamento seguro em PostgreSQL
- **Comunicação Assíncrona**: Requisições não-bloqueantes entre serviços

## 🏗️ Arquitetura

### Stack Tecnológico

- **Framework**: FastAPI 0.119.0
- **Runtime**: Python 3.13+
- **Database**: PostgreSQL 16
- **ORM**: SQLAlchemy 2.0+
- **Gerenciador de Pacotes**: UV
- **Servidor**: Uvicorn 0.37.0
- **Testes de Serviços**: WireMock

### Estrutura de Pastas

```
python-microservice/
├── app/
│   ├── main.py                    # Aplicação FastAPI principal
│   ├── client_manager.py          # Gerenciador de clientes HTTP
│   ├── checkout/                  # Módulo de checkout
│   │   ├── router.py             # Rotas da API
│   │   ├── checkout_model.py     # Modelos de dados
│   │   ├── checkout_request.py   # Schemas de requisição
│   │   └── checkout_process.py   # Lógica de processamento
│   └── infra/                     # Camada de infraestrutura
│       ├── database.py           # Configuração do banco
│       └── client/               # Clientes HTTP
│           ├── payment_client.py
│           ├── inventory_client.py
│           └── order_client.py
├── wiremock/                      # Configurações dos mocks
│   ├── payment/
│   ├── inventory/
│   └── order/
├── docker-compose.yml             # Orquestração de serviços
├── pyproject.toml                 # Configuração do projeto
├── uv.lock                        # Lock de dependências
├── run-dev.sh                     # Script de execução
└── request.http                   # Exemplos de requisições HTTP
```

## 🚀 Iniciando o Projeto

### Pré-requisitos

- Python 3.13+
- UV (gerenciador de pacotes)
- Docker & Docker Compose
- PowerShell ou terminal Unix

### Instalação e Execução

#### 1️⃣ Clonar/Navegar até o Repositório

```powershell
cd C:\Projetos\python-microservice
```

#### 2️⃣ Criar Ambiente Virtual com UV

```powershell
uv venv
```

Isso criará um diretório `.venv` com o ambiente isolado.

#### 3️⃣ Ativar o Ambiente Virtual

**PowerShell:**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Git Bash / Unix:**
```bash
source .venv/bin/activate
```

> **Dica**: Se receber erro de permissão no PowerShell, execute:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

#### 4️⃣ Instalar Dependências

```powershell
uv sync
```

Isso instalará todas as dependências definidas no `uv.lock` de forma determinística.

#### 5️⃣ Iniciar Serviços de Infraestrutura

```powershell
docker-compose up -d
```

Isso iniciará:
- **PostgreSQL** (porta 5442)
- **Payment Service Mock** (porta 8081)
- **Inventory Service Mock** (porta 8082)
- **Order Service Mock** (porta 8083)

Aguarde alguns segundos para os containers ficarem saudáveis:
```powershell
docker-compose ps
```

#### 6️⃣ Executar a Aplicação

**Opção 1 - Via uvicorn direto:**
```powershell
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Opção 2 - Via script:**
```bash
bash run-dev.sh
```

#### 🎯 Resultado Esperado

Você verá:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

A API estará disponível em: **http://localhost:8000**

### ⚡ Resumo - Comandos Sequenciais

```powershell
# Navegar ao projeto
cd C:\Projetos\python-microservice

# Criar ambiente virtual
uv venv

# Ativar ambiente
.\.venv\Scripts\Activate.ps1

# Instalar dependências
uv sync

# Iniciar infraestrutura
docker-compose up -d

# Executar aplicação
python -m uvicorn app.main:app --reload
```

## 📡 API Endpoints

### Health Check

```http
GET /health
```

Retorna o status da aplicação e URL do serviço de pagamento.

### Processar Checkout

```http
POST /checkout/process
Content-Type: application/json

{
  "customer_id": "123",
  "items": [
    {
      "product_id": "ABC",
      "quantity": 2,
      "price": 99.99
    }
  ],
  "payment_method": "credit_card"
}
```

**Response (200):**
```json
{
  "order_id": "ORD-123456",
  "status": "completed",
  "total": 199.98,
  "timestamp": "2026-05-18T22:00:00Z"
}
```

### Exemplos de Requisições

Veja o arquivo `request.http` para mais exemplos que podem ser executados no VS Code com a extensão REST Client.

## 🔧 Variáveis de Ambiente

Create a `.env` file na raiz do projeto:

```env
APP_HOST=0.0.0.0
APP_PORT=8000

DATABASE_URL=postgresql://postgres:postgres@localhost:5442/checkout_db

PAYMENT_SERVICE_URL=http://localhost:8081
INVENTORY_SERVICE_URL=http://localhost:8082
ORDER_SERVICE_URL=http://localhost:8083
```

## 🗄️ Database

### Migrations

As migrations são gerenciadas com Alembic. Para criar uma nova migration:

```powershell
# Gerar migration automática
alembic revision --autogenerate -m "Descrição da mudança"

# Aplicar migrations
alembic upgrade head
```

## 🧪 Testando a Aplicação

### Swagger UI

Acesse a documentação interativa em:
```
http://localhost:8000/docs
```

### ReDoc

Documentação alternativa:
```
http://localhost:8000/redoc
```

### Testes Manuais

Use o arquivo `request.http` com a extensão REST Client do VS Code, ou tools como Postman/Insomnia.

## 🛑 Parar a Aplicação

```powershell
# Parar containers Docker
docker-compose down

# Desativar ambiente virtual
deactivate
```

## WireMock — Mocks de Serviços Externos

Este projeto usa WireMock para simular os serviços externos (payment, inventory e order) durante desenvolvimento e testes.

- **Propósito**: permitir testes e desenvolvimento offline, controlando respostas (sucesso, erro, erros 500, fundos insuficientes, etc.) sem depender dos serviços reais.
- **Local dos arquivos**: os mappings e respostas ficam em `wiremock/` na raiz do projeto. Exemplos:
  - [wiremock/payment/mappings/success.json](wiremock/payment/mappings/success.json)
  - [wiremock/inventory/mappings/success.json](wiremock/inventory/mappings/success.json)
  - [wiremock/order/mappings/success.json](wiremock/order/mappings/success.json)

- **Portas padrão usadas**:
  - Payment mock: `http://localhost:8081`
  - Inventory mock: `http://localhost:8082`
  - Order mock: `http://localhost:8083`

- **Como iniciar os mocks**: o `docker-compose.yml` já inclui os containers de mock. Para subir apenas os mocks ou todo o ambiente, execute:

```powershell
docker-compose up -d
```

Verifique o status com:

```powershell
docker-compose ps
docker-compose logs <service-name>
```

- **Endpoint administrativo do WireMock**: cada mock expõe a API administrativa em `http://localhost:<port>/__admin`. Por exemplo:

```
http://localhost:8081/__admin/mappings
```

- **Adicionar/alterar mappings localmente**:
  1. Crie ou edite um arquivo JSON dentro de `wiremock/<service>/mappings/` seguindo o formato do WireMock (mapping + resposta em `__files` quando necessário).
  2. Reinicie o container do mock para que ele recarregue os mappings montados pelo volume:

```powershell
docker-compose restart <service-name>
```

- **Testando as variações**: use os arquivos em `wiremock/*/mappings/` para simular cenários diferentes (ex.: `payment` com `insufficient_fund.json` ou `server_500.json`). O arquivo `request.http` contém exemplos que apontam para os endpoints dos mocks.

- **Dica**: após mudar mappings com frequência, pode ser útil limpar o container e subir novamente:

```powershell
docker-compose down
docker-compose up -d
```

## 📦 Dependências

| Pacote | Versão | Propósito |
|--------|--------|----------|
| fastapi | >=0.119.0 | Framework web assíncrono |
| uvicorn | >=0.37.0 | Servidor ASGI |
| sqlalchemy | >=2.0.44 | ORM para banco de dados |
| asyncpg | >=0.30.0 | Driver PostgreSQL assíncrono |
| httpx | >=0.28.1 | Cliente HTTP assíncrono |
| alembic | >=1.17.0 | Gerenciamento de migrations |
| python-dotenv | >=1.1.1 | Carregamento de variáveis de ambiente |
| greenlet | >=3.2.4 | Suporte a concorrência |

## 🔒 Boas Práticas Implementadas

- ✅ **Async/Await**: Toda a aplicação é assíncrona para melhor performance
- ✅ **Gerenciamento de Lifespan**: Startup e shutdown controlados
- ✅ **Separação de Responsabilidades**: Camadas bem definidas (router, service, infra)
- ✅ **Clientes HTTP Pool**: Reutilização de conexões com `client_manager`
- ✅ **Type Hints**: Tipagem completa para melhor IDE support e validação
- ✅ **Health Checks**: Verificação de integridade da aplicação
- ✅ **Variáveis de Ambiente**: Configuração externalizada

## 🐛 Troubleshooting

### Erro: "Port already in use"

Se a porta 8000 já está em uso:
```powershell
python -m uvicorn app.main:app --reload --port 8001
```

### Erro: "Database connection refused"

Verifique se os containers estão rodando:
```powershell
docker-compose logs postgres
```

### Erro: "ModuleNotFoundError"

Certifique-se de que o ambiente virtual está ativo e as dependências foram instaladas:
```powershell
uv sync
```

## 📚 Referências

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [AsyncPG](https://magicstack.github.io/asyncpg/)
- [UV Package Manager](https://github.com/astral-sh/uv)

## 📄 Licença

MIT License - Veja LICENSE para detalhes.

## 👤 Autor

Desenvolvido como parte do curso completo de microserviços em Python.

---

**Última atualização**: 2026-05-18