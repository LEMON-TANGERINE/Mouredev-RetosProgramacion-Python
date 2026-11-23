"""
#2 ¿ES UN ANAGRAMA?   Medio #1 2022
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""
def anagrama(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower()) if palabra1.lower() != palabra2.lower() else False

# Optimización teórica: Validar len(palabra1) == len(palabra2) descartaría casos al instante.
# Sin embargo, en la práctica, con palabras del diccionario, el ahorro de tiempo es invisible (nanosegundos).

# COMPROBACIONES
print(anagrama('Amor', 'ramo'))     # True
print(anagrama('frase', 'Fresa'))   # True
print(anagrama('Perro', 'Pero'))    # False
print(anagrama('riesgo', 'sergio')) # True
print(anagrama('Arroz', 'Zorro'))   # False
print(anagrama('Amor', 'amor'))     # False