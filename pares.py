#Pares / Impares
numero = int(input('Ingrese un numero: '))

if numero %2 == 0:
    print('El numero es par.')
else:
    print('El numero es impar')

#Pares / Impares - Rango de números
for numero in range(1,21):

    if numero %2 == 0:
        print('Los numeros pares son el ' + str(numero))
