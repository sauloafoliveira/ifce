from typing import Optional

class Pix:

    feitos = []

    def __init__(self, origem: "ContaCorrente", valor: float):
        self._origem = origem
        self._valor = valor

        
    def enviar(self, chave_destino: str):
        conta_destino = BancoCentral.recuperar_conta(chave_destino)
        
        if not conta_destino:
            print('Conta destino inexistente.')
            return False
        
        if self._origem.transferir(destino=conta_destino, valor=self._valor):
            self.feitos.append(self)
            print('Pix realizado com sucesso.')
            return True
        
        print('Algum erro com a trasnferência. Verifique seu banco.')
        return False

     
class ContaCorrente:

    def __init__(self):
        self.saldo = 0


    def registrar(self, chave: str) -> bool:
        return BancoCentral.registrar(self, chave)
    

    def depositar(self, valor: float) -> bool:
        if BancoCentral.e_valido(valor):
            self.saldo += valor
            return True
        
        return False
    

    def sacar(self, valor: float):
        if not BancoCentral.e_valido(valor):
            return False
        
        if BancoCentral.e_valido(self.quantia - valor):
            self.saldo -= valor
            return True
        
        return False
    
    
    def transferir(self, destino: "ContaCorrente", valor: float):
        if self.sacar(valor):
            return destino.depositar(valor)
        
        return False
    

    def fazer_pix(self, chave_destino: str, valor: float) -> bool:
        p = Pix(origem=self, valor=valor)
        return p.enviar(chave_destino)



class BancoCentral:

    __contas_registradas = {}

    @staticmethod
    def e_valido(quantia: float) -> bool:
        return quantia > 0
    

    @classmethod
    def registrar(cls, conta: ContaCorrente, chave: str) -> bool:
        if chave in cls.__contas_registradas:
            return False
        
        cls.__contas_registradas[chave] = conta

        return True
    

    @classmethod
    def desregistrar(cls, conta_ou_chave: ContaCorrente|str) -> bool:
        if isinstance(conta_ou_chave, ContaCorrente): # usando conta
            
            if cls.recuperar_conta(conta_ou_chave):
                del cls.__contas_registradas[conta_ou_chave]
                return True

        if isinstance(conta_ou_chave, str): # usando chave
            if conta_ou_chave not in cls.__contas_registradas:
                del cls.__contas_registradas[conta_ou_chave]
                return True
            
        return False
    
    
    @classmethod
    def recuperar_conta(cls, chave: str) -> ContaCorrente:
        if chave not in cls.__contas_registradas:
            return None
        
        conta = cls.__contas_registradas[chave]
        return conta
    

c = ContaCorrente()
c.depositar(10)
c.registrar('sauloaf@gmail.com')
print(c.saldo)

e = ContaCorrente()
e.registrar('saulo@ifce.edu.br')

p = Pix(c, 10)
p.enviar('saulo@ifce.edu.br')

print(c.saldo)
