ingreso = input('Ingrese el archivo: ')
archivo = open(ingreso,'r')
contenido = archivo.read()

oraciones = contenido.count('.')
print('El texto contiene {} oraciones.'.format(oraciones))
