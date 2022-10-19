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
    # Realizar una funcion lambda que eleve al cuadrado
    # el número pasado como parámetro

    # potencia_2 = lambda x:......
    # pot_3 = potencia_2(3)

    #1° Creo la función lambda

    potencia_2 = lambda x: x**2

    #2° Pregunto el número que será el parámetro 

    num = float(input("Ingrese un número para elevarlo al cuadrado:\n"))

    #3° Imprimo el cuadrado del número ingresado
    
    print("El cuadrado del número ingresado es:")
    print(potencia_2(num))
    print("Fin del primer ejercicio")


    # 2)
    # Utilice la función map para mapear una lambda expression
    # que retorne la potencia de 2 de cada numero en la lista numeros
    # El resultado (la potencia de cada numero) se debe ir almacenando
    # en una nueva lista
    # Nota: realizar la lambda expression "in line", es decir,
    # no declarar la lambda fuera del map sino diretamente dentro
    # Copiar la lambda creada en el paso anterior dentro del map
    # NOTA: No debe usar "potencia_2" dentro del map, debe colocar
    # directamente la lambda.

    print("Inicio segundo ejercicio")

    # Lista de numeros
    numeros = [1, -5, 4, 3]

    # numeros_potencia = list(map....)

    #Crearé la variable para almacenar la lista de los cuadrados de num
    #con la función map(función, datos) genero los valores

    pot_cuadrado = list(map(lambda x: x**2, numeros))

    #Otra opción
    
    pot_2 = list(map(potencia_2, numeros))      #Utilizo la función creada antes

    print("El cuadrado de los números en la variable lista es:")
    print(pot_cuadrado)
    

    print("terminamos")