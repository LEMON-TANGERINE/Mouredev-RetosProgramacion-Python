"""
#10 CÓDIGO MORSE   Medio #9 2022
/*
 * Crea un programa que sea capaz de transformar texto natural a código
 * morse y viceversa.
 * - Debe detectar automáticamente de qué tipo se trata y realizar
 *   la conversión.
 * - En morse se soporta raya "—", punto ".", un espacio " " entre letras
 *   o símbolos y dos espacios entre palabras "  ".
 * - El alfabeto morse soportado será el mostrado en
 *   https://es.wikipedia.org/wiki/Código_morse.
 */
"""
def morse_texto(texto):
    # Creamos un diccionario que relaciona cada carácter con su representación en código morse, incluido el espacio, que son 2 espacios en morse.
    texto_a_morse = {
                    "a" : ".—",
                    "b" : "—...",
                    "c" : "—.—.",
                    "ch" : "————",
                    "d" : "—..",
                    "e" : ".",
                    "f" : "..—.",
                    "g" : "——.",
                    "h" : "....",
                    "i" : "..",
                    "j" : ".———",
                    "k" : "—.—",
                    "l" : ".—..",
                    "m" : "——",
                    "n" : "—.",
                    "ñ" : "——·——",
                    "o" : "———",
                    "p" : ".——.",
                    "q" : "——.—",
                    "r" : ".—.",
                    "s" : "...", 
                    "t" : "—",
                    "u" : "..—",
                    "ü" : "··——",
                    "v" : "...—",
                    "w" : ".——",
                    "x" : "—..—",
                    "y" : "—.——",
                    "z" : "——..",
                    "1" : ".————",
                    "2" : "..———",
                    "3" : "...——",
                    "4" : "....—",
                    "5" : ".....",
                    "6" : "—....",
                    "7" : "——...",
                    "8" : "———..",
                    "9" : "————.",
                    "0" : "—————",
                    " " : "  ",
                    "," : "——..——",
                    "?" : "..——..",
                    '"' : ".—..—.",
                    "/" : "—..—."
                    }

    resultado = ""
    posicion = 0
    morse_a_texto = {valor: clave for clave, valor in texto_a_morse.items()}    # Creamos un diccionario inverso para acceder a la letra a partir del código morse directamente.

    # Comprobamos si es código morse o texto normal.
    if "—" in texto or "  " in texto or "." in texto:   # Si es código morse: pasarlo a texto normal.
        for posicion, palabra in enumerate(texto.split("  ")):
            for letra in palabra.split(" "):
                resultado += morse_a_texto[letra]

            resultado += " " if posicion + 1 < len(texto.split("  ")) else "" # Añadimos el espacio entre palabras, pero solo si no es la última palabra.



    else:   # Si es texto normal: pasarlo a código morse.
        while posicion < len(texto):
            letra = texto.lower()[posicion]

            # Comprobar si se trata de "ch" o solo "c".
            if posicion + 1 < len(texto) and letra == "c" and texto.lower()[posicion + 1] == "h":
                if posicion + 2 < len(texto):
                    resultado += texto_a_morse["ch"] + " " if texto.lower()[posicion + 2] != " " else texto_a_morse["ch"]   # Añadimos un espacio entre letra y letra, pero solo si no es la ultima letra de la ultima palabra.
                else:
                    resultado += texto_a_morse["ch"]
                posicion += 2   # Para indicar la siguiente letra después de ch.

            else:
                if letra == " ":
                    resultado += texto_a_morse[letra]
                elif posicion + 1 < len(texto):
                    resultado += texto_a_morse[letra] + " " if texto.lower()[posicion + 1] != " " else texto_a_morse[letra] # Si ni es un espacio, ni se trata de la última letra, ni la siguiente letra es un espacio, entonces añade la letra con un espacio para separar letra y letra.
                else:
                    resultado += texto_a_morse[letra]
                posicion += 1   # Para indicar la siguiente letra.

    return resultado


# COMPROBACIONES
print(morse_texto("May the force be with you"))                                 # -> —— .— —.——  — .... .  ..—. ——— .—. —.—. .  —... .  .—— .. — ....  —.—— ——— ..—
print(morse_texto("The Eyes Chico, they Never Lie"))                            # -> — .... .  . —.—— . ...  ———— .. —.—. ——— ——..——  — .... . —.——  —. . ...— . .—.  .—.. .. .
print(morse_texto("Bond, James Bond"))                                          # -> —... ——— —. —.. ——..——  .——— .— —— . ...  —... ——— —. —..
print(morse_texto(".—— .... —.——  ... ———  ... . .—. .. ——— ..— ... ..——.."))   # -> "why so serious?"
print(morse_texto("—.—. .— .—. .——. .  —.. .. . ——"))                           # -> "carpe diem"