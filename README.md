# API Projeto Django  
[![Python 3.13.5](https://img.shields.io/badge/Python-3.13.5-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Django 5.2.8](https://img.shields.io/badge/Django-5.2.8-092E20?style=flat&logo=django&logoColor=white)](https://docs.djangoproject.com/en/6.0/)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=flat&logo=sqlite&logoColor=white)  

## Visão Geral
Este projeto visa resolver o desafio da empresa fictícia EasyCar de informatizar seu processo de aluguel de veículos. Atualmente, todos os registros de clientes, carros e contratos são realizados de forma manual, resultando em dificuldades de controle e consulta de informações.

O propósito desta API RESTful, desenvolvida em Django e Django REST Framework, é substituir essa operação manual por um sistema digital seguro e centralizado, permitindo o gerenciamento eficiente de perfis de clientes, carros e contratos de aluguel.

## Pacotes Utilizados

|Pacote|Versão|Descrição|
|:---|:---|:---|
|Django|5.2.8|Framework web principal|
|djangorestframework|latest|Toolkit para construção de APIs REST|
|django-filters|latest|Ferramenta para criação de formulários de filtro|
|drf-spectacular|latest|Geracão automética de documentação Swagger|
|requests|latest|Fazer requisições HTTP|

## Estrutura do Projeto

```
Projeto-Integrador-3/
├──README.md
├──Requirements.txt
├──Projeto integrador - Diego.pdf
└──projetointegrador3/
    ├──concessionaria/     # App
    │   ├──__init__.py
    │   ├──admin.py
    │   ├──apps.py
    │   ├──models.py       # Banco de dados em sqlite
    │   ├──serializers.py
    │   ├──tests.py
    │   └──views.py
    ├──projetointegrador3/
    │   ├──__init__.py
    │   ├──asgi.py
    │   ├──settings.py     # Configurações globais
    │   ├──urls.py         # Rotas principais
    │   └──wsgi.py
    ├──db.sqlite3
    └──manage.py
```

## Diagrama de Banco de Dados (MER + DER)
Modelo conceitual e modelo relacional abaixo:  
[![Modelos do Banco de Dados](https://img.shields.io/badge/Modelos%20do%20Banco%20de%20Dados-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MuriloLiraGoncalves/BancodeDados_DjangoProjeto3/blob/main/README.md)

## Documentação da API


## Configuração do Ambiente
Siga os passos abaixo para configurar o ambiente local.
1. **Clone o repositório:**
```bash
git clone https://github.com/Filipe-Santos-Soares/Projeto-Integrador-3.git
```
2. **Crie um ambiente virtual:**
```bash
python -m venv AmbienteVirtual
source AmbienteVirtual/bin/activate  # Linux/Mac
AmbienteVirtual\Scripts\activate     # Windows
```
3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```
4. **Aplique as migrações e inicie o servidor:**
```bash
cd projetointegrador3
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


