#Creación de la clase nave, representa una nave en el juego. Tiene vidas, por lo que puede ser tocada o hundida, que eatará represnetado con los valores 1 y 2
class Nave:
    TOCADO = 1
    HUNDIDO = 2

#Creación de los atributos
    def __init__(self, nombre, tipo, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.hundido = False

#Reduce la vida de la nave al ser disparada. Si es 1 es tocado, 2 hundido
    def recibir_disparo(self):

#Si esta hundida devuelve directaente hundido
        if self.hundido:
            return self.HUNDIDO
#Reducción de vida si es tocadada
        self.vida -= 1

#Si esta vida llega a 0 cambiara a estar hundida. Si no estará solo tocada.
        if self.vida <= 0:
            self.vida = 0
            self.hundido = True
            print(f"{self.nombre} hundido")
            return self.HUNDIDO
        else:
            print(f"{self.nombre} tocado. Vida restante: {self.vida}")
            return self.TOCADO

