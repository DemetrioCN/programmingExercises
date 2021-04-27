""" Pide al usuario que ingrese dos números y los sume. Después 
pregunta si quiere añadir otro número: si la respuesta es 
afirmativa añádelo al total; en caso contrario finaliza el 
ciclo y muestra el resultado total en pantalla. """

print("Ingrese dos números")

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

suma = num1 + num2

respuesta = input("¿Le gustaría añadir otro número?")
while respuesta == "si":
    num3 = int(input("Ingrese un número más: "))
    suma_3 = suma + num3
    print(suma_3)
else:
    print(suma)