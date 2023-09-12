# Escopo e tempo de vida

O escopo de uma variável define a seção de código-fonte de onde a variável pode ser acessada;

O tempo de vida de uma variável descreve quanto tempo a variável continuará a existir antes de ser destruída.



# Definições de classes

- Os **atributos** armazenam dados para uso de cada objeto;

- Os **construtores** permitem que cada objeto seja configurado adequadamente quando ele é criado;
- Os **métodos** implementam o comportamento dos objetos.

Atributos, construtores e métodos podem ser escritos em qualquer ordem mas adota-se a seguinte ordem por padrão:

```java
public class NomeDaClasse {
  
   1. Atributos
   2. Construtores
   3. Métodos
  
}
```



# Construtores



Quando usamos a keyword 'new' para criar um objeto de uma determinada classe estamos alocando um espaço na memória. Ao fazer isso, o Java requer que algumas variáveis sejam iniciadas com algum valor.

Esse ato de inicializar, ou construir, é feito pelos construtores, que são métodos - que iremos estudar mais a fundo em nossa apostila de Java logo mais.

Quando usamos a palavra-chave **new**, estamos passando para ela como um parâmetro, qual construtor deve ser executado para instanciar um objeto.



Podemos criar vários construtores. O *construtor padrão* é aquele que não recebe nenhum parâmetro. Em termos mais simples, é aquele que não recebe nenhuma informação. Ele sempre vai ser executado quando você criar um objeto.

```java
Cor azul1 = new Cor("blue");
Cor azul2 = new Cor(0, 0 , 255);
Cor azul3 = new Cor("#0000ff");
Cor preto = new Cor();
```

Esse método é chamado **construtor default**. Ao contrário do que muitos pensam, default não é padrão (embora usemos muito como se fosse). Default é omissão. Quando estamos omitindo outros construtores - que recebem parâmetro - é esse construtor 'padrão' (default) que será chamado.



**Observação:** Se na classe não houver a definição explícita de um construtor,  Java cria uma automáticamente que não possui nenhuma instrução de iniciação das variáveis.

```java
public class Aluno {
  
  String nome;
  String matricula;
  Double nota1;
  Double nota2;
  
  public static void main(String [] args) {
    Aluno joao = new Aluno();
    System.out.println(joao.nome);
    System.out.println( (joao.nota1 + joao.nota2)/2 );
  }
}
```



Ao rodar o programa acima:

```java
>> null
>> Exception in thread "main" java.lang.NullPointerException: Cannot invoke
   "java.lang.Double.doubleValue()" because "<local1>.nota1" is null
```

**Observação:** Um erro de exceção nula, ou melhor dizendo, ```java.lang.NullPointerException``` acontece quando tentamos fazer uma operação com valor ```null```. O valor ```null``` indica a ausência de dados/valores, logo, não pode ser usado para realizar operações.



Para Java, ele implementa um construtor sem parâmetros, sem intruções no dentro do seu bloco de instruções ```{}```, justamente para suprir esse tipo de *"negligência"* na definição da classe. 

```java
public class Aluno {
  
  String nome;
  String matricula;
  Double nota1;
  Double nota2;
  
  // Inxerto que Java faz para ser possível usar esta classe no sistema.
  public Aluno() {} 

  public static void main(String [] args) {
    Aluno joao = new Aluno();
  }
}
```

### Entendendo os elementos de um construtor

Construtores inicializam um objeto e:

- têm o mesmo nome das suas classes;
- armazenam valores iniciais nos campos;
- frequentemente recebem valores de parâmetros externos nesses campos.

Vejamos o exemplo que segue:

```java
public class Aluno {
  
  String nome; // tem null
  String matricula; // tem null
  Double nota1; // tem null
  Double nota2; // tem null
  
  public Aluno(String nome, String matricula) {
    this.nome = nome;
    this.matricula = matricula;
    nota1 = 0.0;
    nota2 = 0.0;
  }
  
}
```

```java
package ifce;

public class Aluno {

	String nome;
	String matricula;
	Double nota1;
	Double nota2;
	
	public Aluno() {
		nota1 = 0.0;
		nota2 = 0.0;
	}

	public Aluno(String nome, String matricula) {
		this.nome = nome;
		this.matricula = matricula;
		nota1 = 0.0;
		nota2 = 0.0;
		System.out.println("Sem notas");
	}

	public Double getMedia() {
		return (this.nota1 + this.nota2) / 2;
	}

	public Aluno(String nome, String matricula, Double nota1, Double nota2) {
		this.nome = nome;
		this.matricula = matricula;
		this.nota1 = nota1;
		this.nota2 = nota2;
	}

	public static void main(String[] args) {
		Aluno alunoX = new Aluno("Mary", "01", 7.0, 9.0);
		System.out.println( alunoX.getMedia() );

		Aluno alunoY = new Aluno("Victor", "02");
		System.out.println( alunoY.getMedia() );
	}
}
```

Note que ao criar o objeto, usamos "new Aluno();"  - logo, não passamos nenhum parâmetro. Então, chamamos claramente o construtor padrão.



## Exercícios

Cor em HTML.

Existem três maneiras de declarar cores em CSS, a saber, HEX, RGB e HSL. Embora HEX e RGB já existam há algum tempo, HSL em CSS ainda é algo relativamente novo.

Uma cor pode ser descrita em qualquer uma destas formas:

- usando uma palavra-chave, por exemplo, ```gray```, ```black```, ```red```, ```blue```, …;
- usando o sistema de coordenada-cúbica RGB, seja ela via #hexadecimal ou das notações funcionais com e/ou sem transparência, por exemplo, rgb(R,G,B) e rgba(R,G,B,A);
- usando o sistema de coordenada-cilíndrica HSL, via notações funcionais, por exemplo, hsl(H,S,L) e hsla(H,S,L,A);

O modelo de cores RGB é um modelo de cores aditivas no qual as cores primárias da luz vermelha, verde e azul são adicionadas de várias maneiras para reproduzir uma ampla gama de cores;

O nome do modelo vem das iniciais das três cores primárias aditivas, vermelho, verde e azul;
A junção de todas dá branco (255, 255, 255) e a ausência é o preto (0, 0, 0).



##### Referências

- [Rafael Guimarães Sakurai](http://lattes.cnpq.br/2777638174344195). **Construtor**, 2020. Disponível em: http://www.universidadejava.com.br/java/java-construtor/. Acessado em 12 de set. de 2023.
- Tatiane Vieira. **O que são os padrões HEX, RGB e HSL de cores?** 2021, Disponível em: https://tecnoblog.net/responde/o-que-sao-os-padroes-hex-rgb-e-hsl-de-cores/. Acessado em 12 de set. de 2023.
- https://www.javaprogressivo.net/2012/09/O-que-sao-Construtores-em-Java-Como-Criar-e-Usar.html
