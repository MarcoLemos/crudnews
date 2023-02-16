# Crudnews_backend

Crudnews_backend é uma micro aplicação em python para um site de notícias fictício.

Crudnews_backend utiliza arquitetura Restful gerenciada atraves do framework fastapi com o banco de dados Nosql mongoDB.


As dependências desse projeto são:
python = "^3.11"
fastapi = "^0.91.0"
uvicorn = "^0.20.0"
odmantic = "^0.9.2"
pydantic (dotenv) = "^1.10.4"

Além disso são utilizadas as bibliotecas no auxilio do desenvolvimento (group dev):
- pytest: Testes unitários
- isort: Organização dos imports
- mkdocs: Documentação
- blue: Formatação automática
- pytest-cov: Opções para verificação de cobertura dos testes
- httpie: Uso geral na consulta aos endpois
- httpx: Auxilio nos testes
- pip-audit: Verificação de integridade das bibliotecas utilizadas no projeto

**A versão base do Python desse projeto é a 3.11**

## Para realizar download do projeto:
~~~
git clone https://github.com/MarcoLemos/crudnews_backend.git
~~~

Nesse projeto foi utilizado a biblioteca poetry para criar o ambiente virtual e arquivo Makefile para organizar e simplificar os comandos.

## Para instalar o Make:

~~~
sudo apt install make
~~~

## Para instalar o poetry:

### Linux ou wsl
~~~
curl -sSL https://install.python-poetry.org | python3 -
~~~

### Powershell
~~~
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
~~~
Instruções adicionais podem ser encontradas na documentação da biblioteca. [Poetry Docs](https://python-poetry.org/docs/)

## Opcional: Se preferir criar o ambiente virtual na pasta raiz do projeto
~~~
poetry config virtualenvs.in-project true
~~~

## Para instalar as dependências 
~~~
make install
~~~

## Inicializar o ambiente virtual

~~~
make shell
~~~

## Uma vez instaladas as dependências, esse documento pode ser visualizado em um servidor local

### Pagina criada com auxilio da biblioteca mkdocs
~~~
make docs
~~~

## **Para rodar o projeto**

~~~
make run
~~~

O projeto estará acessível em (http://127.0.0.1:8000/docs)

O projeto também conta com dependências para formatação, teste e checagem de bibliotecas

## Para rodar os testes

~~~
make test
~~~

## Para rodar os testes com coverage

~~~
make cover
~~~

## Para executar a formatação 

### Para formatação automática seguindo a pep8 são utilizadas as bibliotecas blue e isort

~~~
make format
~~~

## Checagem das bibliotecas com pip-audit

~~~
make sec
~~~

## Dockerfile

Para criar a imagem
- imagem do banco e aplicação
~~~
make imgup
~~~

Parar o container

~~~
make imgs
~~~


Iniciar o container novamente

~~~
make img
~~~

## Git hooks

Esse projeto conta com configuração básica de pre commit. São executados os comandos de formatação com o comando ***make format***
O hook pode ser encontrado em:

~~~
.git/hooks/pre-commit
~~~

## Github actions

Esse projeto conta com analise integrada do github actions. São executados os comandos de testes e formatação. 
O arquivo de workflow pode ser encontrado em:

~~~
.github/workflows/continuos_integration.yml
~~~
