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


""" Solicita al usuario ingresar un número y cuenta cuantos dígitos tiene """

# abs(num): Convierte el número a su valor absoluto para ignorar el signo negativo si existe.
# str(): Convierte el número a una cadena, lo que permite usar len() para contar los caracteres.
# len(): Calcula la longitud de la cadena, que corresponde al número de dígitos.

num = int(input('Ejercicio 46: Ingresa un número: '))

longitud = len(str(abs(num)))

print(f'El número tiene {longitud} dígitos')

""" Hacer un menu de opciones que incluya la opción de salir del programa """
print('Ejercicio 47: ')
while True:
    print('1. Sumar')
    print('2. Restar')
    print('3. Salir')

    opcion = int(input('Escribe el número de la opción que desees selecionar: '))

    if opcion == 1:
        print('Sumando...')
    elif opcion ==2:
        print('Restando')
    elif opcion == 3:
        break
    else:
        print('Opción no válida')

print('Chao chao chao chao')

""" Lanzamiento de moneda """

import random
print('Ejercicio 48:')
while True:
    moneda = random.randint(1,2)
    if moneda == 1:
        print('Cara')
    else:
        print('Cruz')
    again = input('Tirar de nuevo (S/N): ')
    if again.lower() == 'n':
        break
print('Gracias por jugar')

""" Simular un lanzamiento de dado hasta obtener un 6 """

import random
print('Ejercicio 49:')
num = 0
trys = 0
while num !=6:
    num = random.randint(1,6)
    trys += 1 
    print(f'Has sacado un {num}')
    
print(f'Gracias por jugar, lo has conseguido en : {trys} intentos.')

""" Mostrar los números del 1 al 100, pero reemplazando los múltiplos de 3 por "Fizz" y los múltiplos de 5 por "Buzz"  """

num = 1

print('Ejercicio 50: ')
while num <= 100:
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)
    num += 1

