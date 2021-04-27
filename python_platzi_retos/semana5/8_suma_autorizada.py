num1 = float(input("Primer número: "))
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