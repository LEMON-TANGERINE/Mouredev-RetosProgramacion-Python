"""
#11 EXPRESIONES EQUILIBRADAS   Medio #10 2022
/*
 * Crea un programa que comprueba si los paréntesis, llaves y corchetes
 * de una expresión están equilibrados.
 * - Equilibrado significa que estos delimitadores se abren y cieran
 *   en orden y de forma correcta.
 * - Paréntesis, llaves y corchetes son igual de prioritarios.
 *   No hay uno más importante que otro.
 * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
 * - Expresión no balanceada: { a * ( c + d ) ] - 5 }
 */
"""
def expresion_equilibrada(expresion):
        abierto = []
        cierre_apertura =   {
                            "}": "{",
                            "]": "[",
                            ")": "("
                            }

        for letra in expresion:
            if letra in "{[(":              # Si la letra es un símbolo de apertura, lo añadimos a la lista de abiertos.
                abierto.append(letra)

            elif letra in cierre_apertura:                                  # Si la letra es un símbolo de cierre,
                if not abierto or abierto[-1] != cierre_apertura[letra]:    # Si no hay ningún símbolo abierto o el último abierto no corresponde con este cierre, la expresión no está equilibrada.
                    return False                                           
                abierto.pop()                                               # En caso contrario, este cierre es correcto, así que eliminamos de la pila el último símbolo de apertura.

        return not abierto   # Si la lista está vacía quiere decir que la expresion está equilibrada


# COMPROBACIONES
print(expresion_equilibrada("{[ a * (c + d) ] - 5 }"))   # -> True
print(expresion_equilibrada("{ a * (c + d) ] - 5 }"))    # -> False
print(expresion_equilibrada("([{}])"))                    # -> True
print(expresion_equilibrada("([)]"))                      # -> False
print(expresion_equilibrada("((a + b))"))                 # -> True
print(expresion_equilibrada("((a + b)"))                  # -> False
print(expresion_equilibrada(")a+b("))                     # -> False
print(expresion_equilibrada("a + b"))                     # -> True
print(expresion_equilibrada(""))                          # -> True