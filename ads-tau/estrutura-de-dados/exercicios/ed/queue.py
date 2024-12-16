from typing import Generic, TypeVar, Self

T = TypeVar('T')


class Queue(Generic[T]):
    """
    Esta classe modela uma estrutura linear chamada fila na qual valores são adicionados em uma extremidade e removidos da outra. Esta disciplina dá origem a um comportamento primeiro a entrar/primeiro a sair (FIFO) que é a característica definidora das filas. As operações fundamentais da fila são ```enqueue``` (adicionar para trás) e ```dequeue(remover da frente)```. Ambas as operações são executadas em tempo O(1).
    """

    def __init__(self):
        """
        Inicializa uma nova fila, que está inicialmente vazia.
        """       
        super().__init__()

    
    def clear(self) -> None:
        """
        Remove todos os elementos da fila.

        Uso:
            fila.clear()
        """
        raise NotImplemented()
    

    def dequeue(self) -> T:
        """
        Remove e retorna o elemento mais à frente na fila. Se a fila estiver vazia, esta função sinaliza um erro (```IndexError```).
        
        Uso:
            primeiro = fila.dequeue()
        """
        raise NotImplemented()
    

    def enqueue(self, value: T) -> None:
        """
        Adiciona ```value``` ao final da fila.
        
        Uso:
            fila.enqueue(value)
        """
        raise NotImplemented()
    

    def equals(self, other: Self) -> bool:
        """
        Retorna ```True``` se as duas filhas contêm exatamente os mesmos valores de elementos na mesma ordem. Comportamento idêntico ao do operador  ```==```.

        Uso:
            if fila.equals(outra):
        """
        raise NotImplemented()


    def is_empty(self) -> bool:
        """
        Retorna ```True``` se esta fila não contém elementos.

        Uso:
            if fila.is_empty():
        """
        return self.size() == 0
    

    def peek(self) -> T:
        """
        Retorna o elemento no topo desta fila, sem removê-lo. Se a fila estiver vazia, esta função sinaliza um erro (```IndexError```).
        
        Uso:
            a = fila.peek()
        """
        raise NotImplemented()
    

    def size(self) -> int:
        """
        Retorna o número de valores nesta fila.

        Uso:
            tam = fila.size()
        """
        raise NotImplemented()
    

    def to_str(self) -> str:
        """
        Retorna uma representação de string imprimível desta fila. Os elementos são listados da esquerda para a direita, da frente da fila para trás, como "[value1, value2, value3]".

        Uso:
            print(fila.to_str())
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