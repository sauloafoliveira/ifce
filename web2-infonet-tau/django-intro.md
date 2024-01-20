---
marp: true
paginate: true
footer: Github: [:man_technologist: @sauloafoliveira](https://github.com/sauloafoliveira)
header: Desenvolvimento WEB II :earth_americas: | [Web2-InfoNet-Tau](https://github.com/sauloafoliveira/ifce/web2-infonet-tau)

---

<style>
    
  h1 {
       color: darkgreen;
  }
    h2 {
  background: -webkit-linear-gradient(#81ADBB, #1A5C71);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
    }
</style>

<style scoped>
h1 {
  font-size: 3em;
  position: initial;
}

br::after {
    color: grey;
}
</style>


#  Django :snake: :earth_americas:
#### Prof. Saulo Oliveira <br/> Técnico em Informática para Internet <br /> Instituto Federal do Ceará 


---

# Django

Para iniciar a instalação, basta digitar no console:
```sh
$ python -m pip install Django
```

Após a instalação, para verificar, tente rodar o Python no modo interativo e faça a importação do módulo do ```django``` e veja se consegue obter a string da versão instalada.

```python
$ python
Python 3.8.5 (default, Sep  4 2020, 02:22:02) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> print(django.get_version())
4.2.7 
```

---

# Criando um projeto

Para criar um projeto, usaremos o comando
```django-admin``` com as opções ```startproject```,
seguido do nome do projeto ```mysite```.

> ```shell
> $ django-admin startproject mysite
> ```

Esse comando vai criar uma pasta chamada ```mysite```
 no diretório atual, como a estrutura ao lado.
 
O diretório raiz ```mysite``` é um contêiner para o seu projeto. Seu nome não importa para o Django.


<style scoped>
    blockquote {
        padding: 0;
        border: 0;
        width: 58%;
    }
    blockquote:nth-child(2n+1) {
        width: 32%;
        position: absolute;
        top: 28%;
        right: 6%;
    }
</style>    

> ```shell
> mysite/
>     manage.py
>     mysite/
>         __init__.py
>         settings.py
>         urls.py
>         asgi.py
>         wsgi.py
> ```

---

# Estrutura de um projeto
<style scoped>
    blockquote {
        padding: 0;
        border: 0;
        width: 32%;
        position: absolute;
        top: 13%;
        right: 8%;
    }
</style>    

> ```shell
> mysite/
>     manage.py
>     mysite/
>         __init__.py
>         settings.py
>         urls.py
>         asgi.py
>         wsgi.py
> ```

O diretório raiz ```mysite``` é um contêiner para o seu
projeto. Seu nome não importa para o Django.

- ```manage.py```: um utilitário de linha de
 comando para inteagir com esse projeto.
- O diretório interno ```mysite/```  é o pacote do seu
 projeto que você vai precisar usar para importar coisas do seu interior.
- ```mysite/__init__.py```: um arquivo vazio que diz ao Python que este diretório deve ser considerado um pacote Python;
- ```mysite/settings.py```: configurações para este projeto Django;
- ```mysite/urls.py```: as declarações de URLs (rotas) para este projeto Django.

---

# Rodar para testar

Vamos verificar se o seu projeto Django funciona. Mude para o diretório externo do ```mysite``` , se você ainda não o fez, e execute os seguintes comandos:

```shell
$ python manage.py runserver
```

```shell
>>> Watching for file changes with StatReloader
>>> Performing system checks...
>>>
>>> System check identified no issues (0 silenced).
>>>
>>> January 15, 2024 - 12:29:17
>>> Django version 4.2.7, using settings 'mysite.settings'
>>> Starting development server at http://127.0.0.1:8000/
>>> Quit the server with CONTROL-C.
```