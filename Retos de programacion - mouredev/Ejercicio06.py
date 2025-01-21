
#   DIFICIL

#  * EJERCICIO:
#  * Entiende el concepto de recursividad creando una función recursiva que imprima
#  * números del 100 al 0.
#  *
#  * DIFICULTAD EXTRA (opcional):
#  * Utiliza el concepto de recursividad para:
#  * - Calcular el factorial de un número concreto (la función recibe ese número).
#  * - Calcular el valor de un elemento concreto (según su posición) en la 
#  *   sucesión de Fibonacci (la función recibe la posición).


def recursividad(n):

    if n < 0:
        return
    print(n)

    recursividad(n - 1)     # Llamada recursiva con n - 1

recursividad(100)

def factorial(n):
    
    factorial = 1
    i = 1
    while i <= n:
        factorial = factorial * i
        i += 1
    return factorial

print(factorial(5))

def fibonacci(posicion):

        if posicion <= 0:
            return "La posición debe ser un entero positivo."
        elif posicion == 1:
            return 0  # El primer elemento de Fibonacci es 0
        elif posicion == 2:
            return 1  # El segundo elemento de Fibonacci es 1
        else:
            # Llamada recursiva para calcular el valor
            return fibonacci(posicion - 1) + fibonacci(posicion - 2)
        

print(fibonacci(10))