from os import system,startfile
from typing import Collection
from Terreno import Terreno
from ListaSimple import ListaSimple
import xml.etree.ElementTree as ET

def cargarArchivo(ruta, terrenos):
    tree = ET.parse(ruta)
    root = tree.getroot()

    for elemento in root:
        # codigo para imprimir el nombre del terreno
        print('Terreno -> ', elemento.attrib['nombre'])
        # terrenos.crearTerreno(elemento.attrib['nombre'], 'filasM', 'columnasN', 'xInicial', 'yInicial', 'xFinal', 'yFinal')

        for subelemento in elemento:
            # para obtener los datos de la dimension
            for dimension in subelemento.iter('dimension'):
                for dimM in dimension.iter('m'):
                    # print('m -> ', dimM.text)
                    pass
                for dimN in dimension.iter('n'):
                    # print('n -> ', dimN.text)
                    pass
                    
            # para obtener los datos de la posicion inicial        
            for posicionInicial in subelemento.iter('posicioninicio'):
                for posXInicio in posicionInicial.iter('x'):
                    # print('x Inicio -> ', posXInicio.text)
                    pass
                for posYInicio in posicionInicial.iter('y'):
                    # print('y Inicio -> ', posYInicio.text)
                    pass
            # para obtener los datos de la posicion final        
            for posicionFinal in subelemento.iter('posicionfin'):
                for posXFinal in posicionFinal.iter('x'):
                    # print('x Fin -> ', posXFinal.text)
                    pass
                for posYFinal in posicionFinal.iter('y'):
                    # print('y Fin -> ', posYFinal.text)
                    pass
        terrenos.crearTerreno(elemento.attrib['nombre'], int(dimM.text), int(dimN.text), int(posXInicio.text), int(posYInicio.text), int(posXFinal.text), int(posYFinal.text))

        # aqui imprimo las coordenadas y el gas
        for subelemento in elemento:
            for posicion in subelemento.iter('posicion'):
                # print('cordenadas -> ', 'x=' ,posicion.attrib['x'] , ' y=', posicion.attrib['y'], ' - ', posicion.text )
                pass
                # print('Gasolina -> ',posicion.text)
                # for cordenadaX in posicion.attrib['x']:
                #     print('x cordenada -> ',cordenadaX.text)
                terreno = terrenos.getTerreno(elemento.attrib['nombre'])
                terreno.cordenadasXY.insertar(int(posicion.attrib['x']),int(posicion.attrib['y']), int(posicion.text) )
                
def generarGrafica(terreno, coordenadas,filaM,columnaN):

    # while coordenadas is not None:
    #     print('fila:', coordenadas.x, 'columna:', coordenadas.y, ' Gas ->:', coordenadas.gas)
    #     coordenadas = coordenadas.siguiente

    coordenadasMatriz = coordenadas 
    grafica = '''
        digraph mapaTerreno{
            node[shape=box fillcolor="#00FA92" style =filled]
            
            subgraph cluster_p{
                label= '''+ str(terreno) +'''
                bgcolor = "#FFFBD6"
                edge[dir = "none"]
    '''

    while coordenadas is not None:
        grafica += 'nodo' + str(coordenadas.x) +'_'+ str(coordenadas.y) +'[label="'+ str(coordenadas.gas) +'"]'+'\n'
        coordenadas = coordenadas.siguiente
        # print('x -> :', coordenadas.x, 'y ->:', coordenadas.y, ' Gas ->:', coordenadas.gas)

    for i in range(1, int(columnaN) + 1):
        grafica += '\n'
        # print("")
    
        for j in range(1, int(filaM) + 1):
            if j == int(filaM):
                grafica += 'nodo' + str(j) +'_'+ str(i) 
            else:
                grafica += 'nodo' + str(j) +'_'+ str(i) +'->'

            # print('nodo', i , '_' , j)

    
    for i in range(1, int(filaM) + 1):
        grafica += '\n'
        # print("")
        grafica += 'rank=same{'
        for j in range(1, int(columnaN) + 1):
            if j == int(columnaN):
                grafica += 'nodo' + str(i) +'_'+ str(j) 
            else:
                grafica += 'nodo' + str(i) +'_'+ str(j) +'->'
        grafica += '}'
            # print('nodo', i , '_' , j)
            



    grafica += '''
        } }
    '''
    # imprimiendo en forma de matriz 
    while coordenadasMatriz is not None:
        print("[", end=" ")
        for j in range(1,int(columnaN) +1):
            print(coordenadasMatriz.gas, end=" ")
            coordenadasMatriz = coordenadasMatriz.siguiente
        print("]")
    
    miArchivo = open(str(terreno)+'.dot', 'w')
    miArchivo.write(grafica)
    miArchivo.close()

    system('dot -Tpdf '+str(terreno)+'.dot -o '+str(terreno)+'.pdf')
    system('cd ./'+str(terreno)+'.pdf')
    startfile(''+str(terreno)+'.pdf')

def generarRutaCorta(terreno, coordenadas,filaM, columnaN,xInicial,yInicial,xFinal,yFinal ):
    print(terreno)



def menu():
    opcion = 0
    ListaTerrenos = ListaSimple()
    while opcion != 6:
        print('----- Menu Ficheros -----')
        print('1. CARGAR ARCHIVO')
        print('2. PROCESAR ARCHIVO')
        print('3. ESCRIBIR ARCHIVO DE SALIDA')
        print('4. MOSTRAR DATOS DEL ESTUDIANTE')
        print('5. GENERAR GRAFICA')
        print('6. SALIR')
        opcion = input("-> ")
        ruta = ''
        if opcion == '1':
                try:
                    Filename = input('Ingrese nombre de archivo:')
                    # if ".xml" in Filename:
                    file = './' + Filename
                    print(file)
                    if '.xml' in file:
                        cargarArchivo(file, ListaTerrenos)
                        print("Archivo ingresado exitosamente")
                    else:
                        print("Extencion no Admitida en el programa o ruta no encontrada")
                except:
                    print("Errro al ingresar el archivo")
        elif opcion == '2':
            # print('Ingrese nombre fichero')
            print('***********Eligiendo la ruta mas cota ***********')
            # sirve para mostar totos lso terrenos y coordenadas
            # ListaTerrenos.mostrarTerrenos()

            print("Terrenos ingresados: ")
            ListaTerrenos.mostrarSoloTerrenos()
            terr = input('Ingrese Terreno que dese graficar -> ')
            nomTerreno = ListaTerrenos.getTerreno(terr)
            if nomTerreno is None: 
                print('> Terreno incorrecto o no registrado')
            else:
                print('Terreno ----------------------------- ', nomTerreno.terreno)
                # print(nomTerreno.filasM)
                print('-------Archivo procesado-------')
                # nomTerreno.cordenadasXY.mostrarPosiciones()
                # print("prueba-> ", nomTerreno.cordenadasXY.inicio.gas)
                tmp = nomTerreno.cordenadasXY.inicio
                generarRutaCorta(nomTerreno.terreno, tmp,nomTerreno.filasM,nomTerreno.columnasN,nomTerreno.xInicial,nomTerreno.xFinal, nomTerreno.xFinal, nomTerreno.yFinal)
            
      
        elif opcion == '3':
            print('Ingrese nombre fichero')
       
        elif opcion == '4':
            print('-> Estuardo Leonel López Par')
            print('-> 201907622')
            print('-> Introducción a la Programación de Computación 2 seccion "D" ')
            print('-> Ingenieria en Ciencias y Sistemas')
            print('-> 4to Semestre')
         
        elif opcion == '5':
            print('*********** Generando Grafica *************')
            print("Terrenos ingresados: ")
            ListaTerrenos.mostrarSoloTerrenos()
            terr = input('Ingrese Terreno que dese graficar -> ')
            nomTerreno = ListaTerrenos.getTerreno(terr)
            if nomTerreno is None: 
                print('> Terreno incorrecto o no registrado')
            else:
                print('Terreno ----------------------------- ', nomTerreno.terreno)
                # print(nomTerreno.filasM)
                print('-------Coordenadas-------')
                # nomTerreno.cordenadasXY.mostrarPosiciones()
                # print("prueba-> ", nomTerreno.cordenadasXY.inicio.gas)
                tmp = nomTerreno.cordenadasXY.inicio
                generarGrafica(nomTerreno.terreno, tmp,nomTerreno.filasM,nomTerreno.columnasN)
             
        else:
            opcion = 6
            print('Fin de la aplicacion')
if __name__ == "__main__":
    menu()