print("----- Divide la Cuenta -----")

#Funcion para obtener la cuenta a pagar por persona
def cuenta_de_la_cena():
    total_a_pagar = float(input("Ingrese la cuenta total:"))
    amigos = int(input("Ingrese el numero de personas: "))
    porcentaje_de_propina = float(input("Ingrese el porcentaje de propina: "))
    impuesto = 16.0
    Total = total_a_pagar + (total_a_pagar*porcentaje_de_propina/100) + (total_a_pagar*impuesto/100)

    print("El total es {}, incluye el {} % de impuestos y un {} % de propina".format(Total, impuesto, porcentaje_de_propina))

    print("\n")
    print("Cada cliente deberá pagaar: ", Total/amigos)

#Ejecutando la funcion
cuenta_de_la_cena()
