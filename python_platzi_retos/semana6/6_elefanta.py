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