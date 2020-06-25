
#nombre = input("Ingrese su nombre: ")
#apellido = input("Ingrese su apellido paterno: ")

#print("Hola, {} {}".format(nombre, apellido))


curso_platzi = """
    Platzi cuentacon cursos de: \n
    Desarrollo en Ingeniería
    Diseño y UX
    Marketing
    Negocios y Emprendimiento
    Producción Audiovisual
    Crecimiento Profesional
    """
#print(curso_platzi)


#num1 = float(input("Ingreso un numero: "))
#num2 = float(input("Ingrese otro numer: "))
#suma = num1 + num2
#print("Suma: ", round(suma,2))

#print("Ingrese tres numeros separados por coma: ")

#num1 = float(input("Ingrese un numero: "))
#num2 = float(input("Ingrese otro numero: "))
#num3 = float(input("Ingrese un numero mas: "))

#resultado = (num1+num2)*num3
#print(round(resultado, 2))


#rebanadas = int(input("Ingresar rebandas de pizzas: "))

#print("Se comieron 5 rebandas")

#y = 5

#print("Entonces, quedan {}".format(rebanadas-y))



#name = input("Ingrese su nombre: ")
#age = int(input("Ingrese su edad: "))

#print("{} el año pasado tenías {} y el próximo año cumplirás {}".format(name, age, age + 1))


def cuenta_de_la_cena():
    total_a_pagar = float(input("Ingrese el total a pagar: "))
    amigos = int(input("Ingrese el numero de personas: "))
    porcentaje_de_propina = float(input("Ingrese el procentaje de propina: "))
    impuesto = 16.0
    Total = total_a_pagar + (total_a_pagar*porcentaje_de_propina/100) + (total_a_pagar*impuesto/100)
    print("El total es {}, inclueye el {} % de impuestos y un {} % de propina".format(Total, impuesto, porcentaje_de_propina))
    print("Cada cliente deberá pagar: ", Total/amigos)

#cuenta_de_la_cena()

def cuantas_horas():
    dias = int(input("Introduce cierta cantidad de días: "))
    horas = dias*60
    minutos = horas*60
    segundos = minutos*60

    print("{} dias tiene {} horas, {} minutos y {} segundos".format(dias, horas, minutos, segundos))

#cuantas_horas()


def millas_a_km():
    """
    Convertidor de millas a kilometros
    1milla = 1.609344 km
    """

    UNA_MILLA = 1.609344

    millas = float(input("Introduce una cantidad de millas: "))

    km = millas*UNA_MILLA
    print("{} millas son {} kilometros".format(millas, km))

#millas_a_km()


def cuantas_Veces():
    """
    Este programa regresa cuantas veces caben un numero menor a 100 
    en un numero mayor a 1000
    """
    mayor = int(input("Introduce un numero mayor a 1000: "))
    menor = int(input("Introduce un numero menor a 100: "))

    print(mayor // menor)


cuantas_Veces()
