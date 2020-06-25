#Ejercicio 1
#def diferencia_numeros():
#    num1 = float(input("Introduce un numero: "))
#    num2 = float(input("Introduce otro numero: "))

#    diff = abs(num1 - num2)
#    diferencia = "La diferencia entre ellos es de {}".format(diff)
#    if num1 < num2:
#        print("{} es mayor que {}".format(num2, num1))
#        print(diferencia)
#    elif num1 > num2:
#        print("{} es mayor que {}".format(num1, num2))
#        print(diferencia)
#    else:
#        print("Ambos son el mismo número")

#diferencia_numeros()


#Ejercicio 2
""" 
num_limite = float(input("Introduce un número limite: "))
num_comparar = float(input("Introduce un número para comparar: "))

if num_comparar < num_limite:
    print("El número {} se encuentra en el rango, gracias".format(num_comparar))
else:
    print("El número {} excede el límite permitido".format(num_comparar))

 """

#Ejercicio 3
""" num_superior = float(input("Introduce un límite superior: "))
num_inferior = float(input("Introduce un límite inferior: "))
num = float(input("Introduce un número a comparar: "))

if num > num_inferior and num < num_superior:
    print("{} se encuentra entre  {} y {}".format(num, num_inferior,num_superior))
else:
    print("{} está fuera del rango establecido".format(num)) """



#Ejercicio 4
""" 
animal = input("Ingresa tu animal favorito: ")

if animal == "Tortuga" or animal == "tortuga" or  animal == "TORTUGA":
    print("También me gustan las tortugas")
#elif animal == "tortuga":
#    print("También me gustan las tortugas")
#elif animal == "TORTUGA":
#    print("También me gustan las tortugas")
else:
    print("Ese animal es genial, pero prefiero las tortugas") """


# Ejercio 5

""" it_rain = input("Está lloviendo?: ")

if it_rain == "Sí" or it_rain == "Si" or it_rain == "si" or it_rain == "SI":
    viento = input("Está haciendo mucho viento?: ")
    if viento == "Sí" or viento == "Si" or viento == "si" or viento == "SI" :
        print("Hace mucho viento para salir con una sombrilla")
    else:
        print("Deberías llevar una sombrilla")
else:
    print("Que tengas un lindo día")

     """

# Ejercicio 6

""" edad = int(input("Ingrese su edad: "))

if edad >= 30:
    print("Nuncas es tarde para aprender. \n ¿Qué curso tomaremos?")
elif edad >= 18 and edad < 29:
    print("Es un momento excelente para impulsar tu carrera.")
else:
    print("¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte.") """


# Ejercicio 7

num = int(input("Indica un número entre 1 y 6: "))

if num == 1:
    print("Hoy aprenderemos sobre prorgamación")
elif num == 2:
    print("¿Qué tal tomar un curso de marketing digital?")
elif num == 3:
    print("Hoy es un gran día para comenzar a aprender de diseño")
elif num == 4:
    print("¿Y si aprendemos algo de negocios online?")
elif num == 5:
    print("Veamos un par de clases sobre producción audiovisual")
elif num == 6:
    print("Tal vez sea bueno desarrollar una habilidad blanda en Platzi")
else:
    print("Por favor, ingresa un número en el rango indicado")
