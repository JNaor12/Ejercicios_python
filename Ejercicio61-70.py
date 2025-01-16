""" Crea una función para sumar dos números """
print ('Ejercicio 61: ')

num = int(input('Primer número a sumar: '))
num2 = int(input('Segundo número a sumar: '))

def suma(num, num2):
    res = num + num2
    return res

print(suma(num, num2))

""" Crea una función para calcular el área de un circulo """

import math

def area_circulo(radio):
    return math.pi * radio ** 2

res = area_circulo(5)

print(f'Ejercicio 62: El área es -> {res}')

""" Escribe una función para imprimir un mensaje de saludo """

def saludo(nombre):
    print(f'Ejercicio 63: Hola que tal {nombre}')

saludo('Aser')

""" Escribe una función para verificar si un número es par o impar """
print('Ejercicio 64: ')
def verificacion(num):
    if num % 2 == 0:
        return print('El número es par')
    else:
        return print('El número es impar')

verificacion(24)

""" Escribe una función para convertir grados celsius a fahrenheit """
grados = int(input('Escribe los grados Celsius: '))

def conversion(grados_c):
    return (grados_c * 9/5) +32

res = conversion(grados)

print(f'Ejercicio 65: {res} °F')

