from typing import Generic, TypeVar, Self

T = TypeVar('T')


class Stack(Generic[T]):


    def __init__(self) -> Self:
        """
        Esta classe modela uma estrutura linear chamada pilha na qual valores são adicionados e removidos somente de uma extremidade. Esta disciplina dá origem a um comportamento last-in/first-out (LIFO) que é a característica definidora das pilhas. As operações fundamentais da pilha são ```push``` (adicionar ao topo) e ```pop``` (remover do topo). Ambas as operações são executadas em tempo O(1).

        """
        super().__init__()

    def clear(self) -> None:
        """
        Remove todos os elementos desta pilha.

        Uso:
            pilha.clear()
        """
        raise NotImplemented()
    

    def equals(self, other: Self) -> bool:
        """
        Retorna ```True``` se as duas pilhas contêm exatamente os mesmos valores de elementos na mesma ordem. Comportamento idêntico ao do operador  ```==```.

        Uso:
            if pilha.equals(outra):
        """
        raise NotImplemented()
    

    def is_empty(self) -> bool:
        """
        Retorna ```True``` se esta pilha não contém elementos.

        Uso:
            if pilha.is_empty():
        """
        return self.size() == 0
    

    def peek(self) -> T:
        """
        Retorna o elemento no topo desta pilha, sem removê-lo. Se a pilha estiver vazia, esta função sinaliza um erro (```IndexError```).
        
        Uso:
            a = pilha.peek()
        """

        raise NotImplemented()
    

    def pop(self) -> T:
        """
        Remove o elemento do topo desta pilha e o retorna. Se a pilha estiver vazia, esta função sinaliza um erro (```IndexError```).

        Uso:
            a = pilha.pop()

        """

        raise NotImplemented()
    

    def push(self, value: T) -> None:
        """
        Adiciona o valor especificado a esta pilha.

        Uso:
            pilha.push(value)
        """
        raise NotImplemented()

    def size(self) -> int:
        """
        Retorna o número de valores nesta pilha.

        Uso:
            tam = pilha.size()
        """

        raise NotImplemented()



    def to_str(self) -> str:        
        """
        Retorna uma representação de string imprimível desta pilha. Os elementos listados da esquerda para a direita, da parte inferior da pilha para o topo, como "[{]value1, value2, value3]".

        Uso:
            print(pilha.to_str())
        """

    ## truques do Python

    def __bool__(self) -> bool:
        return not self.is_empty()
    
    
    def __eq__(self, other: Self) -> bool:
        return self.equals(other)


    def __str__(self) -> str:
        return self.to_str()
    

    def __len__(self) -> int:
        return self.size()

    