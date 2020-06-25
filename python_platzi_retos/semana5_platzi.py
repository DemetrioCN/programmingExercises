# 1

""" curso = input("Ingrese su curso de PLATZ favorito:")

for i in range(8):
    print(curso) """

# 2

""" curso = input("Ingrese su curso de PLATZ favorito: ")
veces = int(input("Cuantas veces quiere mostrar el mensaje?: "))
for i in range(veces):
    print(curso) """

# 3
""" curso = input("Ingrese su curso de PLATZ favorito: ")

for each_letter in curso:
    print(each_letter)
 """

 # 4

""" animal = input("Cuál es tu animal favorito?: ")
n = int(input("Cuantas veces quieres imprimirlo? "))


for j in range(n):
    for i in animal:
        print(i)
    print("\n")
 """

# 5 Tabla de multiplicar
""" n = int(input("Ingrese un número n para obtener su table de multiplicar: "))
print(10*"-", f'Tabla de multiplicar del {n}', 10*"-")
print("\n")

for i in range(1,11):
    resultado = n*i
    print(f'{n} x {i} = {resultado}') """


# 6

""" numero = float(input("Ingresa un número: "))


if numero > 0:
    for i in range(int(numero)):
        print(numero - i)
else:
    for i in range(int(-1*numero)):
        print(numero+i)
print(float(0)) """

# 7

""" curso = input("Ingrese su curso de PLATZ favorito: ")
veces = int(input("Cuantas veces quiere mostrar el mensaje?: "))
if veces > 15:
    for i in range(3):
        print(curso)
    print(f'{veces} es un número muy grande')
else:
    for i in range(veces):
        print(curso) """

# 8 

""" num1 = float(input("Primer número: "))
var1 = input("Desea sumar este número al total?: ")

num2 = float(input("Segundo número: "))
var2 = input("Desea sumar este número al total?: ")

num3 = float(input("Tercer número: "))
var3 = input("Desea sumar este número al total?: ")

num4 = float(input("Cuarto número: "))
var4 = input("Desea sumar este número al total?: ")

print("\n")

numeros = [num1, num2, num3, num4]
valores = [var1, var2, var3, var4]

#print(numeros, valores)

suma = 0.0
for i in range(len(valores)):
    if valores[i] == 'si':
        #print(numeros[i])
        suma = suma + numeros[i]
print(suma)
 """

# 9 
respuesta = input("Desea una recta numérica positiva o negativa?: ")
numero = int(input("Introduce el número límite: "))
if respuesta == "positiva":
    for i in range(numero+1):
        print(i, end = ' ')
elif respuesta == "negativa":
    for i in range(numero+1):
        print(-i,  end = ' ')