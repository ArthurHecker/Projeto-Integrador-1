# Projeto-Integrador-1
Univesp

Back-end:
Emmanuel, Fábio, Firmo, Arthur

Front-end:
Matheus, Bianca, William, Irving

## Arquitetura inicial 

- `core/`: configurações principais do projeto (settings, urls, wsgi, asgi) > NÃO USAREMOS POR AGORA
- `siteapp/`: app com as páginas e rotas do site
- `templates/`: HTML base e páginas
- `manage.py`: comando principal do Django > NÃO USAREMOS POR AGORA

## Rotas de exemplo

- `/` -> Home
- `/sobre/` -> Página Sobre
- `/servicos/` -> Página Serviços
- `/contato/` -> Página Contato

## Como executar

1. Entre na sua branch:

Atualizar com as alterações das branchs*
```bash
git fetch
```
- Se for Emmanuel:
```bash
git checkout emmanuel
```

- Se for Fabio:
```bash
git checkout fabio
```

- Se for Firmo:
```bash
git checkout firmo
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Aplique migrações iniciais:

4. Rode o servidor:

```bash
python manage.py runserver
```

5. Abra no navegador:

```text
http://127.0.0.1:8000/
```
6. Aplicar as alterações no sistema


- Indicar ao git todos os arquivos alterados no sistema

```bash
git add .
```

- Aplicando todos os arquivos alterados para o github com uma mensagem de identificação

```bash
git commit -m "(Mensagem informando a alteração feita)"
```

- Enviando todas as alterações para os serviços do github
```bash
git push
```
