# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Utilizar comprensión de listas con condicionales

    # 1)
    # Utilizar comprensión de listas para convertir
    # una lista de números como str en números tipo int
    # sería un conversor string --> int
    # Ojo! Tener cuidado con lo string/caracteres
    # que no son números, utilizar condicionales para detectarlos
    # reemplazar dicho str "no numérico" por 0
    # TIP: Recomendamos ver el método "isdigit" de strings
    # para aplicar en este caso.
    list_numeros_str = ['5', '2', '3', '', '7', 'NaN']

    #1° Creo la compresión por filtros

    lista_convertida = [int(x) if x.isdigit()  else 0 for x in list_numeros_str]

    #int() mi primer salida si cumple la condición
    #x.isdigit() condición - si es un dígito es verdadero
    #0 mi 2 salida si no cumple la condición
    #x item
    #list_numeros_str mi iteración
    
    #2° Imprimo la lista

    print("La lista tipo string que contenía números es: \n", lista_convertida)

  



    # ¿Ya terminaron el ejercicio? ¿Por qué no prueban
    # hacer negativo alguno de los números de la lista?
    # ¿Qué sucede con isdigit? Sorprendente no?
    #Si se convierte un "número" de la lista a negativo no lo reconoce como número, solo reconoce los naturales

    print("terminamos")