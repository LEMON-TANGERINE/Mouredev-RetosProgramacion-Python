"""
#14 FACTORIAL RECURSIVO   Fácil #13 2022
/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */
"""
# Para cumplir con la condición de hacerlo de forma recursiva lo que hay que hacer es definir una función que se llame a sí misma usando 2 partes principales: el caso base (que detiene la repetición) y el paso recursivo (donde el problema se hace más pequeño).
def factorial_recursivo(numero):
    if numero == 1 or numero == 0:
        return 1
    return numero * factorial_recursivo(numero - 1)

# El concepto de recursividad funciona como una muñeca rusa (matrioshka):
# Cada llamada abre una muñeca más pequeña hasta llegar al centro (el caso base).
# 
# Ejemplo con factorial_recursivo(3):
# 1. Abre capa 3 -> Espera a resolver 3 * factorial(2)
# 2. Abre capa 2 -> Espera a resolver 2 * factorial(1)
# 3. Llega al centro -> factorial(1) cumple el caso base y devuelve 1.
# 
# Ahora las muñecas se cierran devolviendo el valor hacia atrás:
# - Capa 2 se resuelve: 2 * 1 = 2
# - Capa 3 se resuelve: 3 * 2 = 6 (Resultado final)

# COMPROBACIONES
print(factorial_recursivo(0)) # -> 1
print(factorial_recursivo(1)) # -> 1
print(factorial_recursivo(4)) # -> 24: 1 x 2 x 3 x 4
print(factorial_recursivo(10))# -> 3628800: 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 x 10