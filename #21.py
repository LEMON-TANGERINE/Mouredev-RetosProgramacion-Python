"""
#21 PARANDO EL TIEMPO   Medio #20 2022
/*
 * Crea una función que sume 2 números y retorne su resultado pasados
 * unos segundos.
 * - Recibirá por parámetros los 2 números a sumar y los segundos que
 *   debe tardar en finalizar su ejecución.
 * - Si el lenguaje lo soporta, deberá retornar el resultado de forma
 *   asíncrona, es decir, sin detener la ejecución del programa principal.
 *   Se podría ejecutar varias veces al mismo tiempo.
 */
"""
import asyncio

async def parar_el_tiempo(num1, num2, tiempo=0):
    suma = num1 + num2
    await asyncio.sleep(tiempo) # Hace una pausa que le indica al programa que mientras tanto pase a la siguiente tarea.
    return suma

async def main():
    tareas = [  # Definimos las tareas que queremos ejecutar.
        parar_el_tiempo(1, 2, 3),
        parar_el_tiempo(33, 3, 8),
        parar_el_tiempo(5, 50, 0),
        parar_el_tiempo(60, 7, 6)
    ]
    
    for tarea in asyncio.as_completed(tareas):  # asyncio.as_completed las lanza todas juntas, pero nos devuelve los resultados ordenados por cuál termina antes.
        print(await tarea)  # Imprime las sumas según van llegando.

asyncio.run(main())