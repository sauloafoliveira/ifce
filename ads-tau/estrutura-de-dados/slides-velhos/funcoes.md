---
marp: true
paginate: true
author: Saulo Oliviera @sauloafoliveira
title: Intro to Programming
footer: Github: [@sauloafoliveira](https://github.com/sauloafoliveira)
header: Estrutura de Dados | [Instituto Federal do Ceará](https://www.ifce.edu.br)
---

<style>
    /* Add "Page" prefix and total page number */
section::after {
    font-size: small;
  content: 'Pág. ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
}

    blockquote {
        border: 0;
        padding: 0;
        color: initial;
    }

    h1:has(~ blockquote) + blockquote {
        background-color: #7986CB;
        color: #fff;
        padding: .3em .5em;
        padding-left: 3.5em;
        border-radius: .25em;
    }
    h1:has(~ blockquote) + blockquote:before {
        content: '⚠️';
        font-size: 2em;
        position: absolute;
        left: 1.75em;
        
    }
    
</style>

# Estrutura <br/> de Dados
### Modularização em Python
#### Prof. Saulo Oliveira
Análise e Des. de Sistemas

![bg right:55% top:40% 70%](capa2.png)

---

# Agenda

<style scoped>
    /* ul {
        display: grid; /* Use CSS Grid 
        grid-template-columns: 1fr 1fr;
         /* Create two equal-width columns
    } */
</style>

- Funções
- Recursão
- Bibliotecas
- Módulos
  
--- 

# Funções

> Um problema complexo pode ser simplificado quando dividido em vários problemas menores que são mais fáceis de resolver.

> **Decomposição:**
> - Redução de complexidade; 
> - Permite focalizar a atenção em um problema pequeno de cada vez; 
> - Produz melhor compreensão do todo.

**Analogia com o corpo humano:**
- > Corpo humano :standing_man: $\prec$ Sistemas :frowning_man: $\prec$ Órgãos :anatomical_heart: $\prec$ Células  :atom_symbol:  $\prec$ Móleculas :dna:.
- > Módulos $\prec$ Bibliotecas $\prec$ Funções $\prec$ Variáveis.

---

# Funções

> As funções são blocos de instruções que realizam tarefas específicas;
O código de uma função é carregado uma vez e pode ser executado quantas vezes forem necessárias.

- Os programas em geral são executados linearmente, uma linha após a outra, até o fim;
- As funções permitem a realização de desvios na execução dos programas;
- Desvios são efetuados quando uma função é chamada pelo programa principal.

---
<style scoped>
    h1 {
        margin-top: 3em;
    }
    blockquote {
        background-color: #E0E0E044;
        padding: .5em;
        border-radius: .5em;
        border: 1px solid lightgray;
    }
    blockquote strong {
        font-family: "Helvetica";
    }
    pre {
        width: 45%;
        margin-top: .5em;
    }
    pre:nth-child(2n) {
        position: relative;
        left: 51%;
        top: -26%;
    }
</style>

# Funções

Vejamos o exemplo da função ```len``` no Python.

> **Definição:** Retorna o comprimento (o número de itens) de um objeto. O argumento pode ser uma sequência (como uma ```string```, ```bytes```, ```tuple```, ```list``` ou ```range```) ou uma coleção (como um ```dict```, ```set``` ou ```frozenset```).

```python
nome = input('Digite seu nome')
l = len(nome)
print(l)
```


```python
# bultins.py -- fake
def len(s: Sized) -> int:
    contador = 0
    
    for _ in s:
        contador += 1

    return contador
```

---

<style scoped>
    ul {width: 53%; padding-left: 1em}
    pre {
        width: 35%;
        position: absolute;
        left: 57%;
        top: 22%;
    }

    pre:nth-child(2n +1) {
        top: 60%;
    }


</style>

# Anatomia de uma função (1)

- Na **definição** de funções, as variáveis recebem um nome e são chamadas de **parâmetros**;
- Funções processam algo e devolvem/retornam valores após sua execução. Para isto, utiliza-se o comando ```return``` e valores são retornados. 
- Para capturar os valores retornados, as funções devem aparecer do lado direito de uma expressão de atribuição;
- Usamos *dicas* para os sinalizarmos os tipos de valore. Usamos duas sintaxes, a saber,  ```: int``` para variáveis e ```-> int``` para funções.

```python
#somatorio.py

def somatorio(n: int) -> int:
    total = 0
    
    for i in range(n + 1):
        total += i
    
    return total

s1 = somatorio(10)
s2 = somatorio(4)
s3 = somatorio(-3)

print(f'A soma até 10 é {s1}.')
print(f'A soma até 4  é {s2}.')
print(f'A soma até -3 é {s3}.')
```

---

# Escopo de variáveis

> **Escopo**: refere-se à abrangência em que uma variável estará disponível no seu programa. Na maioria das linguagens de programação há dois escopos, a saber, o ```global``` e o ```local```.

- As variáveis que são declaradas com o **escopo global** estão disponíveis em qualquer região de seu programa, independentemente do tamanho que seu programa possua;
- Já as variáveis de **escopo local** estão disponíveis, apenas, na região em que foram declaradas.
  
> Por exemplo, uma variável que foi definida dentro de uma função existe apenas dentro daquela função. Após a execução e o encerramento de uma função, essa variável não mais existirá e, se o seu valor (conteúdo) não for armazenado em uma variável global, ele será descartado.


---
<style scoped>
    ul {padding-left: 1em;}
</style>
# Passagem de parâmetro por valor
- Parâmetro da função se comporta como uma variável local e qualquer alteração no parâmetro só é perceptível dentro da função;
- Depois que a função é finalizada, a variável que foi passada como parâmetro por valor contém o valor que tinha no momento da chamada da função.

```python
numero = int(input("Digite um numero")) # 11

def dobro(numero):
   numero = numero * 2
   return numero

dobrado = dobro(numero) 

print(dobrado)   # imprime quanto?
print(numero)    # imprime quanto?
```

---

<style scoped>
    blockquote {
        font-size: .75em;
    }
    img {
        width: 70%;
        margin: 0px auto;
        display: block;
    }
</style>

# Passagem por valor e passagem por referência

![alt text w: ](https://devblog.drall.com.br/wp-content/uploads/2016/06/pass-by-reference-vs-pass-by-value-animation.gif)

> Fonte: https://devblog.drall.com.br/excelente-imagem-animada-gif-para-ensinarrepresentar-passagem-de-parametros-por-valorcopia-e-por-referencia.

---

# Modularização

---


# Typing

> **Python** não força anotações de tipos de variáveis e funções em tempo de execução. No entanto, ferramentas de terceiros como verificadores de tipo, IDEs, linters, etc, as usam.

Considere a função abaixo:

```python
def echo(text: str, n: int) -> str:
    return text * n
```

- A função ```echo``` recebe dois argumentos que se espera ser do tipo ```str``` e do tipo ```int```, respectivamente;
- Espera-se que a função retorne uma ```str```, conforme indicado pela *dica* ```-> str```.
- O módulo ```typing``` fornece *dicas de tipo* mais avançadas;



---

# TAD de um cubo :ice_cube: 
<style scoped>
    p, pre {width: 45%;}
    pre {margin-left: 1em ;position: absolute; left: 45%;}

</style>
Desenvolva um TAD que represente um cubo. 

Inclua as funções de inicialização necessárias e as operações que retornem o tamanhos de cada lado, a sua área e o seu volume.

```python
# cubo.py
class Cube:

    def __init__(self, side: float) -> None:
        raise NotImplemented

    @property
    def side(self) -> float:
        raise NotImplemented

    def area(self) -> float:
        raise NotImplemented
    
    def volume(self) -> float:
        raise NotImplemented
```

--- 

# Referências

- Alvarenga Milton. **Excelente imagem animada (gif ) para ensinar/representar passagem de parâmetros por valor/cópia e por referência**. 2015. Disponível em: https://devblog.drall.com.br/excelente-imagem-animada-gif-para-ensinarrepresentar-passagem-de-parametros-por-valorcopia-e-por-referencia.
- Python Software Foundation. **typing — Support for type hints**. 2024. Disponível em: https://docs.python.org/3/library/typing.html
