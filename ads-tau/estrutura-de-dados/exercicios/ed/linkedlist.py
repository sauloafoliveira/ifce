from typing import Generic, TypeVar, Self
from arraylist import ArrayList

T = TypeVar('T')

class ListNode(Generic[T]):

    def __init__(self, value: T):
        self._value = value
        self._next = None

class LinkedList(Generic[T], ArrayList[T]):

    def __init__(self, n: int=0, value: T=None) -> Self:
        """
        Inicializa uma nova Lista. 
        O construtor padrão cria um vetor vazio. 
        A segunda forma cria um array com ```n``` elementos, cada um dos quais é inicializado para ```value```;
        Se ```value``` estiver faltando, os elementos são inicializados com None.

        Args:
            n (int): a quantidade de posições pré-alocadas.
            value (T): o valor padrão a ser preenchido.

        Returns:
            Uma nova lista de tuplas.
        """
        super().__init__()

        self._size = 0
        self._head: ListNode = None
        self._tail: ListNode = None

    def add(self, value: T) -> None:
        node = ListNode(value)

        if self.is_empty():
            self._head, self._tail = node
            self._size = 1
        else:
            self._tail.next = node
            self._size += 1
        

    def clear(self) -> None:
        self._head, self._tail = None
        self._size = 0

    def equals(self, other: T) -> bool:
        """
        Retorna ```True``` se os dois vetores contêm exatamente os mesmos valores de elementos na mesma ordem. 
        
        Uso:
            if (vec1.equals(vec2)):

        """
        raise NotImplementedError()

    def first(self) -> T:
        if self.is_empty():
            raise IndexError('Lista vazia')
        
        return self._head.value
    

    def get_at(self, index: int) -> T:
        node = self._head
        i = 0

        while node:
            if i == index:
                node._value
            
            node = node._next
            i += 1


    def insert_at(self, index: int, value: T) -> None:
        """
        Insere um novo valor neste vetor no índice especificado. 
        Todos os elementos subsequentes são deslocados uma posição para a direita. 
        Este método sinaliza um erro (```IndexError```) se o índice estiver fora do intervalo de 0 até e incluindo o comprimento deste ArrayList.

        Uso:
            vec.insert_at(0, valor)

        """
        raise NotImplementedError()

    def is_empty(self) -> bool:
        return self.size() == 0
    

    def last(self) -> T:
        if self.is_empty():
            raise IndexError()
        
        return self._tail._value


    def map(self, fn: callable) -> None:
        node = self._head
        
        while node:
            node._value = fn(node._value)            
            node = node._next

    def remove_at(self, index: int) -> None:
        """
        Remove o elemento no índice especificado deste ArrayList. 
        Todos os elementos subsequentes são deslocados uma posição para a esquerda. 
        Este método sinaliza um erro (```IndexError```) se o índice estiver fora do intervalo do ArrayList.

        Uso:
            vec.remove_at(0, valor)
        """
        raise NotImplementedError()



    def reverse(self) -> None:
        aux = LinkedList()
        node = self._head
        
        while node:
            aux.insert_at(0, node._value)
        
        self._head = aux._head

    def set_at(self, index: int, value: T) -> None:
        i = 0

        while node:
            if i == index:
                node._value = value
                break
            
            node = node._next


    def shuffle(self) -> None:
        """
        Reorganize os elementos neste ArrayList em ordem aleatória.
        
        Uso:
            vec.shuffle()
        """
        raise NotImplementedError()
    
    def size(self) -> int:
        return self._size

    def sort(self) -> None:
        """
        Reorganiza os elementos neste vetor em ordem crescente. 
        Os elementos são comparados usando o operador ```<```. 
        Em ordem crescente, o elemento mínimo é colocado no índice ```0```; o máximo está no índice ```size()-1```.
 
        Uso:
            vec.sort()
        """
        raise NotImplementedError()
    
    def sublist(self, start: int, end: int=-1) -> Self:
        """
        Retorna um novo vetor contendo elementos de um subintervalo deste vetor. 
        Se apenas um argumento for fornecido, o comprimento do subintervalo será até o fim deste vetor. 
        Por exemplo, a chamada de ```sublist(2, 4)``` retornaria um novo vetor contendo os elementos 2-5 do vetor original em seus índices 0-3. 
        Gera um erro se o intervalo ```[start, end)``` não estiver contido no intervalo ```[0, size()]```.

        Uso:
            sub1 = vec.sublist(3)
            sub2= vec.sublist(1, 4)
        """
        raise NotImplementedError()

    def to_str(self) -> str:
        """
        Retorna uma representação de string imprimível deste ArrayList, como "[value1, value2, value3]".
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

    
    def __get_item__(self, index: int) -> T:
        return self.get_at(index)


    def __set_item__(self, index, value) -> None:
        return self.set_at(index, value)