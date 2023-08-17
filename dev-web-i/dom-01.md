
# Navegando no DOM

### Prof. Saulo Oliveira <saulo.oliveira@ifce.edu.br>

As questões que seguem não podem ter nenhuma modificação nas tags exibidas no ```body```. Use:
- ```document.querySelector( '' )```
- ```Element.children[ <id> ]```
- ```Element.firstChild```
- ```Element.lastChild```

**Questão 1.** Você recebe alguns nomes de frutas diferentes e um elemento de lista não ordenada ```<ul>```. Adicione um item de lista ```<li>``` para cada um à lista não ordenada.

```html
<html lang="en">
<body>
    <ul></ul>
  	<script>
      	const listaDeFrutas = ['tomate', 'goiaba', 'laranja'];
      	const listaNaoOrdenada = document.querySelector('ul');
  	</script>
</body>
</html>
```

Saída esperada:

<ul>
	<li>tomate</li>
 	<li>goiaba</li>
	<li>laranja</li>
</ul>

**Questão 2.** Adicione o logotipo IFCE (elemento de imagem) como um elemento filho ao elemento ```<div>``` existente.

```html
<html lang="en">
<body>
    <div></div>
  	<script>
			const imageSrc = "https://ifce.edu.br/prpi/documentos-1/semic/2018/logo-ifce-vertical.png/@@images/a8ec0f9c-0cbd-499c-a903-e034b8b8579e.png";
  	</script>
</body>
</html>
```



Saída esperada:

<img src="https://ifce.edu.br/fortaleza/comunicacao/logos/logo-horizontal-colorida_media.png/@@images/image.png" style="height: 64px">



**Questão 3.** Altere o texto no primeiro e no último elemento de item de lista em cada elemento de lista não ordenado nesta página. Altere para ```primeiro``` e ```ultimo```.

```html
<html lang="en">
<body>
    <ul>
      <li>1</li>
      <li>2</li>
      <li>3</li>
    </ul>
    <ul>
      <li>a</li>
      <li>b</li>
      <li>c</li>
    </ul>
    <ul>
      <li>I</li>
      <li>II</li>
      <li>III</li>
    </ul>
 		<script>
			
  	</script>
</body>
</html>
```



Saída esperada: 

<ul>
  <li>primeiro</li>
  <li>2</li>
  <li>último</li>
</ul>
<ul>
  <li>primeiro</li>
  <li>b</li>
  <li>último</li>
</ul>
<ul>
  <li>primeiro</li>
  <li>II</li>
  <li>último</li>
</ul>




**Questão 4.** Crie 3 classes CSS para imagens. As classes devem definir tamanhos diferentes para as imagens (ex: uma classe para imagens 50x50, outra classe para imagens 100x100 e outra para 150x150). Crie uma página contendo 10 imagens quaisquer e dois botões de uma lupa pra zoom in (+) e outra para zoom out (-). Ao clicar no botão da lupa zoom in, altere a classe das imagens para a classe que possua um maior tamanho de imagem. Ao clicar na lupa zoom out, altere a classe para uma que possua o tamanho de imagem menor.



```html
<img src="https://picsum.photos/50" /> <!-- Gera uma imagem aleatória 50x50`-->
```



Saída esperada:

<h4>Álbum de fotos aleatórias  (<button>Zoom +</button>) (<button>Zoom -)</button> </h4>
<img src="https://picsum.photos/id/101/50" /><img src="https://picsum.photos/id/102/50" /><img src="https://picsum.photos/id/103/50" /><img src="https://picsum.photos/id/104/50" />

<h4>Álbum de fotos aleatórias  (<button>Zoom +</button>) (<button>Zoom -</button>) </h4>
<img src="https://picsum.photos/id/101/100" /><img src="https://picsum.photos/id/102/100" /><img src="https://picsum.photos/id/103/100" /><img src="https://picsum.photos/id/104/100" />
