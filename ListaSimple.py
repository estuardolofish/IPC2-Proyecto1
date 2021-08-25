from Terreno import Terreno

class ListaSimple():
    def __init__(self):
        self.inicio = None
        self.fin = None
        self.size = 0

    def crearTerreno(self, terreno, filasM, columnasN, xInicial, yInicial, xFinal, yFinal):  #insertar a final
        nuevo = Terreno(terreno, filasM, columnasN, xInicial, yInicial, xFinal, yFinal ) #nuevo estudiante
        self.size += 1
        if self.inicio is None:
            self.inicio = nuevo
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    def mostrarTerrenos(self):
        tmp = self.inicio
        while tmp is not None:
            print('Terreno--------------------------------------- ', tmp.terreno)
            print('m -> :', tmp.filasM)
            print('N -> :', tmp.columnasN)
            print('xInicial :', tmp.xInicial)
            print('yInicial :', tmp.yInicial)
            print('xFinal :', tmp.xFinal)
            print('yFinal :', tmp.yFinal)
            tmp = tmp.siguiente

    def getTerreno(self, terreno):
        tmp = self.inicio
        while tmp is not None:
            if tmp.terreno == terreno:
                return tmp
            tmp = tmp.siguiente
        return None
