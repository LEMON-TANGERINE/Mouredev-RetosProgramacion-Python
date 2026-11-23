"""
#25 ITERATION MASTER   Fácil #24 2022
/*
 * Quiero contar del 1 al 100 de uno en uno (imprimiendo cada uno).
 * ¿De cuántas maneras eres capaz de hacerlo?
 * Crea el código para cada una de ellas.
 */
"""
# bucle for:
for i in range(1, 101):
    print(i)

# bucle while:
cuenta = 1
while cuenta <= 100:
    print(cuenta)
    cuenta += 1

# Recursividad:
def contar(contador=1):
    if contador == 101:
        return
    print(contador)
    return contar(contador + 1)

contar()

# Clase:
class contador:
    def __init__(self, inicio, fin):
        self.inicio = inicio
        self.fin = fin

    def contar(self):
        for i in range(self.inicio, self.fin + 1):    # Aquí he usado un bucle for para el método pero se puede hacer de otras formas.
            print(i)

contador(1, 100).contar()

# itertools (módulo estándar de python)
from itertools import count, islice

for numero in islice(count(1), 100): # itertools.count(1) genera números consecutivos empezando desde el 1 de manera infinita. Para detenerlo en el 100 se envuelve en islice
    print(numero)