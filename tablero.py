#Importación de las clases Nave y Casilla
from nave import Nave
from casilla import Casilla

#Creación de la clase tablero del juego. Esta tiene una lista con todas las casillas y va a gestionar los impactos
class Tablero:

    def __init__(self):

#Valores que puede haber al gestionar un impacto
        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2

#Creación de las naves
        por1 = Nave("Enterprise", "portaaviones", 5)

        fra1 = Nave("Bismarck", "fragata", 3)
        fra2 = Nave("Prince of Wales", "fragata", 3)
        fra3 = Nave("Graf Spee", "fragata", 3)

        sub1 = Nave("U-47", "submarino", 1)
        sub2 = Nave("U-96", "submarino", 1)
        sub3 = Nave("U-505", "submarino", 1)
        sub4 = Nave("U-534", "submarino", 1)

#Tablero con las casillas (10x10)
        self.casillero = [
            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()],

            [Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla(), Casilla()]
        ]

#Colocación de las naves en el tablero
        self.casillero[1][1].nave = por1
        self.casillero[1][2].nave = por1
        self.casillero[1][3].nave = por1
        self.casillero[1][4].nave = por1
        self.casillero[1][5].nave = por1

        self.casillero[3][3].nave = fra1
        self.casillero[4][3].nave = fra1
        self.casillero[5][3].nave = fra1

        self.casillero[7][1].nave = fra2
        self.casillero[7][2].nave = fra2
        self.casillero[7][3].nave = fra2

        self.casillero[9][1].nave = fra3
        self.casillero[9][2].nave = fra3
        self.casillero[9][3].nave = fra3

        self.casillero[4][6].nave = sub1
        self.casillero[9][9].nave = sub2
        self.casillero[7][6].nave = sub3
        self.casillero[9][5].nave = sub4

#Realiza un disparo a la posición que establezcamos. La x son las filas y y columnas. Devolverá el resultado de la acción
    def comprobar_impacto(self, x, y):
        print(f"Impacto en ({x},{y})")
        return self.casillero[x][y].disparar()
