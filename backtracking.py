from Array2D import Array2D

class LaberintoADT:
    """
    0 pasillo, 1 pared, S salida y E entrada
    pasillo es una tupla ((2,1),(2,2),(2,3),(2,4),(3,2),(4,2))
    entrada en una tupla (5,1)
    salida (2,5)
    """
    def __init__(self, rens,cols,pasillos,entrada,salida ):
        self.__laberinto = Array2D(rens,cols,'1')
        for pasillo in pasillos:
            self.__laberinto.set_item(pasillo[0], pasillo[1], '0')
        self.set_entrada(entrada[0],entrada[1])
        self.set_salida(salida[0],salida[1])

    def to_String(self):
        self.__laberinto.to_string()

    """
    Establece la entrada "E" en la matriz, verificar limites perifericos
    """
    def set_entrada(self, ren, col):
        self.__laberinto.set_item(ren,col,'E')
    """
    Establece la entrada "S" en la matriz, verificar limites perifericos
    """
    def set_salida(self,ren, col):
        self.__laberinto.set_item(ren,col,'S')
