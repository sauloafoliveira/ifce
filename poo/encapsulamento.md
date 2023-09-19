## Encapsulamento

Encapsulamento é uma técnica utilizada para restringir o acesso a variáveis (atributos), métodos ou até à própria classe. Os detalhes da implementação ficam ocultos ao usuário da classe, ou seja, o usuário passa a utilizar os mé- todos de uma classe sem se preocupar com detalhes sobre como o método foi implementado internamente.

<div style="margin-left: 25%; font-size: small; text-align: justify;">
Para facilitar o entendimento, façamos uma analogia com um carro. Para dirigir um carro uma pessoa não precisa conhecer os detalhes sobre como funciona o motor ou os demais componentes dele. Um motorista não precisa saber o que acontece internamente no carro quando ele acelera ou quando troca de marcha. Para dirigir ele precisa apenas saber como dirigir o carro utilizando pedais de acelerador, freio e embreagem, volante e alavanca de câmbio. Esses componentes encapsulam toda a complexidade existente no carro sob a ótica do motorista que o utiliza. (CARVALHO, V. A.; TEIXEIRA, G. F., 2012).
</div>



Para isso, precisamos qualificar os membros de uma classe a fim de modificar o nível de acesso deles, sejam atributos,  métodos e até mesmo às classes. São três os possíveis qualificadores de acesso em Java:

- ```public``` ( público ). Indica que o método ou o atributo são acessíveis por qualquer classe, ou seja, que podem ser usados por qualquer classe, indepen- dentemente de estarem no mesmo pacote ou estarem na mesma hierarquia;
- ```private``` ( privado ): Indica que o método ou o atributo são acessíveis ape- nas pela própria classe, ou seja, só podem ser utilizados por métodos da própria classe;
- ```protected``` ( protegido ): Indica que o atributo ou o método são acessíveis pela própria classe, por classes do mesmo pacote ou classes da mesma hierarquia (estudaremos hierarquia de classes quando tratarmos de herança).

**Observação:** Quando omitimos o qualificador de acesso, o atributo, método ou classe são considerados ```protected``` por padrão.

A encapsulação de dados com o código que os manipula em classes é uma das principais vantagens da Orientação a Objeto. No sentido de não quebrar a encapsulação, é muito importante que os membros de uma classe (atributos e métodos) sejam visíveis apenas onde estritamente necessário. 

<p style="background-color: #CBC3E3; padding: 5px; border-radius: 5px; font-weight: bold;">
Mantra: "Não posso quebrar o que não posso acessar".  
</p>

De modo geral tem-se que:

- É comum usarmos ```private``` como especificador de controle de acesso para atributos de uma classe;
- Já que é frequente querermos que métodos de uma classe sejam chamados por objetos de outras classes, não é raro usarmos ```public```como especificador de controle de acesso para métodos de uma classe;
- Como qualquer membro ```protected``` é acessível à classe e a suas subclasses, utilizamo-nos quando a intenção é dar acesso ao programadores que estenderão sua classe.

Além disso, as mudanças de atributos devem ser conduzidas por métodos da própria classe para garantir que ela mantenha o estado do objeto consistente! Tomemos como exemplo um semáforo:

- Não devemos efetuar as mudanças de atributos fora do semáforo. Portanto, não é bom ter um ```setCorDeSemaforo()```;
- É melhor ter um método ```muda()``` que realiza a mudança de cor;
- O próprio semáforo deve saber em que sequência mudar as cores do semáforo.

Vejamos um exemplo dessa classe:

```java
// Semaforo.java

enum CorDeSemaforo {
  VERMELHO, AMARELO, VERDE
}

public class Semaforo {
  
  private CorDeSemaforo corAtual;

  public Semaforo() {
    this(CorDeSemaforo.VERMELHO);
  }

  public void muda() {
    if(corAtual == CorDeSemaforo.VERMELHO) {
      corAtual = CorDeSemaforo.VERDE;
    } else if(corAtual == CorDeSemaforo.AMARELO) {
      corAtual = CorDeSemaforo.VERMELHO;
    } else {
      corAtual = CorDeSemaforo.AMARELO;
    }
  }

  public CorDeSemaforo getCorAtual() {
    return corAtual;
  }

  public String getNomeCorAtual() {
    if(corAtual == CorDeSemaforo.VERMELHO) {
      return "verde";
    } else if(corAtual == CorDeSemaforo.AMARELO) {
      return "amarela";
    } 
    return "vermelho";
  }

  public String toString() {
    return "semaforo está " + getNomeCorAtual();
  }
}
```



```java
// Programa.java

public class Programa {
  public static void main(String [] args) {
    
    Semaforo sinal = new Semaforo();
    
    System.out.println( sinal );
    
    sinal.muda();
    System.out.println( sinal );

    
    sinal.muda();
    System.out.println( sinal );
    
    
    sinal.muda();
    System.out.println( sinal );
    
  }
}
```

# Exercícios

2. Escreva um programa Java para criar uma classe chamada ContaBancaria com variáveis de instância privadas para o número da conta, agência e saldo. Em seguida, crie os seguintes métodos para acessar e modificar essas variáveis:
   1. ```Boolean depositar(Double quantia)``` que verifique se a quantia é positiva (hehehe) e atualize o saldo. Retorne ```true``` se o depósito pode ser realizado e ```false``` caso contrário;
   2. ```Boolean sacar(Double quantia)``` que realize um saque se houver dinheiro disponível e atualize o saldo. Retorne ```true``` se o saque pode ser realizado e ```false``` caso contrário;
   3. ```Boolean transferir(ContaBancaria outraConta, Double quantia)``` que realize uma transferência da conta atual (```this```) para a outra conta (```outraConta```). Retorne ```true``` se o saque pode ser realizado e ```false``` caso contrário;
   4. ```String toString()``` que mostre um texto indicando os dados bancários em formato textual.
   5. **EXTRA** ```String extrato()```  que, com uma Lista de Strings, registre um conjunto de operações de depósitos, saques e transferências para consuta de extrato.
   
   ```java
   public class BancoDoIFCE {
     public static void main(String [] args) {
       ContaBancaria contaDoSaulo = new ContaBancaria();
       ContaBancaria contaDaGeovana = new ContaBancaria();
       
       contaDoSaulo.depositar(1000.00);
       System.out.println(contaDoSaulo);
       
       // emprestar 20 reais pra geovana
       contaDoSaulo.transferir(contaDaGeovana, 20.00);
       System.out.println(contaDoSaulo);
       System.out.println(contaDaGeovana);
       
       // Geovana compra uma coca-cola
       contaDaGeovana.sacar(12);
       System.out.println(contaDaGeovana);
   
       // Geovana tenta pagar Saulo com juros
       contaDaGeovana.transferir(contaDoSaulo, 33.00);    
       System.out.println(contaDoSaulo);
       System.out.println(contaDaGeovana);
       
     }
   }
   ```
   
   

# Referências

1. Ivan Luiz Marques Ricarte. **Programação Orientada a Objetos**: Uma abordagem com Java, 2001. Disponível em: https://www.dca.fee.unicamp.br/cursos/PooJava/Aulas/poojava.pdf. Acessado em 19 de setembro de 2023.
2. ARVALHO, Victorio Albani de; TEIXEIRA, Giovany Frossard. Programação orientada a objetos: Curso técnico de informática. Colatina: IFES, 2012.
3. 
