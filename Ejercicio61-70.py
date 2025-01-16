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


""" Escribe una función para calcular el promedio de una lista de números """

def media(lista):
    return sum(lista)/len(lista)

lista=[4,6,8,10]
res= media(lista)

print('Ejercicio 66:', res)


""" Escribe una función para calcular el volumen de un cilindro  
    V = πr^2h 
"""

import math

def volumen_cilindro(radio, altura):
    return math.pi * radio **2 * altura

res = volumen_cilindro(3,5)

print(f'Ejercicio 67: {res}')

""" Escribe una función que pida por teclado la distancia y la velocidad para poder calcular el tiempo de viaje """

print('Ejercicio 68: ')

def tiempo_viaje():
    distancia = int(input('Escribe la distancia: '))
    velocidad = int(input('Escribe la velocidad: '))
    
    return distancia / velocidad

res = tiempo_viaje()
print(f'{res} horas') 

""" Escribe una función para calcular la tasa de desempleo 
    td = no_empleados / si_empleados * 100
"""
def tasa_desempleo(no_em, si_em):
    return (no_em / si_em)*100

res = tasa_desempleo(100, 900)
print(f'Ejercicio 69: {res}')

""" Escribe una función para clasificar si una sustancia es ácida, básica o neutra a partir de su pH """

def sustancia(ph):
    if ph < 7:
        return "Ácida"
    elif ph > 7:
        return "Básica"
    else:
        return "Neutra"

res = sustancia(7)

print(f'Ejercicio 70: {res}')


