"""
#18 LA CARRERA DE OBSTÁCULOS   Medio #17 2022
/*
 * Crea una función que evalúe si un/a atleta ha superado correctamente una
 * carrera de obstáculos.
 * - La función recibirá dos parámetros:
 *      - Un array que sólo puede contener String con las palabras
 *        "run" o "jump"
 *      - Un String que represente la pista y sólo puede contener "_" (suelo)
 *        o "|" (valla)
 * - La función imprimirá cómo ha finalizado la carrera:
 *      - Si el/a atleta hace "run" en "_" (suelo) y "jump" en "|" (valla)
 *        será correcto y no variará el símbolo de esa parte de la pista.
 *      - Si hace "jump" en "_" (suelo), se variará la pista por "x".
 *      - Si hace "run" en "|" (valla), se variará la pista por "/".
 * - La función retornará un Boolean que indique si ha superado la carrera.
 * Para ello tiene que realizar la opción correcta en cada tramo de la pista.
 */
"""
def carrera_de_obstaculos(acciones, pista):
    if len(acciones) != len(pista): # Comprobamos que haya el mismo número de acciones que de obstáculos en la pista.
        print("El número de acciones tiene que ser igual al número de obstáculos en la pista.")
        return False

    if (    # any() recibe varios valores booleanos y devuelve True si al menos uno es True.
        any(accion not in ("run", "jump") for accion in acciones)   # Si alguna acción no es "run" o "jump" devuelve True.
        or any(obstaculo not in ("_", "|") for obstaculo in pista)  # Si algún obstáculo no es "_" o "|" devuelve True.
    ):
        print("Acción u obstáculo inválido.")
        return False    # Devuelve False si algun obstaculo o acción no es válida.

    fallos = {("jump", "_"): "x", ("run", "|"): "/"}    # Mapeo de errores según las reglas del reto.
    pista_final = "".join(fallos.get((accion, obstaculo), obstaculo) for accion, obstaculo in zip(acciones, pista)) # Recorremos la pista par a par (acción, tramo) y, si el diccionario detecta un fallo, pone 'x' o '/'; si no, deja el símbolo original y los une todos en un texto.

    print(pista_final)
    return pista_final == pista # La carrera se supera si la pista resultante es idéntica a la original.



# COMPROBACIONES
print(carrera_de_obstaculos(["run", "jump", "run", "jump"], "_|_|"))  # -> _|_| | True
print(carrera_de_obstaculos(["jump", "run", "jump", "run"], "_|_|"))  # -> x/x/ | False
print(carrera_de_obstaculos(["run", "jump", "run", "run"], "_|_|"))   # -> _|_/ | False
print(carrera_de_obstaculos(["run", "jump"], "_|_|"))                 # -> El número de acciones tiene que ser igual al número de obstáculos en la pista. | False
print(carrera_de_obstaculos(["fly", "jump"], "_|"))                   # -> Acción u obstáculo inválido. | False