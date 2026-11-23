"""
#4 ¿ES UN NÚMERO PRIMO?   Medio #3 2022
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""
print(2)
for i in range(3, 101):
    for t in range(2, int(i**0.5) + 1): # Pongo i elevado a 0.5 (o a 1/2) porque ningun número tiene divisores propios mayores a su raíz cuadrada. Y el + 1 por cómo funciona la función range()
        if i % t == 0:
            break
    else: # Se pueden usar bucles for con un else para solo ejecutar algo si el bucle for se completo entero sin ser interrumpido por un break
        print(i)