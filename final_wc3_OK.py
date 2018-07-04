#!/usr/bin/python

#Final Diagramación Lógica / Fecha: 2/6/18
#Tema: Crear un WC - Contador de palabras, líneas y caracteres
#Alumno: Alberto Campagna
#IFTS 18 - Analista de Sistemas

print ("-------------------------------------------------------")
print ("Programa WC / Contador de Palabras, Líneas y Caracteres")
print ("-------------------------------------------------------")

ingreso = input('Ingrese el archivo: ')

archivo = open(ingreso,'r')
contenido = archivo.read()
contenido1 = contenido.replace('\n',' ')
contenido2 = contenido1.replace('  ',' ')
contenido3 = contenido2.replace('.','')
contenido4 = contenido3.split(" ")

# ------ PALABRAS ------ #
cant_palabras = len(contenido4)

# ------ PARRAFOS ------ #
parrafos = contenido.split('.\n')
cant_parrafos = len(parrafos)

# ------- LETRAS ------- #
letras = 0
contenido5 = contenido1.replace('  ','')
contenido5 = contenido1.replace(' ','')
for i in contenido5:
    letras = letras + len(i)

print(' ')
print('El texto tiene', cant_palabras , 'palabras,', cant_parrafos ,
      'párrafos y', letras , 'letras.')

archivo.close()
