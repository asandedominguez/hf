# Clase que representa el tablero del juego
class Tablero:

    def __init__(self, tamano=10):
        self.tamano = tamano
        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2

        self.tablero = [[None for i in range(tamano)] for i in range(tamano)]
    def colocar_nave(self, nave, x, y, orientacion):
        if orientacion == "H":
            for e in range(nave.tamno):
                self.tablero[x][y+e] = nave

        elif orientacion == "V":
    
    def comprobar_impacto(self, x, y):
        """
        Comprueba si hay una nave en las coordenadas indicadas.
        Si hay nave, llama a su método recibir_disparo().

        Args:
            x (int): Coordenada X del disparo
            y (int): Coordenada Y del disparo

        Returns:
            str: Resultados del disparo ("Agua", "Tocado", "Hundido")
        """
        print("[LOG] estoy en tablero comprobando impacto")
        return self.AGUA
