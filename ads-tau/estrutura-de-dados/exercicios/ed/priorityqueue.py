from typing import Generic, TypeVar, Self

T = TypeVar('T')


class PriorityQueue(Generic[T]):
    """
    Esta classe modela uma estrutura chamada *fila de prioridades* na qual os valores são processado em ordem de prioridade. Como no uso convencional do inglês, números de prioridade mais baixa correspondem a prioridades mais urgentes, de modo que um item de prioridade 1 tem precedência sobre um item de prioridade 2. As operações fundamentais da fila de prioridades são ```enqueue``` (adicionar valor com prioridade atribuída) e ```dequeue```(remover valor com prioridade mais urgente). Ambas as operações são executadas em tempo O(log N).

    """

    def __init__(self):
        """
        Inicializa uma nova fila de prioridades, que está inicialmente vazia.
        """
        super().__init__()


    def clear(self) -> None:
        """
        Remove todos os elementos da fila.

        Uso:
            fila.clear()
        """
        raise NotImplementedError()
    

    def dequeue(self) -> T:
        """
        Remove e retorna o valor mais à frente (mais urgente).

        Uso:
            urgente = fila_prioridade.dequeue()
        """
        raise NotImplementedError()
    

    def enqueue(self, value: T, priority: int) -> None:
        """
        Adiciona ```value``` à fila de prioridades com a ```priority``` especificada.
        
        Uso:
            fila_prioridade.dequeue("a", 1)  #["a"]     

            fila_prioridade.dequeue("b", 2)  #["a", "b"]

            fila_prioridade.dequeue("c", 1)  #["a", "c", "b"]

        """
        raise NotImplementedError()

    
    def equals(self, other: Self) -> bool:
        """
        Retorna ```True``` se as duas filas de prioridade contêm exatamente os mesmos valores de elementos na mesma ordem. Comportamento idêntico ao do operador  ```==```.

        Uso:
            if fila_prioridade.equals(outra):
        """
        raise NotImplementedError()


    def is_empty(self) -> bool:
        """
        Retorna ```True``` se esta fila de prioridade não contém elementos.

        Uso:
            if fila_prioridade.is_empty():
        """
        return self.size() == 0
    

    def peek(self) -> T:
        """
        Retorna o elemento no topo desta fila de prioridade, sem removê-lo. Se a fila estiver vazia, esta função sinaliza um erro (```IndexError```).
        
        Uso:
            a = fila_prioridade.peek()
        """
        raise NotImplementedError()
    

    def peek_piority(self) -> int:
        """
        Retorna a prioridade do elemento no topo desta fila de prioridade, sem removê-lo. Se a fila estiver vazia, esta função sinaliza um erro (```IndexError```).
        
        Uso:
            a = fila_prioridade.peek_priority()
        """
        raise NotImplementedError()
    

    def size(self) -> int:
        """
        Retorna o número de valores nesta fila.

        Uso:
            tam = fila_prioridade.size()
        """
        raise NotImplemented()
    

    def to_str(self) -> str:
        """
        Retorna uma representação de string imprimível desta fila de prioridade. Os elementos são listados por prioridade, da esquerda para a direita, da frente da fila para trás, como "[value1, value2, value3]".

        Uso:
            print(fila_prioridade.to_str())
        """
        raise NotImplementedError()

    
    ## truques do Python

    def __bool__(self) -> bool:
        return not self.is_empty()
    
    
    def __eq__(self, other: Self) -> bool:
        return self.equals(other)


    def __str__(self) -> str:
        return self.to_str()
    

    def __len__(self) -> int:
        return self.size()