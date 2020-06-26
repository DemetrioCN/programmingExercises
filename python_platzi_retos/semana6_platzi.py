#Retos de platzi

# Reto 1 - Suma hasta cincuenta
""" Crea una variable que se llame total, después pide a tu usuario 
que ingrese un número y lo sume al valor de total. Haz que esto 
se repita hasta que el valor de total sea mayor a 50 y muestra 
el resultado en pantalla. """

""" total = 0

while total < 50:
    n = int(input("Introduce un número entero: "))
    total += n

 """

# Reto #2 - Más allá del 42
""" Crea un código que pida al usuario un número y se repita
hasta que coloque un número mayor a 42. Cuando se cumpla 
esta condición muestra el resultado en pantalla indicando 
esto al usuario y finaliza el ciclo. """

""" 
i = 1
while i < 42:
    print(i)
    i += 1

print("Se ha llegado a 42") 
"""
 
# Reto #3 - Sumas consecutivas
""" Pide al usuario que ingrese dos números y los sume. Después 
pregunta si quiere añadir otro número: si la respuesta es 
afirmativa añádelo al total; en caso contrario finaliza el 
ciclo y muestra el resultado total en pantalla. """

""" 
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
"""


# Reto #4 - Lista de invitados
""" 
Estás organizando un banquete al que quieres invitar a 
tus amigos. Crea un programa que pida el nombre de uno 
de tus amigos, al hacerlo aumenta en uno una variable 
contadora, después pregunta si quieres invitar a alguien 
más: si la respuesta es afirmativa entonces pregunta por 
una persona más; en caso contrario cierra el ciclo y 
muestra en pantalla cuantos invitados son.
"""

""" 
count = 0
respuesta = 'si'
while respuesta == 'si':
    nombre = input("Introduce el nombre de un amigo: \n")
    count += 1
    respuesta = input("¿Quieres invitar a alguien más? \n")


print("Número total de invitados: ", count)
 """

# Reto #5 - Adivina el número secreto
""" Crea un programa donde tendrás la variable numero_secreto, 
la cual toma un valor aleatorio entre 1 y 100. Después pide 
a tu usuario que indique un número para intentar adivinarlo: 
en caso de acertar indícale cual era el número secreto y cuantos 
intentos le tomó; en caso contrario indícale si el número ingresado 
es mayor o menor al número secreto. """

""" 
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

print(f'Te tomó {count} intentos encontrar el número secreto') """

# Reto #6 - Un elefante se balanceaba
""" Escribe un programa que inicie mostrando en pantalla la letra de “Un elefante 
se balanceaba” iniciando con el número 1, después pregunta al usuario cuantos 
elefantes más se balancearán y debe responder un número más al mostrado. En caso 
de ingresar un número diferente pedirle que intente de nuevo y repetir el ciclo 
hasta tener 10 elefantes.Tomar en cuenta cuando el texto muestra un solo elefante 
y varios elefantes """


def elefante(num):
    if num > 1:
        print(f"""
        {num} elefantes se balanceaban
        Sobre la tela de una araña
        Como veían que resistía
        Fueron a llamar otro elefante""")
    else:
        print(f"""
        {num} elefante se balanceaba
        Sobre la tela de una araña
        Como veía que resistía
        Fue a llamar otro elefante""")



num = 1
print(elefante(num))

while num <= 10:
    num_elefantes = int(input('¿Cuantos elefantes más se balancearan? '))
    if num_elefantes < num:
        print("Intente con un nuevo número")
    else:
        num = num_elefantes
        print(elefante(num))