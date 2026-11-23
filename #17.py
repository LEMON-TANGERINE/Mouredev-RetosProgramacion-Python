"""
#17 EN MAYÚSCULA   Fácil #16 2022
/*
 * Crea una función que reciba un String de cualquier tipo y se encargue de
 * poner en mayúscula la primera letra de cada palabra.
 * - No se pueden utilizar operaciones del lenguaje que
 *   lo resuelvan directamente.
 */
"""
def mayusculas(texto):
    abecedario = {      # Creamos un diccionario con cada letra para después cambiarla por la letra correspondiente pero en su versión en mayúscula.
        "a": "A", "b": "B", "c": "C", "d": "D", "e": "E", "f": "F", 
        "g": "G", "h": "H", "i": "I", "j": "J", "k": "K", "l": "L", 
        "m": "M", "n": "N", "ñ": "Ñ", "o": "O", "p": "P", "q": "Q", 
        "r": "R", "s": "S", "t": "T", "u": "U", "v": "V", "w": "W", 
        "x": "X", "y": "Y", "z": "Z"
    }

    palabras_mayuscula = ""     # Aquí iremos añadiendo el resultado.
    palabras = texto.split()    # Creamos una lista de las palabras del texto.

    for posicion, palabra in enumerate(palabras):   # Iteramos cada palabra obteniendo también su índice para controlar los espacios entre palabras
            palabras_mayuscula += abecedario.get(palabra[0], palabra[0]) + palabra[1:] + (" " if posicion != len(palabras) - 1 else "") # Convertimos la primera letra si está en el diccionario, mantenemos el resto y añadimos un espacio si no es la última palabra

    return palabras_mayuscula

# COMPROBACIONES
print(mayusculas("no puedes detener las olas, pero puedes aprender a surfear.")) # -> No Puedes Detener Las Olas, Pero Puedes Aprender A Surfear.
print(mayusculas("que la fuerza te acompañe"))                                   # -> Que La Fuerza Te Acompañe
print(mayusculas("un gran Poder conlleva una gran responsabilidad."))            # -> Un Gran Poder Conlleva Una Gran Responsabilidad.
print(mayusculas("arriba arriba abajo abajo izquierda derecha b a"))             # -> Arriba Arriba Abajo Abajo Izquierda Derecha B A