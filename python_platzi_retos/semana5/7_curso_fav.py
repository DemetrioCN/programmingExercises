curso = input("Ingrese su curso de PLATZ favorito: ")
veces = int(input("Cuantas veces quiere mostrar el mensaje?: "))
if veces > 15:
    for i in range(3):
        print(curso)
    print(f'{veces} es un número muy grande')
else:
    for i in range(veces):
        print(curso)