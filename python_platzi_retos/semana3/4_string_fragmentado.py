oracion = input("Introduce una oración de 10 o más caracteres:")
longitud = len(oracion)
print(f'La longitud de la oración es de {longitud} caracteres')

print("Introduce un número inferior y uno superior que no sobrepase la longitud.")

inferior = int(input("Número inferior: "))
superior = int(input("Número superior: "))

print("Imprimiendo los caracteres que se encuentran en el rango dado: ")
print(oracion[inferior:superior])