""" 
Estás organizando un banquete al que quieres invitar a 
tus amigos. Crea un programa que pida el nombre de uno 
de tus amigos, al hacerlo aumenta en uno una variable 
contadora, después pregunta si quieres invitar a alguien 
más: si la respuesta es afirmativa entonces pregunta por 
una persona más; en caso contrario cierra el ciclo y 
muestra en pantalla cuantos invitados son.
"""

count = 0
respuesta = 'si'
while respuesta == 'si':
    nombre = input("Introduce el nombre de un amigo: \n")
    count += 1
    respuesta = input("¿Quieres invitar a alguien más? \n")


print("Número total de invitados: ", count)
