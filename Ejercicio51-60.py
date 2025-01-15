""" Imprimir los números del 1 al 5 con for """

for i in range(1,6):
    print(f'Ejercicio 51: {i}')


""" Sumar los números del 1 al 10 con for """

suma = 0

for i in range(1,11):
    suma += i

print(f'Ejercicio 52: {suma}')


""" Imprimir los elementos de una lista dada """

lista = [10,20,30,40,50]
print('Ejercicio 53: ')
for elemento in lista:
    print(elemento)


""" Imprimir los carácteres de una cadena utilizando el ciclo for """

cadena = "Hola que tal"
for caracter in cadena:
    print(f'Ejercicio 54: {caracter}')


""" Imprimir los números del 2 al 10 con el ciclo for """

print('Ejercicio 55: ')
for i in range(2,11,2):     #Números del 2 al 11, de 2 en 2
    print(i)


""" Listar 10 números y calcular el cuadrado de cada uno e imprimirlos utilizando for """
print('Ejercicio 56: ')
for i in range(1, 11):
    cuadrado = i ** 2
    print(f'El cuadrado de {i} es {cuadrado}')

""" Imprimir los números del 5 al 1 en orden descendente """
print('Ejercicio 57: ')
for i in range(5,0,-1):
    print(i)

""" Multiplicar todos los elementos de una lista por 2 """

lista = [3, 6.2, 'hola', True]
print('Ejercicio 58: ')
for i in range(len(lista)):
    print(lista[i])

""" Pedir al usuario un número e imprimir la tabla de multiplicar del mismo (con bucle for)"""

num = int(input('Ejercicio 59: Tabla de multiplicar del número: '))

for i in range(1,11):
    res = num * i
    print(f'{num} x {i} = {res}')


""" Imprimir la suma de los números del 1 al 10 utilizando bucle for """

pares = 0

for i in range(1,11):
    if i % 2 == 0:
        pares += i

print (f'Ejercicio 60: {pares}')

