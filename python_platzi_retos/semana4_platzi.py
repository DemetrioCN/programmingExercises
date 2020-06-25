# 1

""" print("Ingresar dos números decimales")

num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))

print("El producto entre ellos es: ", num1*num2) """

# 2 

""" print("Ingresar dos números decimales")

num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
multi = num2*num2
print("El producto entre ellos es: ", round(multi,2)) """

# 3

""" print("Ingresa un número mayor a 20:")
numero = float(input("Numero: "))

print("Su raíz cuadra es: ", round(numero**0.5, 2) ) """

# 4
""" from math import pi

print(10*"*","Este programa calcula el área de un círculo", 10*"*", )

def area_circulo(radio):
    area = pi*radio**2
    print("El área del círculo es: ", round(area, 4))

radio = float(input("Introduce un radio: "))
area_circulo(radio) """

# 5
""" from math import pi

print(10*"*","Este programa calcula el volumen de un cilindro", 10*"*", )

def volumen_cilindro(radio, profundidad):
    volumen = pi*radio**2*profundidad
    print("El volumen del cilindro es: ", round(volumen, 1))

radio = float(input("Introduce el radio del cilindro: "))
profundidad = float(input("Introduce la profundidad del cilindro: "))
volumen_cilindro(radio, profundidad) """


# 6

""" print("Introduce 2 números")
num1 = float(input("Numero 1: "))
num2 = float(input("Numero 1: "))

resultado = f'{num1} dividido entre {num2} es {num1//num2} y sobra {num1%num2}'
print(resultado) """

# 7
figuras = ["Rectangulo", "Cuadrado", "Pentagono"]

print("\n")
print(10*" ", figuras[0] ,10*" ", figuras[1], 10*" ", figuras[2]  )
print("\n")

figura = input("Elegir figura: ")

if figura == figuras[0] or figura == figuras[0].lower() or figura == figuras[0].upper():
    print("Tamaño de los lados: \n")

    base = float(input("Base: "))
    altura = float(input("Altura: "))
    perimetro = 2*base + 2*altura
    area = base*altura
    print("Perimetro: ", perimetro)
    print("Area: ", area)

elif figura == figuras[1] or figura == figuras[1].lower() or figura == figuras[1].upper():
    lado = float(input("Tamaño de los lados: "))
    perimetro = 4*lado
    area = lado**2
    print("Perimetro: ", perimetro)
    print("Area: ", area)

elif figura == figuras[2] or figura == figuras[2].lower() or figura == figuras[2].upper():
    lado = float(input("Tamaño de los lados: "))
    radio = float(input("Radio: "))
    perimetro = 5*lado
    area = radio*(perimetro/2)
    print("Perimetro: ", perimetro)
    print("Area: ", area)


