class Terreno:
    def __init__(self, terreno, filasM, columnasN, xInicial, yInicial, xFinal, yFinal):
        self.terreno = terreno
        self.filasM = filasM
        self.columnasN = columnasN
        self.xInicial = xInicial
        self.yInicial = yInicial
        self.xFinal = xFinal
        self.yFinal = yFinal
        # self.cordenadasXY 
        self.siguiente = None
        
    
#     Las x es m o sea las filas
#     Las y son n o seas las columnas