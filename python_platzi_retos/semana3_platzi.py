# Ejercicios de la semana 3

# 1

""" curso = input("Ingresa el título de tu curso favoritto de platzi:  ")

print("Longitud de la cadena de texto: ", len(curso)) """

# 2

""" nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
comida_favorita = input("Ingresa tu comida favorita: ")

print(f'Hola, mi nombres es {nombre} {apellido} y mi comida favorita es {comida_favorita}') """


# 3
""" print("Ingresa los siguientes datos en minúscula")

nombre = input("Nombre: ")
apellido = input("Apellido: ")
pais = input("País: ")

print("Debido a que se trata de nombrs propios, la forma correcta es: ")
print(nombre.capitalize())
print(apellido.capitalize())
print(pais.capitalize()) """

# 4

""" oracion = input("Introduce una oración de 10 o más caracteres:")
longitud = len(oracion)
print(f'La longitud de la oración es de {longitud} caracteres')

print("Introduce un número inferior y uno superior que no sobrepase la longitud.")

inferior = int(input("Número inferior: "))
superior = int(input("Número superior: "))

print("Imprimiendo los caracteres que se encuentran en el rango dado: ")
print(oracion[inferior:superior]) """

# 5
""" 
print("Indique dos palabras ")

palabra1 = input("Primera palabra: ")
palabra2 = input("Segunda palabra: ")

print(palabra1.lower())
print(palabra2.upper()) """

# 6

""" nombre = input("Ingrese su nombre: ").capitalize()

if len(nombre) > 5:
    print(f'Hola {nombre}, buenos días!')
else:
    apellido = input("Ingresa tu apellido: ").capitalize()
    print(f'Hola {nombre} {apellido}, buenos días!') """

# 7

palabra = input("Introduce una palabra: ")

consonantes = 'bcdfghjklmnpqrstvwxyz'
consonantes = consonantes.join(consonantes.upper())

vocales = 'aeiou'
vocales = vocales.join(vocales.upper())

if palabra[0] in consonantes:
    print(palabra[1:] + palabra[0] + "ay")
elif palabra[0] in  vocales:
    print(palabra + "way")
#else:
#    print("No se encontró ninguna opción")