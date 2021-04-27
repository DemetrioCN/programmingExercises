num_limite = float(input("Introduce un número limite: "))
num_comparar = float(input("Introduce un número para comparar: "))

if num_comparar < num_limite:
    print("El número {} se encuentra en el rango, gracias".format(num_comparar))
else:
    print("El número {} excede el límite permitido".format(num_comparar))