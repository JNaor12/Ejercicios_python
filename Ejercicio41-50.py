""" Imprime los números del 10 al 1 en orden descendente """
i=10
print('Ejercicio41: ')
while i >= 1:
    print(i)
    i -= 1

""" Solicita al usuario ingresar un número N y luego la suma de todos los números desde 1 hasta N """

num = int(input('ingresa un número: '))

i = 1
suma = 0

while num >= i:
    suma+=i
    i+=1

print(f'Ejercicio 42: La suma es: {suma}')

""" 
Solicita al usuario ingresar un número n e imprime el factoriall de ese número.
5! = 5 x 4 x 3 x 2 x 1 = 120 
"""

num = int(input('Ingresa un número: '))

factorial = 1
i = 1
while i <= num:
    factorial = factorial * i
    i += 1

print(f'Ejercicio 43: {factorial}')

""" Genera un número aleatorio entre 1 y 10.
    Luego , pide al usuario adivinar el número hasta que lo haga correctamente.
 """

import random

aleatorio = random.randint(1,10)
trys = 0

while True:
    intento = int(input('Adivina el número: '))
    trys += 1
    if intento == aleatorio:
        print(f'Ejercicio 44: Correcto! El número secreto era: {aleatorio}, solo te ha costado: {trys} intentos.')
    else:
        while True:
            intento = int(input('Otro intento: '))
            trys += 1
            if intento == aleatorio:
                print(f'Ejercicio 44: Correcto! El número secreto era: {aleatorio}, solo te ha costado: {trys} intentos.')
                break
    break

""" Imprime la tabla de multiplicar de un número ingresado por el usuario """

num = int(input('Ejercicio 45: Tabla de multiplicar del número: '))
i = 1
while i <= 10:
    print(f'{num} x {i} = {num*i}')
    i += 1
