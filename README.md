# Telemetria
Aplicação de telemetria de temperatura e umidade com arduíno e python

# Instalação do ambiente de desenvolvimento

Para instalar a aplicação, você deve clonar o projeto, entrar no diretório,e criar um virtualenv.
```
virtualenv env
```

Depois é necessário ativar o virtualenv.
```
source env/bin/activate
```

O próximo passo é instalar as dependências, para isso faça:
```
pip install -r requirements.txt
```

Por fim, o último passo é rodar a aplicação flask:
```
FLASK_APP=hello.py flask run
```
