"""
#8 CONTANDO PALABRAS   Medio #7 2022
/*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
"""
def contar_palabras(texto):
    recuento = {}

    for signo in ",.¿?¡!()-;":
        texto = texto.replace(signo, "")

    palabras = texto.lower().split()

    for palabra in palabras:
        recuento[palabra] = recuento.get(palabra, 0) + 1

    return recuento, f"Total: {len(palabras)} palabras"

# Esto es opcional, pero hace que la salida sea un poco más limpia.
recuento, total = contar_palabras("¡Hola! ¿Hola? Hola... Hola, hola; (hola) -hola-.")
print(recuento)
print(total)
recuento, total = contar_palabras("Python python PYTHON PyThOn pYtHoN")
print(recuento)
print(total)
recuento, total = contar_palabras("Caminante, no hay camino, se hace camino al andar. Al andar se hace el camino y al volver la vista atrás se ve la senda que nunca se ha de volver a pisar.")
print(recuento)
print(total)
recuento, total = contar_palabras("Hola     qué    tal      todo    bien")
print(recuento)
print(total)