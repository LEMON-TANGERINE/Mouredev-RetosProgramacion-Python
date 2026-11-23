"""
#12 ELIMINANDO CARACTERES   Fácil #11 2022
/*
 * Crea una función que reciba dos cadenas como parámetro (str1, str2)
 * e imprima otras dos cadenas como salida (out1, out2).
 * - out1 contendrá todos los caracteres presentes en la str1 pero NO
 *   estén presentes en str2.
 * - out2 contendrá todos los caracteres presentes en la str2 pero NO
 *   estén presentes en str1.
 */
"""
# Esta es la forma más sencilla y probablemente la mejor, no obstante, también se puede hacer con bucle for con if, expresiones regulares, filter(), etc.
def eliminar_caracteres(str1, str2):
    out1 = "".join(set(str1) - set(str2)) # Convertimos en sets para que no haya letras repetidas y restamos para quedarnos solo con aquellas que solo aparecen en str1.
    out2 = "".join(set(str2) - set(str1)) # Lo mismo pero para sacar aquellas letras que solo aparecen en str2.

    print(f"out1 (caracteres presentes en {str1} pero NO en {str2}): {out1}")
    print(f"out1 (caracteres presentes en {str2} pero NO en {str1}): {out2}")


# COMPROBACIONES
eliminar_caracteres('perro','peras')
eliminar_caracteres('gato','raton')
eliminar_caracteres('casa','lolo')
eliminar_caracteres('banana','manzana')
eliminar_caracteres('python','python')