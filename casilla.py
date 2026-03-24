#Cración de la clase casilla con el atributo nave y visitada. Representa una casilla del tablero. Guarda si ya fue atacada
class Casilla:
    def __init__(self):
        self.nave = None
        self.visitada = False

#Realiza un disparo sobre la casilla. None si ya fue atacada, 0 si es agua, 1 tocado y 2 hundido.
    def disparar(self):
        if self.visitada:
            print("Ya disparaste aquí")
            return None

        self.visitada = True

        if self.nave is None:
            return 0

        return self.nave.recibir_disparo()