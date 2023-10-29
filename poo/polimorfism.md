# Polimorfismo

## Sobrecarga 

Métodos/Construtures sobrecarregados são métodos que tem o mesmo nome, mas com argumentos diferentes, eles possuem estas características:

- possuem lista de argumentos diferentes;
- podem alterar o tipo de retorno;
- podem alterar o modificador de acesso;
- podem declarar exceções verificadas novas ou mais abrangentes.


**Em resumo**: Pra sobrecarregar métodos, você *DEVE* mudar a assinatura do método, manipulando seus argumentos:

```java
public void init()
public void init(String value)
public void init(Sring value, String key)
public void init(Integer value)
```


## Múltiplas formas

Lembram-se daquela semântica que foi dito sobre herança? “É UM”. Então podemos tratar um objeto da classe filha como se fosse um objeto da classe pai.

```java 
// ContaBancaria.java

package nullbank;

class ContaBancaria {

    protected Double saldo;
    private Integer agencia;
    private Integer numero;
    private String favorecido;

    public ContaBancaria(Double saldo, Integer agencia, Integer numero, String favorecido) { /** ... */  }

    public void sacar(Double quantia) {}
    
    public void depositar(Double quantia) {}

    public void transferir(ContaBancaria destino, Double quantia) {}    
    
    /// Imagine getters & setters
}

// ContaPoupanca.java

package nullbank;

public class ContaPoupanca extends ContaBancaria {

    public ContaPoupanca(Double saldo, Integer agencia, Integer numero, String favorecido) {
        super(saldo, agencia, numero, favorecido);
    }

    public void render() {
        this.saldo *= 1.06; // render a 6%.
    }
}


// ContaCorrente.java

package nullbank;

public class ContaCorrente extends ContaBancaria {

    public ContaCorrente(Double saldo, Integer agencia, Integer numero, String favorecido) {
        super(saldo, agencia, numero, favorecido);
    }

    public void pagar(Boleto boleto) {
        if(this.saldo >= boleto.getValor()) {
            this.saldo -= boleto.getValor();
            boleto.setPago(true);
        }
    }
}
```
Agora, olhemos para a classe ```ContaCorrente```. Vamos adicionar a opção de pagar via Pix.
Pix é o pagamento instantâneo brasileiro. O meio de pagamento criado pelo Banco Central (BC) em que os recursos são transferidos entre contas em poucos segundos, a qualquer hora ou dia. É prático, rápido e seguro. O Pix pode ser realizado a partir de uma conta corrente, conta poupança ou conta de pagamento pré-paga.

```java
// ContaCorrente.java

package nullbank;

public class ContaCorrente extends ContaBancaria {

    public ContaCorrente(Double saldo, Integer agencia, Integer numero, String favorecido) {
        super(saldo, agencia, numero, favorecido);
    }

    // ... código anterior //

    public void pix(QrCode qrcode) {
        Boleto boleto = qrcode.getBoleto();
        this.pagar( boleto );
    }

    public void pix(String chave, Double quantia) {
        ContaBancaria destino = BancoCentral.getContaCorrentePelaChave( chave );
        
        if(destino == null) {
            System.out.println("Não existe conta associada a esta chave.");
        } else {
            this.transferir( destino, quantia );
        }
    } 

    public void pix(String copiaECola) {
        QrCode qrcode = BancoCentral.getQrCode( copiaECola );
        this.pix( qrcode );
    }
}
```

Foram adicionados 03 (três) novos métodos:
- ```public void pix(QrCode);```;
- ```public void pix(String)```;
- ```public void pix(String, Double)```.

A primeira coisa que deve vir a sua cabeça quando se trata de polimorfismo é **herança**. Este conceito de herança, ela tem que estar bem definido para que você possa entender o conceito, ou seja, quando a classe ```B```  herda de uma classe ```A```, todos os membros (varáveis de instância e métodos) públicos ou protegidos de ```A``` passa a fazer parte de ```B```. Usando outra abordagem é dizer que polimorfismo é usado usar um tipo genérico de variáveis de referência para apontar para tipos de objetos mais específicos.


```java

package nullbank;
public class NullBank {

    public static void main(String [] args) {
        ContaBancaria a = new ContaCorrente();
        ContaCorrente b = new ContaCorrente();

        a.pix("saulo@gmail", 10.0); // por quê dá erro?
        b.pix("saulo@gmail", 10.0); // por quê dá erro?
    }
}
```
# Exercício -- Sobrecarga
1. Crie um novo projeto chamado ```PraticaSobrecarga```. Sugere-se agora a criação de três construtores diferentes para a classe ```Relogio``` apresentada na listagem abaixo. Desta maneira, o relógio pode ser inicializado de três maneiras diferentes:

   1. Informando-se hora, minuto e segundo (como já feito);
   2. Informando-se somente a hora e o minuto, e inicializando o segundo com 1;
   3. Informando-se somente a hora, e inicializando o minuto e o segundo com 1.

Obs.: Considere a utilização do método ```acertaHora```.

```java
package sobrecarga;

public class Relogio {

    // Atributos
    private Integer hora, minuto, segundo;

    /** Digite aqui os conttrutores */
    public Relogio(Integer h, Integer m, Integer s) {
        acertaHora(h, m, s);
    }

    public void acertaHora(Integer h, Integer m, Integer s) {
        this.hora    = (h >= 0 && h <= 23) ? h : 0;
        this.minuto  = (m >= 0 && m <= 59) ? m : 0;
        this.segundo = (s >= 0 && s <= 59) ? s : 0;
    }

    public String toString() {
        String str = "Hora atual: " + hora + ":" + minuto + ":" + segundo;
        return str;
    }
}
```
Agora, crie uma classe ```TestaRelogio``` que implementa o método ```main```. Dentro deste método, crie novos objetos da classe ```Relogio``` com valores diferentes utilizando todos os construtores implementados. Depois, apresente no Terminal a hora armazenada em cada relógio criado. Verifique que aqueles não informados são inicializados corretamente com 1.

2. Crie uma nova classe chamada ```Cor``` para descrever as cores em um sistema de cores. Sugere-se agora a criação de dois construtores diferentes para a classe ```Cor`` apresentada na listagem abaixo. Desta maneira, uma cor pode ser criada a partir de um hexadecimal:

    1. O construtor vazio deve iniciar as componentes para gerar a cor preta ```black```;
    2. O construtor que usa ```String``` deve permitir ao menos usar as cores básicas (```red```, ```blue```, ```green```, ```yellow```, ```magenta```, ```cyan```, ```black``` e ```white```);
    3. Um construtor que usa as três inteiros para criar uma cor RGB.

```java
package sobrecarga;
public class Cor {

	private Integer red, green, blue;

	public Cor(Integer hex) {
		red = (hex & 0xFF0000) >> 16;
		green = (hex & 0xFF00) >> 8;
		blue = (hex & 0xFF);
	}

	@Override
	public String toString() {
		return String.format("rgb(%02d, %02d, %02d)", red, green, blue);
	}

	public static void main(String[] args) {
		System.out.println(new Cor(0xAF5622)); // em Java, o hexadecimal é com 0x e não com #
//		System.out.println(new Cor("red"));
//		System.out.println(new Cor(100, 200, 20));
//		System.out.println(new Cor());
	}
}
```

A saída *desejada* do código acima deve estar em desconforme:
```shell
$ rgb(175, 86, 34)
$ rgb(255, 0, 0)
$ rgb(100, 200, 20)
$ rgb(0, 0, 0)
```


## Referências

- Sobrecarga e sobrescrita, 2008, https://www.guj.com.br/t/sobrecarga-e-sobrescrita/212821. Acessado em 29 de out 2023.
- Banco Central do Brasil. **Pix**. 2023. Disponível em: https://www.bcb.gov.br/estabilidadefinanceira/pix. Acessado em 29 de out 2023.
- . Disponível em: https://www.inf.pucrs.br/~michael/aulas/algo_progII/apresentacoes/aula4%20-%20exercicios%20sobre%20sobrecarga.htm. Acessado em 29 de out. 2023.
- Tatiana Vieira. **O que são os padrões HEX, RGB e HSL de cores?** Disponível em: https://tecnoblog.net/responde/o-que-sao-os-padroes-hex-rgb-e-hsl-de-cores/. Acessado em 29 de out. 2023.