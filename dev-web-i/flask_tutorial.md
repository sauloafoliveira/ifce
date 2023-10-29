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


### Parte 4. Entendendo como criar **rotas** via métodos HTTP

Existem 06 (seis) métodos HTTP conhecidos:

- ```GET```: O método ```GET``` solicita a representação de um recurso específico. Requisições utilizando o método ```GET``` devem retornar apenas dados;
- ```HEAD```: O método ```HEAD``` solicita uma resposta de forma idêntica ao método ```GET```, porém sem conter o corpo da resposta;
- ```POST```: O método ```POST``` é utilizado para submeter uma entidade a um recurso específico, frequentemente causando uma mudança no estado do recurso ou efeitos colaterais no servidor;
- ```PUT```: O método ```PUT``` substitui todas as atuais representações do recurso de destino pela carga de dados da requisição;
- ```DELETE```: O método ```DELETE``` remove um recurso específico;
- ```PATCH```: O método ```PATCH``` é utilizado para aplicar modificações parciais em um recurso.

<small>Existem outros verbos: ```CONNECT```, ```OPTIONS``` e ```TRACE``` (compatibilidade indefinida).</small>

### Criando a aplicão de CRUD de lista de amigos
Faremos agora um crud (sigla para CREATE, READ, UPDATE, DELETE) de uma lista de amigos. Mais à frente, trabalharemos com uma lista de Contatos do PIX :D.

1. Crie o arquivo ```app-contatos.py``` com o código abaixo:

```python
# app_contatos.py
from flask import Flask, render_template, request, jsonify, redirect

contatos = [
    'Zezinho',
    'Luizinho'
]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('contatos.html')

@app.route('/contatos')
def listar_contatos():
    return jsonify(contatos)


@app.route('/add', methods=['POST'])
def add_contato():
    nome = request.form['nome']

    if nome:
        contatos.append(nome)
        
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)


```

No código acima, temos alguns elementos importantíssimos. Na linha de importação, observe novas funções importadas do ```Flask```: ```from flask import Flask, render_template, request, jsonify, redirect```:

- ```Flask``` possui o módulo básico para criação da microaplicação;
- ```render_template``` é a função usada para carregar arquivos htmls como resposta às requisições;
- ```request``` é um auxiliar que nos ajuda a tratar dados da requisição;
- ```jsonify``` converte a resposta da requisição para o formato ```JSON```; e por fim
- ```redirect``` é um auxiliar que nos ajuda a redirecionar a execução para uma rota especificada.

2. Em seguida, crie uma pasta ```templates``` e nela crie o arquivo ```contatos.html```
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Agendinha</title>
    <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
</head>
<body>

    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid d-flex justify-content-center">
            <a class="navbar-brand" href="#">Lista de contatos</a>
        </div>
    </nav>

      
    <div class="container pt-1">

        <h2 class="my-2">Add amiguinhos</h2>
        <form method="POST" action="/add">
            <div class="mb-3">
                <label for="nome" class="form-label">Nome do amiguinho(a)</label>
                <input type="text" class="form-control" id="nome" name="nome" />
            </div>
            <input type="submit" class="btn btn-primary" value="Cadastrar">

        </form>

        <hr>
        
        <h2 class="py-1">Minha agendinha</h2>
        <ul class="list-group"></ul>


    </div>



    <script type="text/babel">

        /// Capturar o elemento em que será renderizado o componente
        const container = document.querySelector(".list-group");

        
        /// Vincular o componete à tag
        ReactDOM.createRoot(
            container // tag para renderizar o componente
        ).render(<App />); // o Componente a ser renderizado

        function App() {

            const [contatos, setContatos] = React.useState(['Saulo Oliveira']);

            React.useEffect(() => {
                
                fetch('/contatos').then(
                    (resp) => resp.json().then(
                        (json) =>  setContatos( json )
                    )
                )
                .catch((e) => 
                    alert('Não deu pra carregar sua lista! Vai aparecer o seu amigo de todas as horas.')
                );
                
            }, []);

            return (
                <>
                    {contatos.map( (nome, id) => <Contato nome={nome} key={id} /> )}
                </>
            );
        }

        function Contato({nome}) {
            return (
                <>
                    <li className="list-group-item">
                        <div className="fw-bold">
                            <i className="bi bi-person"></i> {nome}
                        </div>
                    </li>
                </>
            );
        }

    </script>

    
</body>
</html>
```

3. Navegue via Terminal para a pasta do projeto e execute o projeto ```$ python3 app-contatos.py```. Em seguida, acesse http://localhost:8000.
 
4. Vamos trabalhar na deleção de nomes dessa agenda! Para isto, crie uma nova rota no  ```app-contatos.py```, conforme o código abaixo:

```python

@app.route('/esquecer', methods=['DELETE']) 
def del_contatos():
    nome = request.form['nome'] 
    
    if nome and (nome in contatos): # verifica se existe mesmo
        i = contatos.index(nome)    # descobre a posição do nome
        del contatos[i]             # apaga o índice

    return jsonify(contatos)
```

**Importante**: os outros métodos ```PUT``` e ```DELETE``` são constumeiramente passados via chamadas assíncronas via JS (pelo fetch, no nosso caso). Simularemos uma deleção pelo terminal. Mandando uma requisição via terminal. Vamos apagar o Zezinho. A sintaxe é a seguinte:

Sintaxe:
```shell
$ curl -X <método> <site> -d <parâmetro chave=valor>
```

```shell
$ curl -X DELETE "localhost:8000/esquecer" -d nome=Zezinho
```

### Referências

**Python Basics**. Flask REST API Tutorial. Disponível em: https://pythonbasics.org/flask-rest-api/. Acessado em 25 de out. 2023.

**MDN Contributors**. Métodos de requisição HTTP. Disponível em: https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods. Acessado em 29 de out. 2023.