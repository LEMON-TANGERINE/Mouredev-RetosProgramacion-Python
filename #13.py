"""
#13 ¿ES UN PALÍNDROMO?   Medio #12 2022
/*
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 */
"""
import unicodedata

def es_palindromo(texto):
    texto = "".join(c for c in unicodedata.normalize('NFD', texto.lower()) if unicodedata.category(c) != 'Mn' and c.isalnum())
    # unicodedata.normalize('NFD', texto.lower()) separa letras con tilde en la letra sin tilde + tilde flotante. Este proceso se aplica al texto en minúsculas.
    # Después, en if unicodedata.category(c) != 'Mn', category(c) nos dice qué tipo de carácter es cada letra, 'Mn' significa Mark, Nonspacing. Por eso descarta las tildes flotantes.
    # Y finalmente c.isalnum() se queda solo con las letras y los números, y elimina automáticamente cualquier signo de puntuación y espacios.

    return texto == texto[::-1] # Comprueba si el texto es igual al texto al revés, en tal caso, es palíndromo.

# --- COMPROBACIONES ---
print(es_palindromo("Ana lleva al oso la avellana."))       # -> True
print(es_palindromo("Dábale arroz a la zorra el abad."))    # -> True
print(es_palindromo("Python"))                              # -> False