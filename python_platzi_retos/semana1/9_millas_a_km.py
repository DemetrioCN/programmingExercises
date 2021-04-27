print("--- Convertidor de millas a KM ---")

def millas_a_km():
    """
    Convertidor de millas a kilometrs
    1 milla = 1.609344 km
    """

    UNA_MILLA = 1.609344

    millas = float(input("Introduce una cantidad de millas: "))

    km = millas*UNA_MILLA

    print("{} millas son {} kilometros".format(millas, round(km,2)))


# Ejecutando la funcion
millas_a_km()
