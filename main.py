from ListaSimple import ListaSimple
import xml.etree.ElementTree as ET


def cargarArchivo(ruta, terrenos):
    tree = ET.parse(ruta)
    root = tree.getroot()

    for elemento in root:
        # codigo para imprimir el nombre del terreno
        # print('Terreno -> ', elemento.attrib['nombre'])
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
        terrenos.crearTerreno(elemento.attrib['nombre'], dimM.text, dimN.text, posXInicio.text, posYInicio.text, posXFinal.text, posYFinal.text)

        for subelemento in elemento:
            for posicion in subelemento.iter('posicion'):
                print('cordenadas -> ', 'x=' ,posicion.attrib['x'] , ' y=', posicion.attrib['y'], ' - ', posicion.text )
                pass
                # print('Gasolina -> ',posicion.text)
                # for cordenadaX in posicion.attrib['x']:
                #     print('x cordenada -> ',cordenadaX.text)
                terreno = terrenos.getTerreno(elemento.attrib['nombre'])
                terreno.cordenadasXY.insertar(posicion.attrib['x'],posicion.attrib['y'], posicion.text )
                

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

              

                # try:
                    Filename = input('Ingrese nombre de archivo:')
                    # if ".xml" in Filename:
                    file = './' + Filename
                    cargarArchivo(file, ListaTerrenos)
                    print("Archivo ingresado exitosamente")
                #     else:
                #         print("Extencion no Admitida en el programa o ruta no encontrada")
                # except:
                #     print("Vuelva a ingresar la ruta")
    
        elif opcion == '2':
            # print('Ingrese nombre fichero')
            print('---------- Terrenos Ingresados ----------', 'Total:',ListaTerrenos.size)
            ListaTerrenos.mostrarTerrenos()
      
        elif opcion == '3':
            print('Ingrese nombre fichero')
       
        elif opcion == '4':
            print('Ingrese nombre fichero')
         
        elif opcion == '5':
            print('Ingrese nombre fichero')
             
        else:
            opcion = 6
            print('Fin de la aplicacion')
if __name__ == "__main__":
    menu()