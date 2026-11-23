"""
#23 CONJUNTOS   Fácil #22 2022
/*
 * Crea una función que reciba dos array, un booleano y retorne un array.
 * - Si el booleano es verdadero buscará y retornará los elementos comunes
 *   de los dos array.
 * - Si el booleano es falso buscará y retornará los elementos no comunes
 *   de los dos array.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""
# En python no existen los arrays, lo más parecido a un array es una lista
def conjuntos(array1: list, array2: list, booleano: bool) -> list:
    if booleano:
        return [item for item in set(array1) if item in array2]

    lista1 = [item for item in set(array1) if item not in array2]
    lista2 = [item for item in set(array2) if item not in array1]
    return lista1 + lista2


# Esta sería la solución utilizando operaciones de python que lo resuelven directamente, pero el reto no lo permite.
def conjuntos(array1, array2, booleano):
    if booleano:
        return [set(array1).intersection(set(array2))]   # O lo que es lo mismo [set(array1) & set(array2)]
    return [set(array1).symmetric_difference(set(array2))]  # O lo que es lo mismo [set(array1) ^ set(array2)]



# COMPROBACIONES
print(conjuntos([1, 2, 3, 4], [3, 4, 5, 6], True))      # -> [3, 4]
print(conjuntos([1, 2, 3, 4], [3, 4, 5, 6], False))     # -> [1, 2, 5, 6]
print(conjuntos([1, 1, 2, 2, 3], [2, 3, 3, 4], True))   # -> [2, 3]
print(conjuntos([1, 2], [3, 4], True))                  # -> []
print(conjuntos([1, 2, 3], [1, 2, 3], False))           # -> []
print(conjuntos([], [], True))                          # -> []