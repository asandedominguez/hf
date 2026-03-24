#Importamos el tablero
from tablero import Tablero

#Creación de la clase Juego, es la que va a gestionarlo. Controla los ataques y muestra los resultados
class Juego:
    def __init__(self):
        self.tablero = Tablero()

#Muestra el resultado.
    def mostrar_resultado(self, resultado):
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")
        elif resultado is None:
            print("Ya disparaste aquí")

#Realiza los ataques a una posición el tablero.
    def lanzar_ataque(self, x, y):
        print(f"Ataque a {x},{y}")

#Conseguimos el resultado a traves del tablero
        resultado = self.tablero.comprobar_impacto(x, y)
#Se muestra el resultado
        self.mostrar_resultado(resultado)

#Ataques realizados
    def jugar(self):
        self.lanzar_ataque(1, 1)
        self.lanzar_ataque(1, 2)
        self.lanzar_ataque(1, 3)
        self.lanzar_ataque(1, 4)
        self.lanzar_ataque(1, 5)

if __name__ == "__main__":
    juego = Juego()
    juego.jugar()