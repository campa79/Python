#! -- coding: utf-8 --
# Programa de la prueba de Python IFTS 18
# 1er Parcial 2018

cantidad_alumnos = int(input("Ingrese cantidad de alumnos: "))

for alumno in range(cantidad_alumnos):
    print("INGRESE LAS NOTAS:")
    print("")
    n1 = int(input("Nota 1: "))
    n2 = int(input("Nota 2: "))
    n3 = int(input("Nota 3: "))
    
    promedio = (n1 + n2 + n3) / 3
    if promedio < 4:
        print("Desaprobado.")

    else:
        print("Aprobaste con un promedio de: " + str(promedio))

#Aca hago la parte que muestra la nota mas alta.
    if n1 > n2 and n1 > n3:
        print('La nota mas alta fue un {}' .format(n1))
    elif n2 > n1 and n2 > n3:
        print('La nota mas alta fue un {}' .format(n2))
    elif n3 > n1 and n3 > n2:
        print('La nota mas alta fue un {}' .format(n3))

#    if n1 > n2 and n3:
#        print('La nota mas alta fue un ' + str(n1))
#    elif n2 > n1 and n3:
#        print('La nota mas alta fue un ' + str(n2))
#    else:
#        print('La nota mas alta fue un ' + str(n3))


