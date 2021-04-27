from math import pi

print(10*"*","Este programa calcula el volumen de un cilindro", 10*"*", )

def volumen_cilindro(radio, profundidad):
    volumen = pi*radio**2*profundidad
    print("El volumen del cilindro es: ", round(volumen, 1))

radio = float(input("Introduce el radio del cilindro: "))
profundidad = float(input("Introduce la profundidad del cilindro: "))
volumen_cilindro(radio, profundidad)