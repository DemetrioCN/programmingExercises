respuesta = input("Desea una recta numérica positiva o negativa?: ")
numero = int(input("Introduce el número límite: "))
if respuesta == "positiva":
    for i in range(numero+1):
        print(i, end = ' ')
elif respuesta == "negativa":
    for i in range(numero+1):
        print(-i,  end = ' ')