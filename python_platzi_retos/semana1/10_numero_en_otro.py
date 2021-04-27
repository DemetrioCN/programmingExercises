print("--- Determina cuantas veces cabe un numero en otro ---")

def cuantas_veces():
    """
    Este programa regresa cuantas veces caben un número menor a 100 
    en un numero mayor a 1000
    """

    mayor = int(input("Introduce un numero mayor a 1000: "))
    menor = int(input("Introduce un numero menor a 100: "))

    print(mayor // menor)

#Ejecutando la funcion
cuantas_veces()
