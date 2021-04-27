print("-- Calculando días --")

def cuantas_horas():
    dias = int(input("Introduce el numero de dias: "))
    horas = dias*60
    minutos = horas*60
    segundos = minutos*60

    print("{} dias tiene {} horas, {} minutos y {} segundos".format(dias, horas, minutos, segundos))

#Llamar a la función
cuantas_horas()
