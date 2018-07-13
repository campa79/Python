#!/usr/bin/python
import os

#Final Diagramación Lógica / Fecha: 2/6/18
#Tema: Crear un WC - Contador de palabras, líneas y caracteres.
#Alumno: Alberto Campagna
#IFTS 18 - Analista de Sistemas

# ----------------------- MENU ----------------------- #
def menu():
    print('')
    print("--------------------")
    print("-   Programa WC    -")
    print("--------------------")
    print('')
    print('1. Ingresar archivo')
    print('2. Mostrar archivo')
    print('3. Buscador archivo')
    print('4. Salir')
    print('')
# --------------------- PALABRAS --------------------- #
def palabras():
    cant_palabras = len(contenido3)
    return(cant_palabras)
# ---------------------- LINEAS ---------------------- #
def lineas():
    cant_lineas = sum(1 for line in open(ingreso))
    return(cant_lineas)
# --------------------- PARRAFOS --------------------- #
def parrafos():
    parrafos = contenido.split('.\n')
    cant_parrafos = len(parrafos)
    return(cant_parrafos)
# ---------------------- LETRAS ---------------------- #
def letras():
    letras = 0
    for i in contenido3:
        letras = letras + len(i)
    return(letras)
# ---------------------------------------------------- #

while True:
    menu()
    try:
        opcion = int(input('Ingrese una opción: '))
        if opcion == 4:
            print (' ')
            print('Gracias por usar este programa.')
            break
        ingreso = input('Ingrese el archivo: ')
        archivo = open(ingreso,'r')
        contenido = archivo.read()
        contenido1 = contenido.replace('\n',' ')
        contenido2 = contenido1.replace('  ',' ')
        contenido3 = contenido2.split(" ")
        
        if opcion == 1:
            print('')
            print('El texto tiene {} palabras, {} líneas, {} párrafos y {} letras.'
                .format(palabras(),lineas(),parrafos(),letras()))
            print('')
        
        elif opcion == 2:
            archivo = open(ingreso,'r')
            for linea in archivo.readlines(): 
                print (linea)
            archivo.close()
            
        elif opcion == 3:
            archivo = open(ingreso,'r')
            string = input('Ingrese que palabra buscar: ')
            lista = contenido.count(string)
            print('La letra/palabra "{}" aparece {} veces.'.format(string,lista))
    
        elif opcion != 1 or 2 or 3 or 4 or 0:
            menu()

        archivo.close()
        
    except:
        print('Ingrese una opción correcta.')
