# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Utilizar comprensión de listas para filtrar

    accesos = [10, 50, 7, 5, 15, 25, 3, 4, 13]

    # La lista accesso contiene los números de ID de personal
    # que ingresaron por ese molinete

    # 1)
    # Generar una lista por comprensión de la lista "accesos"
    # una lista que solo contenga (filtrado) los ID de personal
    # entre 1 al 10 inclusive, se desea separar del grupo de accesos
    # los ID entre el 1 y 10.
    # De la lista resultante informar cuantas personas/personal
    # comprendido en dicho rango pasó por ese molinete

    print("Inicio del primer ejercicio")

    # personal_1_10 = [.....]

    #1° Genero la comprensión

    personal_1_10 = [x for x in accesos if (x < 11)]

    #Primera x es mi salida 
    #Segunda x es mi item
    #accesos es donde itero
    #if es la condición que se debe cumplir para que tenga salida

    #2° Imprimo la cantidad de personas que paso por el molinete en el rango del 1 al 10

    print("La cantidad de personas que pasaron por el molinente con ID entre 1 y 10 fueron:\n", len(personal_1_10))
    print("Los ID de las personas que pasaron son:\n", personal_1_10)


    print("Fin del primer ejercicio")

    # 2)
    # Generar una lista por comprensión de la listas "accesos"
    # cuyo ID de personal esté dentro de los ID válidos para ingresar
    # por ese molinete:
    id_validos = [3, 4, 7, 8, 15]
    # Debe generar una nueva lista basada en "accesos" filtrada por los ID
    # aprobados en "id_validos".
    # TIP: Utilizar el operador "in" para chequear si un ID de accesos está
    # dentro de "id_validos"

    print("Inicio del segundo ejercicio")

    # personal_valido = [.....]

    #1° Genero la compresión

    personal_valido = [x for x in personal_1_10 if x in id_validos]

    #Primera x mi salida
    #Segunda x mi item 
    #personal_1_10 lista que recorro/itero
    #x in id_validos verifico si mi item se encuentra en la lista id_validos

    print("Los ID entre 1 y 10 que pasaron por el molinete, solamente los siguientes estaban aprobados:\n", personal_valido)
    print("Fin del segundo ejercicio")
    print("terminamos")