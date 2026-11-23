"""
#5 AREA DE UN POLÍGONO   Fácil #4 2022
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""
"""
NOTA: Hay muchas formas de resolver este ejercicio.
Yo he utilizado `if/else` y `match/case` por ser las soluciones más simples, intuitivas y de rápida ejecución
pero también se puede hacer con clases o funciones lambda.
"""

def area(poligono):
    if poligono.lower() == "triangulo" or poligono.lower() == "triángulo":
        base = float(input("¿Cuánto mide la base? "))
        altura = float(input("¿Cuánto mide de alto? "))
        return (base * altura) / 2
    elif poligono.lower() == "cuadrado":
        lado = float(input("¿Cuánto mide el lado? "))
        return lado**2
    elif poligono.lower() == "rectangulo" or poligono.lower() == "rectángulo":
        base = float(input("¿Cuánto mide la base? "))
        altura = float(input("¿Cuánto mide de alto? "))
        return base * altura
    else:
        return "Polígonos soportados: triángulo, cuadrado y rectángulo"

print(area("Triángulo"))




def area(poligono, base, altura=0): # Por defecto pongo que la altura es 0 si no se especifica en caso de que el poligono sea cuadrado
    tipo = poligono.lower().strip() # strip() es para quitar espacios. Es buena práctica sanitizar el input de los usuarios
    match tipo:
        case "triangulo" | "triángulo":
            return (base * altura) / 2
        case "cuadrado":
            return (base ** 2)
        case "rectangulo" | "rectángulo":
            return base * altura

print(area("cuadrado", 4))




def area(poligono, **medidas):
    # Obtiene 'lado' o 'base', el que haya enviado el usuario (por defecto 0 para que si el usuario no pone nada no crashee el programa)
    lado_o_base = medidas.get("lado") or medidas.get("base", 0)
    altura = medidas.get("altura", 0)

    match poligono.lower():
        case "triangulo"| "triángulo":
            return (lado_o_base * altura) / 2
        case "cuadrado":
            return lado_o_base**2
        case "rectangulo" | "rectángulo":
            return lado_o_base * altura

# Permite usar el nombre que quieras al llamar la función:
print(area("Rectángulo", base=10, altura=5))  # Usas 'base' pero puedes usar 'lado' para el cuadrado