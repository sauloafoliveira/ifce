from typing import Generic, TypeVar, Self

T = TypeVar('T')

class ArrayList(Generic[T]):

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

    def add(self, value: T) -> None:
        """
        Adiciona um novo valor ao final deste ArrayList.
        
        Uso:
            vec.add(valor);

        """
        raise NotImplemented()

    def clear(self) -> None:
        """
        Remove todos os elementos deste ArrayList.
        
        Uso:
            vec.clear()
        """
        raise NotImplemented()

    def equals(self, other: T) -> bool:
        """
        Retorna ```True``` se os dois vetores contêm exatamente os mesmos valores de elementos na mesma ordem. 
        
        Uso:
            if (vec1.equals(vec2)):

        """
        raise NotImplemented()

    def first(self) -> T:
        """
        Retorna o elemento no índice 0 neste vetor. Equivalente a get(0). 
        Este método sinaliza um erro (IndexError) se o vetor estiver vazio.

        Uso:
            a = vec.first()
        """
        raise NotImplemented()

    def get_at(self, index: int) -> T:
        """
        Retorna o elemento no índice especificado neste ArrayList. 
        Este método sinaliza um erro (```IndexError```) se o índice não estiver no intervalo deste ArrayList.
        
        Uso:
            b = vec.get_at(2)

        """
        raise NotImplemented()

    def insert_at(self, index: int, value: T) -> None:
        """
        Insere um novo valor neste vetor no índice especificado. 
        Todos os elementos subsequentes são deslocados uma posição para a direita. 
        Este método sinaliza um erro (```IndexError```) se o índice estiver fora do intervalo de 0 até e incluindo o comprimento deste ArrayList.

        Uso:
            vec.insert_at(0, valor)

        """
        raise NotImplemented()

    def is_empty(self) -> bool:
        """
        Retorna ```True``` se este ArrayList não contém elementos.
        
        Uso:
            if vec.is_empty():
        """
        return self.size() == 0
    
    def last(self) -> T:
        """
        Retorna o último elemento neste ArrayList. Equivalente a ```get(size() - 1)```. 
        Este método sinaliza um erro (```IndexError```) se o ArrayList estiver vazio.

        Uso:
            val = vec.last()
        """
        raise NotImplemented()

    def map(self, fn: callable) -> None:
        """
        Chama a função especificada em cada elemento deste vetor em ordem de índice crescente e mofidica o valor do índice pelo resultado de ```fn```.

        Uso:
            vec.map(lambda x: x * 2)

        """
        raise NotImplemented()

    def remove_at(self, index: int) -> None:
        """
        Remove o elemento no índice especificado deste ArrayList. 
        Todos os elementos subsequentes são deslocados uma posição para a esquerda. 
        Este método sinaliza um erro (```IndexError```) se o índice estiver fora do intervalo do ArrayList.

        Uso:
            vec.remove_at(0, valor)
        """
        raise NotImplemented()

    def reverse(self) -> None:
        """
        Reorganiza os elementos neste vetor na ordem oposta. 
        Como exemplo, o elemento anteriormente no índice ```0``` é trocado pelo elemento no índice ```size()-1```.

        Uso:
            vec.reverse()
        """
        raise NotImplemented()

    def set_at(self, index: int, value: T) -> None:
        """
        Substitui o elemento no índice especificado neste vetor por um novo valor. 
        O valor anterior naquele índice é sobrescrito. 
        Este método sinaliza um erro (```IndexError```) se o índice não estiver no intervalo do ArrayList.

        Uso:
            vec.set_at(2, value)

        """
        raise NotImplemented()

    def shuffle(self) -> None:
        """
        Reorganize os elementos neste ArrayList em ordem aleatória.
        
        Uso:
            vec.shuffle()
        """
        raise NotImplemented()
    
    def size(self) -> int:
        """
        Retorna o número de elementos neste ArrayList.
        
        Uso:
            tam = vec.size()

        """
        raise NotImplemented()

    def sort(self) -> None:
        """
        Reorganiza os elementos neste vetor em ordem crescente. 
        Os elementos são comparados usando o operador ```<```. 
        Em ordem crescente, o elemento mínimo é colocado no índice ```0```; o máximo está no índice ```size()-1```.
 
        Uso:
            vec.sort()
        """
        raise NotImplemented()
    
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
        raise NotImplemented()

    def to_str(self) -> str:
        """
        Retorna uma representação de string imprimível deste ArrayList, como "[value1, value2, value3]".
        """
        raise NotImplemented()

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