from ListaSimple import ListaSimple
import xml.etree.ElementTree as ET


def cargarArchivo(ruta, terrenos):
    tree = ET.parse(ruta)
    root = tree.getroot()

    for elemento in root:
        print('Terreno -> ', elemento.attrib['nombre'])
        for subelemento in elemento:
            # para obtener los datos de la dimension
            for dimension in subelemento.iter('dimension'):
                for dimM in dimension.iter('m'):
                    print('m -> ', dimM.text)
                for dimN in dimension.iter('n'):
                    print('n -> ', dimN.text)
                    
            # para obtener los datos de la posicion inicial        
            for posicionInicial in subelemento.iter('posicioninicio'):
                for posXInicio in posicionInicial.iter('x'):
                    print('x Inicio -> ', posXInicio.text)
                for posYInicio in posicionInicial.iter('y'):
                    print('y Inicio -> ', posYInicio.text)

            # para obtener los datos de la posicion final        
            for posicionFinal in subelemento.iter('posicionfin'):
                for posXFinal in posicionFinal.iter('x'):
                    print('x Fin -> ', posXFinal.text)
                for posYFinal in posicionFinal.iter('y'):
                    print('y Fin -> ', posYFinal.text)
        # terrenos.crearTerrenos('terreno', 'filasM', 'columnasN', 'xInicial', 'yInicial', 'xFinal', 'yFinal')

            for posicion in subelemento.iter('posicion'):
                print('cordenadas -> ', 'x=' ,posicion.attrib['x'] , ' y=', posicion.attrib['y'], ' - ', posicion.text )
                # print('Gasolina -> ',posicion.text)
                # for cordenadaX in posicion.attrib['x']:
                #     print('x cordenada -> ',cordenadaX.text)


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
            Filename = input('Ingrese nombre de archivo:')
            file = './' + Filename
            cargarArchivo(file, ListaTerrenos)
 
        elif opcion == '2':
            print('Ingrese nombre fichero')
      
        elif opcion == '3':
            print('Ingrese nombre fichero')
       
        elif opcion == '4':
            print('Ingrese nombre fichero')
         
        elif opcion == '5':
            print('Ingrese nombre fichero')
             
        else:
            opcion = 6
if __name__ == "__main__":
    menu()