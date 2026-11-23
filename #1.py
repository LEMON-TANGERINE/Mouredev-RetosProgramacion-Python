"""
#1 EL FAMOSO "FIZZ BUZZ"   Fácil #0 2022
/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
"""

for n in range(1, 101):
    output = ""
    if n % 3 == 0:
        output += "fizz"
    if n % 5 == 0:
        output += "buzz"

    print(output or n)