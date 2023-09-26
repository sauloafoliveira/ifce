# NullBank (rsrsrsr)

Façamos agora uma um aplicativo (classe com programa principal) para controlar  as funcionalidades do banco com a classe ```ContaBancaria``` da aula passada:

```java
package nullbank;

public class ContaBancaria {
  private Integer numero;
  private String nome;
  private Double saldo;
  
  public ContaBancaria(Integer numero, String nome) {
		this.numero = numero;
    this.nome = nome;
    this.saldo = 0.0;
  }
  
  public Boolean depositar(Double quantia) {
    this.saldo += (quantia > 0) ? quantia : 0;
    return true;
  }
  
  public Boolean sacar(Double quantia) {
    Boolean podeSacar = (quantia <= saldo);
    this.saldo -= podeSacar ? quantia : 0;
    return podeSacar;
  }
  
  public Boolean transferir(ContaBancaria outraConta, Double quantia) {
    if (this.sacar(quantia)) {
      outraConta.depositar(quantia);
      return true;
    }
    return false;
  }
  
  @Override
  public String toString() {
    return String.format("Conta %d de [%s] tem %.2f de saldo.", numero, nome, saldo);
  }
  
}
```





```java
package nullbank;
  
public class NullBank {
  
  public static Integer id = 1;
  
  public static ContaBancaria criarConta(String nome) {
    return new ContaBancaria(id++, nome);
  }
  
  public static void main(String [] args) {
    ContaBancaria c1 = criarConta("Saulo");
    ContaBancaria c2 = criarConta("Geovana");

    System.out.println(c1);
    System.out.println(c2);
    
    c1.depositar(100.00);
    c2.depositar(33.00);
    
    System.out.println(c1);
    System.out.println(c2);
    
    c1.transferir(c2, 12.00);
    
    System.out.println(c1);
    System.out.println(c2);
  }
}
```



## Membros de classe (e também de objetos)

Atributos estáticos são atributos que contêm informações inerentes a uma classe e não a um objeto em específico. Por isso são também conhecidos como atributos ou **variáveis de classe**.

Por exemplo, suponha que quiséssemos ter um atributo que indicasse a quantidade de contas criadas. Esse atributo não seria inerente a uma conta em específico, mas a todas as contas. Assim, seria definido como um atribu- to estático. Para definir um atributo estático em Java, basta colocar a palavra *static* entre o qualificador e o tipo do atributo.

<div style="margin-left: 25%; font-size: small; text-align: justify;">
Define um atributo de uma classe inteira. A variável se aplica à própria classe e a todas as suas instâncias, de modo que somente um valor é armazenado, não importando quantos objetos dessa classe tenham sido criados (CADENHEAD; LEMAY, 2005, p. 9).
</div>

O mesmo conceito é válido para métodos. Métodos estáticos são inerentes à classe e, por isso, não nos obrigam a instanciar um objeto para que possa- mos utilizá-los. Para definir um método como estático, basta utilizar a palavra *static*, a exemplo do que acontece com atributos. Para utilizar um método estático devo utilizar o nome da classe acompanhado pelo nome do método.



**Observação:** Um método criado como estático só poderá acessar atributos que também sejam estáticos, além dos seus argumentos e variáveis locais.



# Exercícios

1. Faça um conjunto de métodos **estáticos** para realizar um menu para um conjunto de operações de caixa de banco:
   1. Método para realizar depósito informando o número da conta e o valor a ser depositado;
   2. Método para realizar saque informando o número da conta e o valor a ser sacado. Observação, imprima "saldo insuficiente" se o saque não puder ser realizado;
   3. Método para realizar transferência informando os números de contas e o valor a ser transferido da primeira conta para a segunda. Observação, imprima "saldo insuficiente" se o saque não puder ser realizado;
   4. Método para remunerar a 1% todos as contas, isto é, ```saldo *= 0.01 ```, pois no NullBank todo o dinheiro investido;
   5. Método para mostrar o capital do banco inteiro, isto é, o total de todo o dinheiro das contas existentes no banco;
   6. Método para cobrar taxa de manutenção de todas as contas no valor de R$ 5,30;
   7. Mostrar o membro mais rico;
   8. Mostrar o número de correntistas.

   

# Referências

1. Ivan Luiz Marques Ricarte. **Programação Orientada a Objetos**: Uma abordagem com Java, 2001. Disponível em: https://www.dca.fee.unicamp.br/cursos/PooJava/Aulas/poojava.pdf. Acessado em 19 de setembro de 2023.
2. ARVALHO, Victorio Albani de; TEIXEIRA, Giovany Frossard. Programação orientada a objetos: Curso técnico de informática. Colatina: IFES, 2012.