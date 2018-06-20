#!/usr/bin/python
import os
    
def menu():
    print(' ')
    print('*** ARCHIVO DE NOMBRES Y APELLIDOS ***')
    print(' ')
    print('1. Ingresar Nombre y Apellido')
    print('2. Mostrar el Archivo')
    print('3. Salir')
    print(' ')

while True:
    menu()
    opcion = int(input('Ingrese una opcion: '))
    
    if opcion == 1:
        nombre = input("Ingresa tu nombre: ");
        #print ('Nombre ingresado: ' + str(nombre))
        apellido = input("Ingresa tu apellido: ");
        #print ('Tu nombre es: {}' .format(apellido))
        
        file = open('nombres.txt','a')
        file.write(nombre + ' ' + apellido + '\n')
        file.close()
        
    elif opcion == 2:
        print("Listado de Nombres:")
        file = open("nombres.txt", 'r') 
        for linea in file.readlines(): 
            print (linea)
            file.close()
        
    elif opcion == 3 or opcion == 0:
        print (' ')
        print('Gracias por usar este programa.')
        break
    
    elif opcion != 1 or 2 or 3 or 0:
        menu()
        


