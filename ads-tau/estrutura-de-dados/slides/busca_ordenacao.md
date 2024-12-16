---
marp: true
paginate: true
author: Saulo Oliviera @sauloafoliveira
title: Intro to Programming
footer: Prof. **Saulo Oliveira** | [@sauloafoliveira](https://github.com/sauloafoliveira)
header: Estrutura de Dados | [Instituto Federal do Ceará](https://www.ifce.edu.br)
---

<style>

    footer {
        color: #567890;
    }
    /* Add "Page" prefix and total page number */
    section::after {
        font-size: small;
        content: 'Pág. ' attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
    }


    section {
        padding-left: 1.1em;
        padding-right: 1.1em;
    }

    /** Seções */
    section:has(> header + h1 + footer) {
        background-color: #567890;        
    }

    section:has(> header + h1 + footer) * {
        color: white;
    }

    section:has(> header + h1 + footer) h1 {
        text-align: center;
        font-variant: small-caps;
        font-size: 6em;
    }
    /***/

    blockquote {
        border: 0;
        color: initial;        
        background-color: #7986CB22;
        padding: .3em .5em;
        border-radius: .25em;
        text-align: justify;
    }

    blockquote:has(> h1) {
        padding: 0em;
        padding-bottom: .5em;
        border-bottom-left-radius: .5em;
        border-bottom-right-radius: .5em;
    }
    blockquote:has(> h1) :not(h1, strong, .MathJax) {
        margin-right: .5em;
    }
    blockquote:has(> h1) p {
        margin-left: .5em;
    }


    blockquote h1 {
        color: white;
        font-variant: small-caps;
        font-size: 1em;
        background-color: #7986CB;
        margin: 0;
        padding: .3em .5em;
        border-top-left-radius: .5em;
        border-top-right-radius: .5em;
        margin-bottom: .5em;
    }

    blockquote:has(> blockquote:has(> blockquote)) {
        background-color: #7FFFD4;        
    }
    blockquote:has(> blockquote) {
        background-color: #F4A46044;        
    }


    blockquote:has(> blockquote) blockquote {
        background-color: transparent;
        padding: 0;
    }

    /* h1:has(~ blockquote) + blockquote {
        background-color: #7986CB;
        color: #fff;
        padding: .3em .5em;
        padding-left: 3.5em;
        border-radius: .25em;
        text-align: justify;
    }

    h1:has(~ blockquote) + blockquote:before {
        content: '⚠️';
        font-size: 2em;
        position: absolute;
        left: 1em;
        
    } */

    img[center] {
        display: block;
        margin: 0 auto;
    }
    
    h1 code {
        font-size: .75em;
    }

    h4 {
        font-size: .75em;
        font-weight: 400;
        line-height: 1.7;
        font-variant: small-caps;
    }

    h2, h3, h4 {
        margin: 0;
    }
</style>

# Estrutura  de Dados
## Ordenação e Busca
#### Curso de Análise e Desenvolvimento de Sistemas
#### Última revisão: **2024.2**

![bg right:55% top:40% 80%](images/capa2.png)

---
# Ordenação e Busca
---
# Buble sort
---
# Selection sort
---
# Insertion sort
---
# Merge Sort

---
# Quick Sort

---

# Referências

- Paul Rail. **All you need to know about “Big O Notation” to crack your next coding interview.** Disponível em: https://www.freecodecamp.org/news/all-you-need-to-know-about-big-o-notation-to-crack-your-next-coding-interview-9d575e7eec4/.
- Prof. José Maria Monteiro. **INF 1010 Estruturas de Dados Avançadas: Complexidade de Algoritmos**. Disponível em: https://www.inf.puc-rio.br/~noemi/eda-19.1/complexidade.pdf.
- Prof. Reinaldo Fortes. **BCC202 - Estrutura de Dados I Aula 04: Análise de Algoritmos (Parte 1).** Disponível em: https://www.decom.ufop.br/reifortes.
- Prof. Reinaldo Fortes. **BCC202 - Estrutura de Dados I Aula 05: Análise de Algoritmos (Parte 2).** Disponível em: https://www.decom.ufop.br/reifortes.
- Programiz. **Asymptotic Analysis: Big-O Notation and More.** Disponível em: https://www.programiz.com/dsa/asymptotic-notations.
