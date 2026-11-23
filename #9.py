"""
#9 DECIMAL A BINARIO   Fácil #8 2022
/*
 * Crea un programa que se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
 */
"""
#  "Decimal" no significa que tenga coma o punto flotante, sino que pertenece al sistema numérico decimal (Base 10).

# Con una lista:
def decimal_a_binario(decimal):
    if decimal == 0:
        return 0

    binario = []
    while decimal > 0:
        binario.append(decimal % 2)
        decimal //= 2

    return "".join(str(n) for n in binario[::-1])



# Con un string normal
def decimal_a_binario(decimal):
    binario = ""

    while decimal > 0:
        binario += str(decimal % 2)
        decimal //= 2

    return binario[::-1] or "0"



# Con divmod(). divmod(decimal, 2) hace decimal // 2 y decimal % 2 al mismo tiempo
def decimal_a_binario(decimal):
    if decimal == 0:
        return "0"

    binario = []

    while decimal:
        decimal, resto = divmod(decimal, 2)
        binario.append(str(resto))

    return "".join(reversed(binario))