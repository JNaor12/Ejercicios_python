""" Sumar dos números y mostrar su resultado """

def sumar (primero, segundo):
    return primero + segundo

res = sumar(12, 2)

print("Ejercicio1 :", res)

""" Calcula el área de un círculo con un radio dado """ #PI
import math

def area (radio):
    return (radio**2)*math.pi

res = area(3)

print("Ejercicio2 :", res)

""" Concatena dos cadenas de texto"""
def concatena(palabra1, palabra2):
    return palabra1 + palabra2

res = concatena("Hola ", "Mundo")

print("Ejercicio3 :", res)

""" Crear lista con diferentes elementos e imprimirla """

lista = ["Hola Mundo", 12, "Puchero", False, 33]

print("Ejercicio 4 :", lista)

""" Multiplica dos números y mostrar su resultado """

def multiplicar (primero, segundo):
    return primero * segundo

res = multiplicar(5, 2)

print("Ejercicio5 :", res)

""" Crea una cadena de texto y muestra su longitud"""

def longitud (cadena):
    return len(cadena)

res = longitud('hola filomena')

print("Ejercicio6 :", res)

""" Calcula el promedio de una lista de números """

def media (lista):
    return sum(lista)/len(lista)

lista=[2,4,6,8]
res= media(lista)

print('Ejercicio7:', res)

""" Crea una tupla con elementos e imprimela """

mi_tupla = (3, False, 'uno', 5.5)

print("Ejercicio8 :", mi_tupla)

""" Realiza la potencia de un número """

def potencia (num):
    return num**2

res = potencia(5)
print("Ejercicio3 :", res)

""" Invertir una cadena """

def invertir(string):
    return string[::-1]

res = invertir('cadena')

print("Ejercicio10 :", res)