"""
#3 LA SUCESIÓN DE FIBONACCI   Difícil #2 2022
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
"""
n1, n2 = 0, 1

for _ in range(50):
    print(n1)
    n1, n2 = n2, n1 + n2

# Explicación paso a paso:
#   VUELTA 1
#   print(0)
#   n1, n2 = 1, 0 + 1

#   VUELTA 2
#   print(1)
#   n1, n2 = 1, 1 + 1

#   VUELTA 3
#   print(1)
#   n1, n2 = 2, 3