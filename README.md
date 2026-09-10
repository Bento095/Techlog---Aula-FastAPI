
# 🚀 Techlog Solutions - CRM

Um sistema de CRM (Customer Relationship Management) simples e robusto desenvolvido com **FastAPI**, **Jinja2** e **SQLite**. O projeto conta com rotas de autenticação, controle de sessão via cookies, gerenciamento de clientes e testes automatizados.

Projeto desenvolvido durante os estudos de FastAPI na Alura.

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3.14+](https://www.python.org/)** — Linguagem principal
- **[FastAPI](https://fastapi.tiangolo.com/)** — Framework web moderno e de alta performance
- **[Jinja2](https://jinja.palletsprojects.com/)** — Motor de templates para renderização no servidor (SSR)
- **[SQLite3](https://www.sqlite.org/)** — Banco de dados relacional leve
- **[Uvicorn](https://www.uvicorn.org/)** — Servidor ASGI
- **[Pytest](https://docs.pytest.org/) & [Pytest-Asyncio](https://pytest-asyncio.readthedocs.io/)** — Testes unitários e assíncronos

---

## ✨ Funcionalidades

- 🔒 **Autenticação & Controle de Acesso:**
  - Cadastro de novos usuários com validação.
  - Login com autenticação via banco de dados e suporte a conta administrativa.
  - Middleware de proteção de rotas via Cookie de sessão (`session_token`).
  - Rota de Logout para encerramento de sessão.

- 👥 **Gestão de Clientes:**
  - Listagem e cadastro de clientes no banco SQLite.
  - Padrão de projeto *Repository* para isolamento do acesso aos dados.

- 🎨 **Interface Web:**
  - Layout dinâmico com Jinja2.
  - Estilização e scripts centralizados na pasta de estáticos.

---

## 📁 Estrutura do Projeto

```text
Techlog---Aula-FastAPI/
├── app/
│   ├── banco_de_dados/          # Conexão e repositórios (UsuarioRepositorio, ClienteRepositorio)
│   ├── rotas/                   # Endpoints da aplicação (login, registro, cliente)
│   ├── autenticacao_middleware.py # Middleware de verificação de token/cookie
│   ├── dependencias.py          # Injeção de dependências do FastAPI
│   └── main.py                  # Inicialização do app e rotas principais
├── static/                      # Arquivos CSS e JavaScript
├── templates/                   # Páginas HTML (Jinja2)
├── test/                        # Suíte de testes automatizados
└── requirements.txt             # Dependências do projeto

```

---

## 🔧 Como Executar o Projeto

### Pré-requisitos

* Python 3.10 ou superior instalado.
* Git instalado.

### Passo a passo

1. **Clone o repositório:**
```bash
git clone [https://github.com/SEU-USUARIO/Techlog---Aula-FastAPI.git](https://github.com/SEU-USUARIO/Techlog---Aula-FastAPI.git)
cd Techlog---Aula-FastAPI

```


2. **Crie e ative um ambiente virtual:**
```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou no Windows: .venv\Scripts\activate

```


3. **Instale as dependências:**
```bash
pip install -r requirements.txt

```


*(Caso não tenha um `requirements.txt`, você pode instalar os pacotes com: `pip install fastapi uvicorn jinja2 pytest pytest-asyncio`)*
4. **Inicie o servidor de desenvolvimento:**
```bash
uvicorn app.main:app --reload

```


5. **Acesse no navegador:**
Abra [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 Como Executar os Testes

O projeto utiliza `pytest` com suporte a testes assíncronos (`pytest-asyncio`). Para rodar a suíte completa de testes:

```bash
pytest

```

Para rodar um teste específico:

```bash
pytest test/banco_de_dados/test_cliente_repositorio.py -k test_listar_clientes_retorna_lista_vazia

```

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais. Sinta-se à vontade para clonar, estudar e modificar!

```
