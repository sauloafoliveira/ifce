# Roteiro criação Flask + Api Restful



## Parte 1. Configurando um ambiente virtual do Python

Nesta seção, você construirá a estrutura do seu projeto. Você pode nomear a pasta raiz do seu projeto da maneira que desejar. 

1. Para configurar uma pasta raiz ```app_flask_01```, basta executar os comandos abaixo. Observe que o sinal de ```$``` é só pra indicar que você está num terminal:

```shell
$ mkdir app_flask_01
$ cd app_flask_01
```

A primeira linha cria uma pasta via linha de comando. Já a segunda pasta movimenta o diretório para ```app_flask_01```. A partir de então, todos os nosso arquivos deste projeto ficarão localizados nesta pasta.

2. Criar e ativar um ambiente virtual. Dessa forma, você instalará quaisquer dependências do projeto, não em todo o sistema, mas apenas no ambiente virtual do seu projeto. *Demora um pouco, tenha paciência*.

 ```shell
 $ python -m venv venv
 $ source venv/bin/activate
 ```

Pronto! A partir de agora temos um Python só nosso de modo que todas as configurações não quebrarão nem instalarão elementos desnecessários no Python utlizado no computador como um todo, e sim, somente no contido nesta pasta. Se tudo tiver dado certo, ficará um ```(venv)``` no início do terminal indicando que você está num ambinete virtual.

3. Depois de criar e ativar seu ambiente virtual, é hora de instalar o **Flask** com ```pip```. O micro framework Flask é a principal dependência que seu projeto requer. 

   ```shell
   (venv) $ python -m pip install Flask
   ```

   Depois de algum tempo e a instalação bem sucedida, temos em mão um ambiente virtual configurado e o Flask instalado na máquina. 

## Parte 2. Configurando uma aplicação Flask

1. O arquivo principal do seu projeto Flask será `app.py`. Crie `app.py` em `app_flask_01/` e adicione o seguinte conteúdo:

```python
# app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
```

Você importa o módulo `Flask`, dando ao aplicativo acesso à funcionalidade do Flask. Em seguida, você cria uma instância de aplicativo Flask chamada `app`. Em seguida, você conecta a rota da URL `"/"` à função `home()` decorando-a com `@app.route("/")`. Esta função chama a `render_template()` que é uma função Flask para obter o arquivo `home.html` e retorná-lo ao navegador. 

2. Cria uma pasta chamada ```templates``` e nela crie o arquivo chamado ```home.html``` com o código abaixo:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teste do Flask</title>
</head>
<body>
    <p>
        Oie!
    </p>
</body>
</html>
```

E assim, a estrutura de arquivos deve ficar assim:

```shell
$ tree app_flask_01
app_flask_01
├── app.py
├── templates
│   ├── home.html
└── venv
    ├── bin
```

2. Abra seu navegador em https://localhost:8000. Para ver se aparece um Oie!

### Parte 3. Criando novas páginas para novas requisições.

1. Crie novos arquivos de na pasta ```templates``` e novas rotas na sua aplicação Flask:
   1. Página de login;
   2. Página sobre nós;
   3. Página de contato.

### Referências

**Python Basics**. Flask REST API Tutorial. Disponível em: https://pythonbasics.org/flask-rest-api/. Acessado em 25 de out. 2023.