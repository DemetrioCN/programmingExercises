palabra = input("Introduce una palabra: ")

consonantes = 'bcdfghjklmnpqrstvwxyz'
consonantes = consonantes.join(consonantes.upper())

vocales = 'aeiou'
vocales = vocales.join(vocales.upper())

if palabra[0] in consonantes:
    print(palabra[1:] + palabra[0] + "ay")
elif palabra[0] in  vocales:
    print(palabra + "way")