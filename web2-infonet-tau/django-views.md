---
marp: true
paginate: true
footer: Github: [:man_technologist: @sauloafoliveira](https://github.com/sauloafoliveira)
header: Desenvolvimento WEB II :earth_americas: | [Web2-InfoNet-Tau](https://github.com/sauloafoliveira/ifce/web2-infonet-tau)

---

<style>
  
  blockquote {
    color: initial;
  }


  h1 + blockquote {
    border: 0; color: #212121; font-size: .75em; padding: 0; margin-top: -.75em;
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


#  Views & Rotas :world_map: :motorway:
#### Prof. Saulo Oliveira <br/> Técnico em Informática para Internet <br /> Instituto Federal do Ceará 


---

---

# Formulários



--- 

# GET e POST

> ```GET``` e ```POST``` são os únicos métodos HTTP a serem usados ​​ao lidar com formulários.

- O formulário de login do Django é retornado usando o ```POST``` método, no qual o navegador agrupa os dados do formulário, codifica-os para transmissão, envia-os ao servidor e então recebe de volta sua resposta.

- ```GET```, por outro lado, agrupa os dados enviados em uma string e usa isso para compor um URL. A URL contém o endereço para onde os dados devem ser enviados, bem como as chaves e valores dos dados.

>  ```GET``` e ```POST``` normalmente são usados ​​para finalidades diferentes. Qualquer solicitação que possa ser usada para alterar o estado do sistema – por exemplo, uma solicitação que faça alterações no banco de dados – deve usar ```POST```. ```GET``` deve ser usado apenas para solicitações que não afetem o estado do sistema.

---

# Construindo um formulário no Django

```python
# forms.py
from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
```

--- 

# Validadores (1)

>  Os validadores podem ser úteis para reutilizar a lógica de validação entre diferentes tipos de campos.

Um validador é uma chamada que recebe um valor e gera um ```ValidationError``` se não atender a alguns critérios.


```python

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _("%(value)s is not an even number"),
            params={"value": value},
        )
```

---

# Validadores (2)

Você pode adicionar isso a um campo de modelo através do atributo ```validators```:

```python
from django.db import models


class MyModel(models.Model):
    even_field = models.IntegerField(validators=[validate_even])

```

--- 

# Validadores (3)

```python
user = CharField(
    max_length=30,
    required=True,
    validators=[
        RegexValidator(
            regex='^[a-zA-Z0-9]*$',
            message='Username must be Alphanumeric',
            code='invalid_username'
        ),
    ]
)
```

--- 

# Regex
<style scoped>
table {font-size: .5em}

table:nth-child(4) {

position: absolute;
left: 50%;
top: 33%;
}
</style>

| Padrão   | Significado                                                  |
| -------- | ------------------------------------------------------------ |
| ^        | Nega a expressão OU marca 0 início de uma string             |
| $        | Marca 0 final de uma string                                  |
| +        | Prolonga 0 caractere anterior                                |
| *        | Prolonga 0 caractere anterior, mas ele também pode não existir |
| ?        | Diz que há dúvida se 0 caractere anterior a ele existe       |
| .        | Substitui qualquer caractere (apenas um)                     |
| [A-Z]    | Procura qualquer caractere maiúsculo de A a Z                |
| [a-z]    | Procura qualquer caractere minusculo de a a Z                |
| [0-9]    | Procura qualquer dígito de 0 a 9                             |

| Padrão   | Significado                                                  |
| -------- | ------------------------------------------------------------ |
| [125]    | Procura os dígitos 1, 2 ou 5                                 |
| [^0-9]   | 01 nega a expressão a seguir, logo, procura tudo que não for número. |
| [abc]    | Procura os caracteres a, b ou c                              |
| [^A-Z]   | Procura tudo que não for letra maiúscula                     |
| [a-zA-Z] | Procura tudo que for letra                                   |
| \s       | Procura espaços                                              |
| \w       | Procura caracteres, exceto os especiais                      |
| \d       | Também procura qualquer dígito de 0 a 9                      |


--- 

# Cross-Site Request Forgery (CSRF)

> Falsificações de solicitações de sites cruzados.

Esse tipo de ataque ocorre quando um site malicioso contém um link, um botão de formulário ou algum JavaScript que se destina a executar alguma ação em seu site, usando as credenciais de um usuário conectado que visita o site malicioso em seu navegador. 

> :warning: Um tipo de ataque relacionado, ```login CSRF```, onde um site de ataque engana o navegador de um usuário para fazer login em um site com as credenciais de outra pessoa, também é coberto.

<style scoped>
  blockquote:nth-child(5) {
    color: black;
    background-color: lightyellow;
    border: 0;
    padding: .75em 1em;
  }
  blockquote:nth-child(5) code {
    color: darkorange;
  }
</style>

---

# Cross-Site Request Forgery (CSRF)

<style scoped>
  img[alt=csrf] {margin: 0px auto; display: block; width: 70%;}

  a[href*='writesoftwarewell'] {font-size:.75em;
    padding: .1em .25em;
  }
  a[href*='writesoftwarewell']::before {
    content: 'Fonte:  ';
    text-decoration: none;
    color: initial;
    background-color: white;
    
  }
</style>

![csrf](https://www.writesoftwarewell.com/content/images/2023/02/csrf_explanation-2.png)


https://www.writesoftwarewell.com/how-csrf-attack-works-cross-site-request-forgery/

---

# Referências

- Django. **Working with forms**. Disponível em: https://docs.djangoproject.com/en/5.0/topics/forms/. Acessado em 20 de março de 2024.
---