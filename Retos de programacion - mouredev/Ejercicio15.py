
#  * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
#  * asíncrona una función que tardará en finalizar un número concreto de
#  * segundos parametrizables. También debes poder asignarle un nombre.
#  * La función imprime su nombre, cuándo empieza, el tiempo que durará
#  * su ejecución y cuando finaliza.

#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando el concepto de asincronía y la función anterior, crea
#  * el siguiente programa que ejecuta en este orden:
#  * - Una función C que dura 3 segundos.
#  * - Una función B que dura 2 segundos.
#  * - Una función A que dura 1 segundo.
#  * - Una función D que dura 1 segundo.
#  * - Las funciones C, B y A se ejecutan en paralelo.
#  * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.

import asyncio
from datetime import datetime


async def tarea(name: str, duration: int):

    print(f"{datetime.now()} |Tarea '{name}' comienza. Durará {duration} segundos.")
    await asyncio.sleep(duration) 
    print(f"{datetime.now()} | Tarea '{name}' ha finalizado")
        # await: Pausa la función actual (sin bloquear el programa completo) hasta que se complete lo que sigue.
        # asyncio.sleep(duracion): Simula una espera durante duracion segundos. Mientras esta tarea "duerme", otras tareas pueden ejecutarse.


async def main():

    tasks = [
        tarea("C", 3),
        tarea("B", 2),
        tarea("A", 1)
    ]

    await asyncio.gather(*tasks)
        # asyncio.gather(*tareas): Ejecuta todas las tareas de la lista al mismo tiempo.
            # El programa no espera a que termine una tarea antes de comenzar otra.
            # Esto maximiza la eficiencia cuando trabajamos con operaciones que incluyen esperas (como sleep).
    await tarea("D",1)
        # Ejecuta la tarea D tras finalizar las 'tasks'

asyncio.run(main())


