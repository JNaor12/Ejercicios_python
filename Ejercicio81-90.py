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
print('Ejercicio 83: ')
print(lista)
print(enteros)

""" Calcular la longitud de una lista de palabras utilizando map() """

def longitud(palabra):
    return len(palabra)

animales = ["gato", "perro", "Jirafa"]

longitudes = list(map(longitud, animales))
print('Ejercicio 84: ')
print(animales)
print(longitudes)

""" Obtener el cuadrado de la suma de dos listas de números utilizando map() """

def suma_cuadrados(a, b):
    return (a+b) ** 2

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]

res = list(map(suma_cuadrados, lista1, lista2))

print('Ejercicio 85: ')
print(f'Primera lista: {lista1}')
print(f'Segunda lista: {lista2}')
print(f'Resultado: {res}')