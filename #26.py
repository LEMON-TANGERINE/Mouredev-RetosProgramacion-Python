"""
#26 PIEDRA, PAPEL, TIJERA   Medio #25 2022
/*
 * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "R" (piedra), "P" (papel)
 *   o "S" (tijera).
 * - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
 */
"""
def ganador(partidas):  # La función recibirá una lista de tuplas donde R es piedra (rock), P es papel (paper) y S es tijeras (scissors).
    resultados_ganadores = {"R":"S", "S":"P", "P":"R"}  # Establecemos qué gana a qué: piedra gana a tijeras, papel a piedra...
    resultados = []

    for player1, player2 in partidas:   # En cada tupla, separamos entre la acción del Player 1 y la acción del Player 2.

        if player1 != player2:  # Solo si las jugadas son distintas se comprueba lo siguiente
            resultados.append("Player 1" if player2 == resultados_ganadores[player1] else "Player 2")   # Si la jugada de Player 1 gana a la del Player 2, entonces gana Player 1 y viceversa.

    return "Player 1" if resultados.count("Player 1") > resultados.count("Player 2") else ("Player 2" if resultados.count("Player 2") > resultados.count("Player 1") else "Tie")    # Gana el que haya ganado más veces, si han ganado las mismas veces entonces es empate.



# COMPROBACIONES
print(ganador([("R","S"), ("S","R"), ("P","S")]))     # -> Player 2
print(ganador([("R", "S"), ("P", "R"), ("S", "P")]))  # -> Player 1
print(ganador([("S", "R"), ("R", "P"), ("P", "S")]))  # -> Player 2
print(ganador([("R", "S"), ("S", "R"), ("P", "P")]))  # -> Tie