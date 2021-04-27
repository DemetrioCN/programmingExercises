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