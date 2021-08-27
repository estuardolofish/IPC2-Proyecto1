from os import X_OK
from xml.etree.ElementTree import ProcessingInstruction
from Posicion import Posicion

class ListaDoble():
    def __init__(self):
        self.inicio = None

    def insertar(self, x, y, gas):
        nuevo = Posicion(x, y, gas)
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
            nuevo.anterior = tmp

    def mostrarPosiciones(self):
        tmp = self.inicio
        while tmp is not None:
            print('x -> :', tmp.x, 'y ->:', tmp.y, ' Gas ->:', tmp.gas)
            tmp = tmp.siguiente

    # def mostrarCoordenadas():
    #     tmp = self.inicio
    #     while tmp is not None:
    #         return tmp.x
    #         print('x -> :', tmp.x, 'y ->:', tmp.y, ' Gas ->:', tmp.gas)
    #         tmp = tmp.siguiente
