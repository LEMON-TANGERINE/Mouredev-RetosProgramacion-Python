"""
#7 INVIRTIENDO CADENAS   Fácil #6 2022
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
"""
# Podemos resolver este ejercicio de varias formas distintas. Aunque aquí muestro 4 enfoques distintos, existen muchas otras formas de resolverlo (usando recursividad, usando pilas, etc.).

# OPCIÓN 1: Concatenación con índice negativo
# Se recorren los índices del final al principio usando el rango en negativo y concatenando cadenas directamente.
def invertir(texto):
    texto_invertido = ""
    for l in range(1, len(texto) + 1):
        texto_invertido += texto[-l]
    return texto_invertido

print(invertir("Hola mundo"))


# OPCIÓN 2: Acumulación invertida carácter a carácter
# Se itera sobre cada letra y se antepone al resultado acumulado para invertir el orden de forma intuitiva.
def invertir(texto):
    texto_invertido = ""
    for l in texto:
        texto_invertido = l + texto_invertido
    return texto_invertido

print(invertir("Hola mundo"))


# OPCIÓN 3: Generación y join con range inverso (ESTA ES LA SOLUCIÓN IDEAL)
# Se usa un generador que recorre los índices hacia atrás mediante range(inicio, fin, paso) y une los caracteres con .join().
def invertir(texto):
    return "".join(texto[i] for i in range(len(texto) - 1, -1, -1))

print(invertir("Hola mundo"))


# OPCIÓN 4: Uso de lista mutable y .join()
# Se almacena cada carácter invertido en una lista usando .append() para evitar la concatenación ineficiente de cadenas de la opción 1, y al final se unifica con .join().
def invertir(texto):
    texto_invertido = []
    for l in range(1, len(texto) + 1):
        texto_invertido.append(texto[-l])
    return "".join(texto_invertido)

print(invertir("Hola mundo"))