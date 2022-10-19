# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas

import random       #Necesario para el 3 ejercicio



if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Práctica de comprensión de listas
    # 1)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá tener un tamaño de 11
    # números, conteniendo del 0 al 10 inclusive

    # lista_0_10 = [......]

    print("Inicio del primer ejercicio")

    #1° Creo la lista de comprensión

    lista_0_10 = [x for x in range(11)]

    #Primera x es mi expresión
    #Segunda x es mi item
    #range() es mi iteración

    #2° Imprimo la lista

    print("Los números desde 0 a 10 son: \n", lista_0_10)

    print("Fin del primer ejercicio")

    
    # 2)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá contener la tabla del 5,
    # desde el múltiplo 0 al múltiplo 10
    # El resultado esperado es:
    # [0 5 10 15 20 25 30 35 40 45 50]
    # Utilizar comprensión de listas para generar essa lista
    # Lo esperable es que realicen una lista de 11 elementos,
    # del 0 al 10 (como el ejer anterior) pero que cada
    # elemento lo multipliquen x5.

    # tabla_5 = [......]

    print("Inicio del segundo ejercicio")

    #1° Genero la lista de comprensión

    tabla_5 = [x*5 for x in range(11)]

    #x*5 es mi expresión
    #x es mi item
    #range() es mi iteración

    #2° Imprimo la tabla de 5

    print("La tabla del 5 desde 0 hasta 10 es:\n", tabla_5)

    print("Fin del segundo ejercicio")

    # 3)
    # Generar una lista a partir de comprensión de listas,
    # esta lista generada deberá contener 10 números aleatorios,
    # estos números deberán estar entre el rango 1 al 30 representando
    # números posibles de un mes (los números pueden repetirse).
    # NOTA: Importar el módulo random y utilizar randrange
    # o randint para generar números aleatorios.
    # https://docs.python.org/3/library/random.html

    print("Inicio del tercer ejercicio")

    # dias_mes = [.....]

    #1° Genero la lista de comprensión

    dias_mes = [random.randint(1,31) for x in range (10)]

    #random.randit() es mi expresión
    #x es mi item
    #range() es mi iteración

    #Otra opción sería

    #dias_mes_1 = [random.randrange(1,31,1) for x in range(10)]

    #random.randrange(a, b, c)
    #a: inicio, b: fin, c: salto

    #2° Imprimo la lista aleatoria

    print("Los 10 números aleatorios posibles dentre de un mes son:\n", dias_mes)
    

    print("terminamos")