""" Crea una variable que se llame total, después pide a tu usuario 
que ingrese un número y lo sume al valor de total. Haz que esto 
se repita hasta que el valor de total sea mayor a 50 y muestra 
el resultado en pantalla. """

total = 0

while total < 50:
    n = int(input("Introduce un número entero: "))
    total += n
