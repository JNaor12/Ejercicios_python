""" Elevar al cuadrado una lista de números utilizando map() """

def elevar(x):
    return x ** 2

lista = [1,2,3,4,5]
cuadrados = list(map(elevar, lista))        # list() Devuelve una lista y map(elevar, lista) recorre la array lista y le hace la función elevar) 
print('Ejercicio 81: ')
print(f'Lista de números: {lista}')
print(f'Lista de números al cuadrado :{cuadrados}')

""" Convertir una lista de cadenas que sean números a enteros utilizando map """

def convertir_entero(lista):
    return int(lista)

lista = ["1", "2", "3", "4"]

enteros = list(map(convertir_entero, lista))
print('Ejercicio 82: ')
print(lista)
print(enteros)

""" Calcular la longitud de una lista de palabras utilizando map() """

def longitud(palabra):
    return len(palabra)

animales = ["gato", "perro", "Jirafa"]

longitudes = list(map(longitud, animales))
print('Ejercicio 83: ')
print(animales)
print(longitudes)

""" Obtener el cuadrado de la suma de dos listas de números utilizando map() """

def suma_cuadrados(a, b):
    return (a+b) ** 2

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]

res = list(map(suma_cuadrados, lista1, lista2))

print('Ejercicio 84: ')
print(f'Primera lista: {lista1}')
print(f'Segunda lista: {lista2}')
print(f'Resultado: {res}')

""" Contar el número de vocales en una lista de palabras utilizando map """

def contar(palabra):
    return sum(1 for letra in palabra if letra.lower() in 'aeiou')

palabras = ['Hola ', 'mundo', 'murcielago']

conteos = list(map(contar, palabras))

print('Ejercicio 85: ')
print(f'Primera lista: {palabras}')
print(f'Segunda lista: {conteos}')

""" Elevar un número al cuadrado utilizando lmbda """

print('Ejercicio 86:')
cuadrado = lambda x : x ** 2    # x es el parametro que pide (en este caso 5)
print(cuadrado(5))


""" Sumar dos números utilizando lambda """

print('Ejercicio 87:')
suma = lambda x, y : x + y
print(suma(5,2))


""" Verifica si un número es par usando lambda """

print('Ejercicio 88:')
par = lambda x : x % 2 == 0
print(par(6))

""" Comprobar si una palabra es palíndromo usando lambda """

print('Ejercicio 89:')
palabra = lambda x : x == x[::-1]
print(palabra('radar'))

""" Duplicar cada elemento de una lista usando map() lambda """

numeros = [1,2,3,4,5]
duplicados = list(map(lambda x : x * 2, numeros))

print('Ejercicio 90: ')
print(numeros)
print(duplicados)