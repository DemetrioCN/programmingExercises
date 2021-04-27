""" Crea un programa donde tendrás la variable numero_secreto, 
la cual toma un valor aleatorio entre 1 y 100. Después pide 
a tu usuario que indique un número para intentar adivinarlo: 
en caso de acertar indícale cual era el número secreto y cuantos 
intentos le tomó; en caso contrario indícale si el número ingresado 
es mayor o menor al número secreto. """

import random
numero_secreto = random.randint(1, 100)
print(numero_secreto)

adivina_el_numero = int(input('Introduce un numero entre 1 y 100:\n '))

count = 0

while adivina_el_numero != numero_secreto:
    if numero_secreto < adivina_el_numero:
        print(f'El numero secreto es menor que {adivina_el_numero}\n')
    else:
        print(f'El numero secreto es mayor que {adivina_el_numero}\n')

    count += 1
    adivina_el_numero = int(input('Introduce un nuevo numero entre 1 y 100:\n '))

print(f'Te tomó {count} intentos encontrar el número secreto')

