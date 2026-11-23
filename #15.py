"""
#15 ¿ES UN NÚMERO DE ARMSTRONG?   Fácil #14 2022
/*
 * Escribe una función que calcule si un número dado es un número de Armstrong
 * (o también llamado narcisista).
 * Si no conoces qué es un número de Armstrong, debes buscar información
 * al respecto.
 */
"""
# Un número de Armstrong / número narcisista es un número entero que es igual a la suma de cada uno de sus dígitos elevados a la potencia del número total de cifras que lo componen
# Ej: el 153 es un número de Armstrong porque 1³ + 5³ + 3³ = 153

def armstrong(numero):
    str_numero = str(numero)    # Transformamos el número en string para poder recorrer cada dígito con for.
    return sum(int(n) ** len(str_numero) for n in str_numero) == numero # Miramos si la suma de cada dígito elevado al número total de dígitos es igual al numero incial, en cuyo caso es un número de Armstrong.


# COMPROBACIONES
print(armstrong(1))     # -> True
print(armstrong(10))    # -> False
print(armstrong(100))   # -> False
print(armstrong(370))   # -> True
print(armstrong(407))   # -> True
print(armstrong(1635))  # -> False