class Posicion:
    def __init__(self, x, y, gas):
        self.x = x
        self.y = y
        self.gas = gas
        self.siguiente = None
        self.anterior = None