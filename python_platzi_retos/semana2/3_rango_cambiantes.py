num_superior = float(input("Introduce un límite superior: "))
num_inferior = float(input("Introduce un límite inferior: "))
num = float(input("Introduce un número a comparar: "))

if num > num_inferior and num < num_superior:
    print("{} se encuentra entre  {} y {}".format(num, num_inferior,num_superior))
else:
    print("{} está fuera del rango establecido".format(num))
