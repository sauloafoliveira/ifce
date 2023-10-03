# Máquina de vender bilhetes

Uma máquina de bilhetes emite bilhetes de tarifa fixa. O preço de um bilhete é especificado pelo construtor. As instâncias verificarão para garantir que um usuário insira apenas
quantias sensatas de dinheiro, e só imprimirá um bilhete se tiver sido investido dinheiro suficiente. Veja o código abaixo.

```java
package bilheteria;

public class MaquinaDeBilhetes {
  
  private final Double preco; // preço dos bilhetes
  private Double saldo; // saldo armazenado para compra de bilhetes
  private Double total; // total arrecadado 
  
  public MaquinaDeBilhetes(Double preco) {
    this.preco = preco;
    this.saldo = 0.0;
    this.total = 0.0;
  }
  
  // Retorna o valor da tarifa
  public Double getPreco() {
    return preco;
  }
  
  
  // Retorna o saldo armazenado na máquina
  public Double getSaldo() {
    return saldo;
  }
  
  public void inserirDinheiro(Double quantia) {
    if(quantia > 0) {
      saldo = saldo + quantia;
    } else {
      System.out.println("Não existe dinheiro negativo.");
    }
  }
  
  
  // Imprime o bilhete
  public void imprimirBilhete() {
    // Simule a impressão de um bilhete. 	
    System.out.println("##################"); 
    System.out.println("# Bilhete "); 
    System.out.println("# " + preco);
    System.out.println("##################"); 
    System.out.println();

  }
  
}
```

Sob vários aspectos, seu comportamento é inadequado:

- Sem verificação sobre as quantias inseridas;

- Sem restituições;

- Sem verificação para uma inicialização correta.


Como podemos melhorar? Precisamos de um comportamento mais sofisticado.

# Exercício

Implemente em Java a classe ```Bilheteria``` com campos, métodos e instâncias de objetos que permitam a simulação da venda de bilhetes com a classe ```MaquinaDeBilhetes```. Esta classe deverá permitir o usuário:

1. Selecionar as opções:
   1. compra de bilhetes;
   2. visualizar preço do bilhete;
   3. restituição de saldo;
   4. imprimir bilhete; e
   5. sair.
2. A máquina deverá permitir apenas a inserção de cédulas de 5, 10 ou 20 reais;
3. Se o saldo for maior que 40 reais não deverá permitir inserir mais dinheiro, até que sejam gastos, pelo menos 20 reais em compra de bilhetes;
4. Imprimir bilhete deve ser possível somente se houver saldo suficiente;
5. Atualizar o total a cada venda/impressão de bilhete.