ingreso = input('Ingrese el archivo: ')
archivo = open(ingreso,'r')
contenido = archivo.read()

string = input('Ingrese que palabra buscar: ')
veces = contenido.count(string)
print('La letra/palabra "{}" aparece {} veces.'.format(string,veces))
