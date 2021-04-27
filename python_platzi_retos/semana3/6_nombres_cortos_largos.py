nombre = input("Ingrese su nombre: ").capitalize()

if len(nombre) > 5:
    print(f'Hola {nombre}, buenos días!')
else:
    apellido = input("Ingresa tu apellido: ").capitalize()
    print(f'Hola {nombre} {apellido}, buenos días!')