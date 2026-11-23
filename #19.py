"""
#19 TRES EN RAYA   Difícil #18 2022
/*
 * Crea una función que analice una matriz 3x3 compuesta por "X" y "O"
 * y retorne lo siguiente:
 * - "X" si han ganado las "X"
 * - "O" si han ganado los "O"
 * - "Empate" si ha habido un empate
 * - "Nulo" si la proporción de "X", de "O", o de la matriz no es correcta.
 *   O si han ganado los 2.
 * Nota: La matriz puede no estar totalmente cubierta.
 * Se podría representar con un vacío "", por ejemplo.
 */
"""
def tres_en_raya(matriz):
    if len(matriz) > 3 or any(len(fila) != 3 for fila in matriz):   # Comprobamos que hayan 3 filas en la matriz y 3 fichas en cada fila.
        return "Nulo"

    total_x = sum(fila.count("X") for fila in matriz)   # Calculamos el número total de fichas X.
    total_o = sum(fila.count("O") for fila in matriz)   # Calculamos el número total de fichas O.

    if abs(total_x - total_o) > 1:  # Comprobamos que no haya un número inválido de fichas de cada tipo.
        return "Nulo"

    tres_en_raya = [] # En esta lista iremos añadiendo las fichas que han hecho 3 en raya

    for columna in range(3): # Miramos cada columna.
        if matriz[0][columna] == matriz[1][columna] == matriz[2][columna] and matriz[0][columna] != "": # Comprobamos si en cada columna las tres fichas son iguales y que no esté vacía la columna.
            tres_en_raya.append(f"{matriz[0][columna]}")   # Añadimos la ficha del que hizo 3 en raya.

    for fila in matriz: # Miramos cada fila.
        if fila[0] == fila[1] == fila[2] and fila[0] != "": # Comprobamos si en cada fila las tres fichas son iguales y que no esté vacía la fila.
            tres_en_raya.append(f"{fila[0]}") # Añadimos la ficha del que hizo 3 en raya.

    if matriz[0][0] == matriz[1][1] == matriz[2][2] and matriz[0][0] != "": # Miramos cada fila y comprobamos la diagonal de arriba a la izquierda a abajo a la derecha.
            tres_en_raya.append(f"{matriz[0][0]}")

    if matriz[0][2] == matriz[1][1] == matriz[2][0] and matriz[0][2] != "": # Miramos cada fila y comprobamos la diagonal de arriba a la derecha a abajo a la izquierda.
            tres_en_raya.append(f"{matriz[0][2]}")

    if not tres_en_raya:    # Si la lista está vacía significa que no ha ganado nadie, entonces es empate.
        return "Empate"
    elif len(set(tres_en_raya)) > 1:    # Si la lista tiene más de un ganador es nulo.
        return "Nulo"
    return tres_en_raya[0]  # Si ni es empate ni los dos han ganado entonces devolvemos el ganador.


# COMPROBACIONES
print(tres_en_raya( [   # -> "X"
    ["X", "X", "X"],
    ["O", "O", ""],
    ["", "", ""]
]))
print(tres_en_raya([    # -> "O"
    ["O", "X", ""],
    ["X", "O", ""],
    ["X", "", "O"]
]))
print(tres_en_raya([    # -> "Empate"
    ["X", "O", "X"],
    ["X", "O", "O"],
    ["O", "X", "X"]
]))
print(tres_en_raya([    # -> "Nulo"
    ["X", "X", "X"],
    ["X", "O", ""],
    ["", "", ""]
]))
print(tres_en_raya([    # -> "Nulo"
    ["X", "X", "X"],
    ["O", "O", "O"],
    ["", "", ""]
]))