numero = float(input("Ingresa un número: "))


if numero > 0:
    for i in range(int(numero)):
        print(numero - i)
else:
    for i in range(int(-1*numero)):
        print(numero+i)
print(float(0))