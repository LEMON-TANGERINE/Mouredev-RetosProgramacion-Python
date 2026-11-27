"""
#27 CUADRADO Y TRIÁNGULO 2D   Fácil #26 2022
/*
 * Crea un programa que dibuje un cuadrado o un triángulo con asteriscos "*".
 * - Indicaremos el tamaño del lado y si la figura a dibujar es una u otra.
 * - EXTRA: ¿Eres capaz de dibujar más figuras?
 */
"""
def cuadrado_triangulo(figura, lado):   # Figura puede ser "triangulo" o "cuadrado". El lado es la altura o las filas.
    if figura == "triangulo":
        ancho = 2 * lado - 1    # Usamos 2 * lado - 1 para calcular el ancho total de la base simétrica.
        for fila in range(lado):    # Por cada fila aumentamos los asteriscos de 2 en 2 y los centramos en el medio.
            asteriscos = "*" * (2 * fila + 1)
            print(asteriscos.center(ancho))

    elif figura == "cuadrado":
        for fila in range(lado):    # Por cada fila imprimimos un número de asteriscos igual al número total de filas, o a la altura. Porque en el cuadrado base = altura.
            print("* " * lado)

    else:   # Si la figura del argumento no es válida o está mal escrita, imprimimos el aviso. 
        print("Figura no reconocida. Escoge entre triangulo/cuadrado.")



# COMPROBACIONES
cuadrado_triangulo("triangulo", 6)
cuadrado_triangulo("cuadrado", 8)



# EXTRA
def dibujo_extra(figura, lado, ancho=None):   # Figura puede ser "triangulo", "cuadrado" o "rectangulo". El lado es la altura o las filas.
    if figura == "triangulo":
        ancho = 2 * lado - 1
        for fila in range(lado):
            asteriscos = "*" * (2 * fila + 1)
            print(asteriscos.center(ancho))

    elif figura == "cuadrado":
        for fila in range(lado):
            print("* " * lado)

    elif figura == "rectangulo":
        if ancho is None:
            print("Indica el ancho del rectangulo.")
            return

        for fila in range(lado):
            print("* " * ancho)

    elif figura == "triangulo invertido":
            ancho = 2 * lado - 1
            for fila in reversed(range(lado)):
                asteriscos = "*" * (2 * fila + 1)
                print(asteriscos.center(ancho))

    elif figura == "rombo": # En realidad, un rombo son 2 triángulos, uno normal y uno invertido.
        ancho = 2 * lado - 1

        if lado % 2 != 0:   # Si el lado es impar, tiene un único pico central.
            for fila in range(lado // 2 + 1):
                asteriscos = "*" * (2 * fila + 1)
                print(asteriscos.center(ancho)) # Imprimimos el primer triángulo.

        else:   # Si el lado es par tiene dos filas centrales iguales.
            for fila in range(lado // 2):
                asteriscos = "*" * (2 * fila + 1)
                print(asteriscos.center(ancho)) # Imprimimos el primer triángulo.

        for fila in reversed(range(lado // 2)): # Imprimimos el segundo triángulo (el invertido).
            asteriscos = "*" * (2 * fila + 1)
            print(asteriscos.center(ancho))

    else:
        print("Figura no reconocida. Escoge entre triangulo/cuadrado/rectangulo/triangulo invertido/rombo.")



# COMPROBACIONES
dibujo_extra("rectangulo", 5, 9)
dibujo_extra("triangulo invertido", 5)
dibujo_extra("rombo", 10)