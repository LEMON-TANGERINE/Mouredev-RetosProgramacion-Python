"""
#22 CALCULADORA .TXT   Medio #21 2022
/*
 * Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
 * resultado e imprímelo.
 * - El .txt se corresponde con las entradas de una calculadora.
 * - Cada línea tendrá un número o una operación representada por un
 *   símbolo (alternando ambos).
 * - Soporta números enteros y decimales.
 * - Soporta las operaciones suma "+", resta "-", multiplicación "*"
 *   y división "/".
 * - El resultado se muestra al finalizar la lectura de la última
 *   línea (si el .txt es correcto).
 * - Si el formato del .txt no es correcto, se indicará que no se han
 *   podido resolver las operaciones.
 */
"""
# Opción recomendada. Hace las operaciones de forma secuencial, sin seguir la jerarquía de las operaciones.
def resolver_calculadora():
    try:
        with open("Challenge22.txt", "r", encoding="utf-8") as archivo:
            lineas = [linea.strip() for linea in archivo]   # Usamos el .strip() para eliminar saltos de línea sueltos.

        if len(lineas) % 2 == 0 or not lineas:  # Si hay algún signo suelto inválido o si está vacía se produce un error
            raise ValueError("Formato incorrecto: Número impar de líneas requerido.")

        resultado = float(lineas[0])    # Cogemos el primer número como base.

        for i in range(1, len(lineas), 2):  # Recorremos desde el índice 1 hasta el final, saltando de 2 en 2.
            operador = lineas[i]
            siguiente_numero = float(lineas[i+1])

            if operador == "+": # Comprobamos qué signo es y aplicamos la operación del número que ya tenemos con el siguiente.
                resultado += siguiente_numero
            elif operador == "-":
                resultado -= siguiente_numero
            elif operador == "*":
                resultado *= siguiente_numero
            elif operador == "/":
                resultado /= siguiente_numero
            else:
                raise ValueError("Operador no válido.")

        print(resultado)

    except (FileNotFoundError, ValueError, ZeroDivisionError, IndexError):  # Si no se ha podido abrir el archivo o hay algún error, se produce un error
        print("No se han podido resolver las operaciones debido a un error en el formato del archivo.")

resolver_calculadora()



# Opción con eval(). No recomendada pero es conveniente saber que es posible hacerlo así también. Hace las operaciones siguiendo la jerarquía de las operaciones.
def resolver_calculadora():
    try:
        with open("Challenge22.txt", "r", encoding="utf-8") as archivo:
            lineas = [linea.strip() for linea in archivo]

        if len(lineas) % 2 == 0 or not lineas:
            raise ValueError("Formato incorrecto: Número impar de líneas requerido.")

        print(eval("".join(lineas)))    # eval() es capaz de hacer todas las operaciones de un string. Por ejemplo: eval("1+3-2") daría 2, sin embargo, es mejor evitar el uso de eval() para
                                        # prevenir errores de sintaxis inesperados y problemas de seguridad.
    except (FileNotFoundError, ValueError, ZeroDivisionError, IndexError):
        print("No se han podido resolver las operaciones debido a un error en el formato del archivo.")

resolver_calculadora()