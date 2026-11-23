"""
#16 ¿CUÁNTOS DÍAS?   Difícil #15 2022
/*
 * Crea una función que calcule y retorne cuántos días hay entre dos cadenas
 * de texto que representen fechas.
 * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
 * - La función recibirá dos String y retornará un Int.
 * - La diferencia en días será absoluta (no importa el orden de las fechas).
 * - Si una de las dos cadenas de texto no representa una fecha correcta se
 *   lanzará una excepción.
 */
"""
from datetime import datetime   # La librería datetime de Python proporciona clases para manipular fechas, horas e intervalos de tiempo de forma sencilla y precisa.


def cuantos_dias(fecha1: str, fecha2: str) -> int:  # Aclaramos que la función recibe dos strings y retorna un integer como indican las instrucciones.
    try:
        f1 = datetime.strptime(fecha1, "%d/%m/%Y")  # Crea una fecha con el formato dd/MM/yyyy.
        f2 = datetime.strptime(fecha2, "%d/%m/%Y")  # Crea la otra fecha.

        return abs((f2 - f1).days)  # Restar dos fechas de datetime devuelve la diferencia de días entre ambas fechas.
    except ValueError:              # Relanzamos la excepción con un mensaje personalizado para cumplir los requisitos del ejercicio.
        raise ValueError("Fecha inválida - Revise el formato (dd/MM/yyyy) y que la fecha exista.")

# COMPROBACIONES
print(cuantos_dias("03/02/2000", "01/01/2000")) # -> 33 
print(cuantos_dias("03/02/2000", "05/01/2000")) # -> 29
print(cuantos_dias("01/01/2000", "07/02/2000")) # -> 37
print(cuantos_dias("15/05/2023", "15/05/2023")) # -> 0 (misma fecha)
print(cuantos_dias("01/01/2024", "01/01/2025")) # -> 366 (2024 fue un año bisiesto)
print(cuantos_dias("01-01-2023", "01/01/2023")) # -> ValueError (Fecha inválida)