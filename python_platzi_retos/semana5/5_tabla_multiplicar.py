n = int(input("Ingrese un número n para obtener su table de multiplicar: "))
print(10*"-", f'Tabla de multiplicar del {n}', 10*"-")
print("\n")

for i in range(1,11):
    resultado = n*i
    print(f'{n} x {i} = {resultado}')