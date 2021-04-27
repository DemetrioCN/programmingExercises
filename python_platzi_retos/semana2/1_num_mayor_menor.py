print("Da cual es el numero mayor y su diferencia")
def diferencia_numeros():
    num1 = float(input("Introduce un numero: "))
    num2 = float(input("Introduce otro numero: "))

    diff = abs(num1 - num2)
    diferencia = "La diferencia entre ellos es de {}".format(diff)
    if num1 < num2:
        print("{} es mayor que {}".format(num2, num1))
        print(diferencia)
    elif num1 > num2:
        print("{} es mayor que {}".format(num1, num2))
        print(diferencia)
    else:
        print("Ambos son el mismo número")

# Llamar a la funcion
diferencia_numeros()