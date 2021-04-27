from math import pi

print(10*"*","Este programa calcula el área de un círculo", 10*"*", )

def area_circulo(radio):
    area = pi*radio**2
    print("El área del círculo es: ", round(area, 4))

radio = float(input("Introduce un radio: "))
area_circulo(radio)