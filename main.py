import xml.etree.ElementTree as ET





def Menu():
    opcion = 0
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
            print('Ingrese nombre fichero')
 
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
    Menu()