# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con lambda


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Lambda expression
    # 1)
    # Realizar una funcion lambda que retorne el tamaño
    # (len) de un string pasado como parámetro

    # len_string = lambda......

    #1° Creo la función lambda

    len_string = lambda x: len(x)

    #2° Pregunto el string que que desea ingresar para saber su extensión 

    string = str(input("Ingrese la palabra que desea saber su longitud:\n"))

    #3° Imprimo la longitud de la palabra ingresada
    
    print("La longitud de la palabra ingresada es:")
    print(len_string(string))
    print("Fin del primer ejercicio")

    # 2)
    # Lista de string
    palabras = ['Inove', 'casa', 'programacion']

    print("Inicio del segundo ejercicio")
    # Utilice la función map para mapear una lambda expression
    # que retorne el tamaño (len) de cada texto em cata iteración
    # de la lista de textos
    # El resultado (el len de cada palabra) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line"
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "len_string" dentro del map, debe colocar
    # directamente la lambda.

    # palabras_len = list(map....)

    #1° Creo la variable que me almacenará la longitud

    palabras_len = list(map(lambda x: len(x), palabras))

    #2 Imprimo por pantalla la longitud de cada palabra

    print("La longitud de cada palabra de la lista:")
    print(palabras, "es")
    print(palabras_len, "respectivamente")


    print("terminamos")