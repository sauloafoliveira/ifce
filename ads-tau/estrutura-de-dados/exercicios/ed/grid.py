from typing import Generic, TypeVar, Self

T = TypeVar('T')


class Grid(Generic[T]):

    def __init__(self, rows: int, cols: int, value: T = None) -> None:
        super().__init__()



    def clear(self) -> None:
        """
        Remove todos os elementos da grade.

        Uso:
            grade.clear()
        """
        raise NotImplementedError()
    

    def equals(self, other: Self) -> bool:
        """
        Retorna ```True``` se as duas grades contêm exatamente os mesmos valores de elementos na mesma ordem. Comportamento idêntico ao do operador  ```==```.

        Uso:
            if grade.equals(outra):
        """
        raise NotImplementedError()


    def fill(self, value: T) -> None:
        """
        Define cada elemento nesta grade para o valor fornecido. Todo o conteúdo da grade é substituído por este valor em cada local.

        Uso:
            grade.fill(valor)
        """
        raise NotImplementedError()
    

    def get_at(self, row: int, col: int) -> T:
        """
        Retorna o elemento especificado na ```(row, col)``` da grade. Este método sinaliza um erro se o local especificado estiver fora dos limites da grade.
        
        Uso:
            valor = grade.get_at(x, y)
        """
        raise NotImplementedError()
    

    def in_bounds(self, row: int, col: int) -> bool:
        """
        Retorna ```True``` se a ```row``` e ```col``` especificados estão dentro dos limites da grade.
        """

        raise NotImplementedError()
    

    def is_empty(self) -> bool:
        """
        Retorna ```True``` se a grade não contém nenhuma linha ou coluna (tamanho 0x0).

        Uso:
            if grid.is_empty():
        """
        return self.size() == 0
    

    def map(self, fn: callable) -> None:
        """
        Chama a função especificada em cada elemento da grade. Os elementos são processados em ordem de linha principal, na qual todos os elementos da linha 0 são processados, seguidos pelos elementos da linha 1, e assim por diante.

        Uso:
            grade.map(fn)
        """
        raise NotImplementedError()
    

    def num_cols(self) -> int:
        """
        Retorna o número de colunas na grade.
        """
        raise NotImplementedError()
    

    def num_rows(self) -> int:
        """
        Retorna o número de linhas na grade.
        """
        raise NotImplementedError()
    

    def resize(self, rows: int, cols: int, retain: bool = False) -> None:
        """
        Reinicializa a grade para ter o número especificado de linhas e colunas (```rows``` e ```cols```). Cada elemento da grade recém-redimensionada é inicializado para o valor padrão do tipo. Se o argumento ```retain``` opcional for ```True```, ele retém qualquer conteúdo de grade anterior que possa ser. Se ```retain``` for ```False``` ou não for fornecido, todos os conteúdos anteriores serão descartados.

        Esta função sinaliza um erro se um número negativo de linhas ou colunas for passado.

        Uso:
            grade.resize(rows, cols)
            grade.resize(rows, cols, True)
        """

        raise NotImplementedError()
    

    def set_at(self, row: int, col: int, value: T) -> None:
        """
        Substitui o elemento no local especificado ```row``` e ```col``` na grade por um novo valor. Este método sinaliza um erro (```IndexError```) se o local especificado estiver fora dos limites da grade.

        Uso:
            grade.set_at(x, y, value)
        """
        raise NotImplementedError()
    

    def size(self) -> int:
        """
        Retorna o número total de elementos na grade, que é igual ao número de linhas vezes o número de colunas.

        Uso:
            sz = grade.size()
        """

        return self.num_cols() * self.num_rows()
    


    def to_str(self) -> str:
        """
        Retorna uma representação de string imprimível desta grade, como "[value1, value2, value3; value4, value5, value6; value7, value8, value9]".

        Uso:
            print(grid.to_str())
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

    
    def __get_item__(self, index) -> T:
        return self.get_at(index[0], index[1])


    def __set_item__(self, index, value) -> None:
        return self.set_at(index[0], index[1], value)