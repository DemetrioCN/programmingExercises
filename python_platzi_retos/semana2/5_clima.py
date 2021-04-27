it_rain = input("Está lloviendo?: ")

if it_rain == "Sí" or it_rain == "Si" or it_rain == "si" or it_rain == "SI":
    viento = input("Está haciendo mucho viento?: ")
    if viento == "Sí" or viento == "Si" or viento == "si" or viento == "SI" :
        print("Hace mucho viento para salir con una sombrilla")
    else:
        print("Deberías llevar una sombrilla")
else:
    print("Que tengas un lindo día")