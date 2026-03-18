# Projeto-Integrador-1
Univesp

Back-end:
Emmanuel, Fábio, Firmo, Arthur

Front-end:
Matheus, Bianca, William, Irving

## Arquitetura inicial (simples)

Este projeto foi organizado para iniciantes em Django, com apenas o essencial:

- `core/`: configurações principais do projeto (settings, urls, wsgi, asgi)
- `siteapp/`: app com as páginas e rotas do site
- `templates/`: HTML base e páginas
- `manage.py`: comando principal do Django

Estrutura:

```text
Projeto-Integrador-1/
├── core/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── siteapp/
│   ├── __init__.py
│   ├── apps.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   └── siteapp/
│       ├── contato.html
│       ├── home.html
│       ├── servicos.html
│       └── sobre.html
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Rotas de exemplo

- `/` -> Home
- `/sobre/` -> Página Sobre
- `/servicos/` -> Página Serviços
- `/contato/` -> Página Contato

## Como executar

1. Ative e crie o ambiente virtual:

```bash
python -m venv venv
```

```bash
source venv/bin/activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Aplique migrações iniciais:

```bash
python manage.py migrate
```

4. Rode o servidor:

```bash
python manage.py runserver
```

5. Abra no navegador:

```text
http://127.0.0.1:8000/
```

