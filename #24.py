"""
#24 MÁXIMO COMÚN DIVISOR Y MÍNIMO COMÚN MÚLTIPLO   Medio #23 2022
/*
 * Crea dos funciones, una que calcule el máximo común divisor (MCD) y otra
 * que calcule el mínimo común múltiplo (mcm) de dos números enteros.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""
import math

# Opción 1: Esta opción puede ser la más fácil de entender.
def MCD(num1, num2):
    divisores_num1 = [num for num in range(1, num1 + 1) if num1 % num == 0] # Sacamos los divisores del primer número.
    divisores_num2 = [num for num in range(1, num2 + 1) if num2 % num == 0] # Sacamos los divisores del segundo número.

    for num in reversed(divisores_num1):    # Comprobamos bajando de mayor a menor los divisores de num1 y si alguno coincide y es divisor de num2 también, devolvemos ese número.
        if num in divisores_num2:
            return num
    return 1    # Esta línea no es necesaria porque al final el último número divisble será uno siempre, pero es buena práctica que las funciones siempre devuelvan un valor.

# Opción 2: Esta opción es la mejor y la más óptima.
def MCD(num1, num2):
    for num in range(min(num1, num2), 0, -1):   # Recorremos todos los números desde el menor de entre num1 y num2 hasta 1.
        if num1 % num == 0 and num2 % num == 0: # Si alguno es divisor de num1 y de num2, retornamos ese número.
            return num




# Opción 1: Esta opción puede ser la más sencilla para principiantes.
def mcm(num1, num2):
    for num in range(max(num1, num2), num1 * num2 + 1, +1): # Recorremos todos los números desde el mayor de los dos hasta num1 por num2, de uno en uno.
        if num % num1 == 0 and num % num2 == 0: # Si el número es múltiplo de ambos, entonces devolvemos dicho número.
            return num

# Opción 2: Esta opción es la mejor y la más elegante, aunque depende de la otra función.
def mcm(num1, num2):    # Hay una regla matemática que establece que el mínimo común múltiplo de dos números es igual a un número por el otro entre el máximo común divisor de los dos
    return (num1 * num2 // MCD(num1, num2))






# Aunque el reto no permite usar operaciones del lenguaje que lo resulven directamente, es conveniente saber cómo sería usando el módulo math
def MCD(num1, num2):
    return math.gcd(num1, num2)


def mcm(num1, num2):
    return abs(num1 * num2) // math.gcd(num1, num2)




# COMPROBACIONES
print(MCD(24, 36))   # -> 12
print(mcm(24, 36))   # -> 72
print(MCD(7, 13))    # -> 1
print(mcm(7, 13))    # -> 91
print(MCD(5, 15))    # -> 5
print(mcm(5, 15))    # -> 15