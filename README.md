# i3gs DJANGO-BASE

## Informações

- A aplicação foi construída com python 3
- Autenticação: Cada sessão dura 2 horas, isso pode ser mudado no arquivo de configuração do projeto

## Primeiros passos

Crie um ambiente virtual

```sh
python -m venv projectbase
```

Ative a venv e atualize o pip

```sh
source projectbase/bin/activate
```

```sh
python -m pip install --upgrade pip
```

Clone o repositório

```sh
git clone https://gitlab.com/i3data/django-base.git
```

Entre na pasta do projeto

```sh
cd django-base
```

Instale as dependências
```sh
pip install -r requirements.txt
```

Faça a migração

> Por padrão aplicação procura por um banco com  nome: dbbase, user: djangobase, password: djangobase (Isso pode ser modificado)

```sh
python manage.py makemigrations
```

Execute a aplicação

```sh
python manage.py runserver
```
Agora acesse a aplicação em: http://localhost:8000


## Começar uma nova aplicação

Configure o email de recuperação de senha no arquivo [settings.py](./i3gs_base/settings.py)

```py
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com' #Servidor SMTP
EMAIL_HOST_USER = 'seuemail@email.com'
EMAIL_HOST_PASSWORD = 'passwordEmail'
EMAIL_PORT = 587
```
