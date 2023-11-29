# Banco de dados + Endpoints (Base de dados de país)

## Parte 1. Configurando o Conector MySQL no Python

1. Ative o ambinete virtual do Python. Navegue até a pasta do projeto e digite;
   a) No Linux:

   ```shell
   source venv/bin/activate
   ```

   b) No Windows:
   ```powershell
   .\venv\Scripts\activate
   ```

2. Com o ambiente virtual ativo, instale via ```pip``` o ```mysql-connector-python```.
   ```shell
   python3 -m pip install mysql-connector-python
   ```



## Parte 2. Carregando o banco de dados do Mundo

1. Faça o donwload do arquivo SQL ```world.sql```  lá do Google Sala de Aula.

2. Abra o MySQL Workbench e configure/abra uma nova conexão com os parâmetros de conexão da lousa.

3. Crie um novo esquema abrindo o arquivo ```world.sql```;

4. Teste a seguinte *query*:
   ```sql
   SELECT Name, Code2, Continent, Population FROM Country;
   ```

## Parte 3. Testando a conexão com o banco no Python.

1. Primeiramente abra o MySQL Workbench e copie as informações acerca da conexão local. Descubra o nome de usuário e senha;
2. Crie e rode um *script* em Python com o código abaixo:

```python
# testa-conn.py
import mysql.connector

cnx = mysql.connector.connect(user='root', password='12345678',
                              host='127.0.0.1',
                              database='world')
if cnx.is_connected():
  print('Conectou!')
else:
  print('Algum problema na conexão.')
cnx.close()
```

## Parte 4. Utilizando SQL no Python

```python
# con-test2.py
import mysql.connector

cnx = mysql.connector.connect(user='root', password='12345678',
                              host='127.0.0.1',
                              database='world')
cursor = cnx.cursor()

query = '''
    SELECT Name, Code2, Continent, Population
    FROM Country
    WHERE Population > %s
'''
cursor.execute(query, (50_000, ))

print('Lista dos países com mais de 50K habitantes.')

for (Name, Code2, Continent, Population) in cursor:
    print(f'O país {Name} ({Code2}) do continente {Continent} possui {Population} habitantes.')

cnx.close()
```



### Parte 5. Criando funções utilitárias

1. Crie um arquivo ```world_db.py```. Nele ocultaremos detalhes de operaçãoes e dados sensíveis.
   

```python
# world_db.py
import mysql.connector

_cnx = None
_cursor = None

def conectar():
  _cnx = mysql.connector.connect(user='root', password='12345678',
                              host='127.0.0.1',
                              database='world')
	_cursor = cnx.cursor()

def is_conectado():
  return True if _cnx and _cnx.is_connected() else False
  
def desconectar():
  _cnx.close()

  
def listar_continentes():
  
  if not is_conectado():
    return []
  
  query = '''
    SELECT Continent
    FROM Country
    GROUP BY Continent;
	'''
  cursor.execute(query)
  
  return list(cursor)

```

2. Crie um arquivo ```app_world.py```. Nele colocaremos o flask para consumir dados do banco.
   ```python
   from flask import Flask, render_template, request, jsonify, redirect
   from world_db import conectar, desconectar, listar_continentes
   
   
   app = Flask(__name__)
   
   conectar()
   
   @app.route('/')
   def home():
     return 'Países do mundo'
   
   @app.route('/continents')
   def continentes():
     return jsonify( listar_continentes() )
   
   if __name__ == "__main__":
       app.run(host="0.0.0.0", port=80, debug=True)
   ```

   

--- prx parte

### 3.1 Criando requisições via Shell (Unix-like)

```shell
curl -X POST "localhost/registrar" -d chave="saulo@ifce.edu.br" -d nome="Saulo Oliveira"
```



### 3.1 Criando requisiçoes via PowerShell (Windows)

```powershell
$Dados = @{
	chave = "saulo@ifce.edu.br"
	nome = "Saulo Oliveira"
}

$Params = @{
	Method = "Post"
	Uri = "localhost/registrar"
	Form = $Dados
	ContentType = "application/json"
}

Invoke-RestMethod @Params
```



### Destrinchando os elementos deste conjunto de comandos

1. Dicionário de **dados** da requisição. Usa-se a sintaxe ```chave = valor```. Observe que funciona como a declaração de variáveis dentro de ```@{ }```:
   ```powershell
   $Dados = @{
   	chave = "saulo@ifce.edu.br"
   	nome = "Saulo Oliveira"
   }
   ```

2. Dicionário de **parâmetros** da requisição, similar ao dicionário de dados da requisição. Observe que dentro dos parâmetros, há a menção direta dos dados ```$Dados```:
   ```powershell
   
   $Params = @{
   	Method = "Post"
   	Uri = "localhost/registrar"
   	Form = $Dados
   	ContentType = "application/json"
   }
   ```

3. Execução do comando com os parâmetros e os dados da requisão:
   ```powershell
   Invoke-RestMethod @Params
   ```



## Final

```python
def crud(sql, cnx, cur, params):
  try:
    cur.execute(sql,  *params)
    cnx.commit()
    return True
  except:
    return False

```
   

   

## Referências

Oracle. **Connecting to MySQL Using Connector/Python**. Disponível em: https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html. Acessado em: 8 nov 2023.
