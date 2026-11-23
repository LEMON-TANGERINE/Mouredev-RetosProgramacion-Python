"""
#20 CONVERSOR TIEMPO   Fácil #19 2022
/*
 * Crea una función que reciba días, horas, minutos y segundos (como enteros)
 * y retorne su resultado en milisegundos.
 */
"""
def tiempo_a_milisegundos(dias, horas, minutos, segundos):
    return dias * 86400000 + horas * 3600000 + minutos * 60000 + segundos * 1000    # En un segundo hay 1000 milisegundos, de ahí ya podemos calcular cuántos milisegundos hay en un día, una hora y un minuto.


# COMPROBACIONES
print(tiempo_a_milisegundos(1, 0, 0, 0))    # -> 86400000
print(tiempo_a_milisegundos(0, 5, 0, 0))    # -> 18000000
print(tiempo_a_milisegundos(0, 0, 15, 0))   # -> 900000
print(tiempo_a_milisegundos(0, 2, 30, 15))  # -> 9015000