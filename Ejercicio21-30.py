""" Multiplica una cadena por un número entero """

cadena = 'hola '

multiplicado = cadena * 4

print('Ejercicio21: ', multiplicado)

""" Divide una cadena en una lista de subcadenas / Convertir cadena en array separado por palabras"""

cadena = 'hola que tal'
division = cadena.split()
print('Ejercicio22: ',division)

""" Verifica si una palabra es un palíndromo 
Ejemplo: RADAR, dábale arroz a la zorra el abad. """

def palindromo(palabra):
    if palabra == palabra[::-1]:
        print(palabra)
        print(palabra[::-1])
        return True
    else:
        print(palabra)
        print(palabra[::-1])
        return False

res = palindromo('radar')
print('Ejercicio23: ', res)

""" Elimina un elemento específico de una lista """

def eliminar(num, lista):
    lista.remove(num)
    return lista


lista = [1,2,3,4,5]
res = eliminar(3, lista)
print('Ejercicio24: ', res)

""" Genera una lista de números del 1 al 200 """
numeros= list(range(1, 201))

# print('Ejercicio25: ', numeros)

""" Intercambia los valores de dos variables con asignacion múltiple """

a = 5
b = 10
print('Ejercicio26: ', a ,b)
a, b = b, a
print('Ejercicio26: ', a ,b)

""" Ejercicio 27
Realiza operaciones básicas con conjuntos union e intersección """

conjunto1 = {1,2,3}
conjunto2 = {3,4,5}

union = conjunto1 | conjunto2
interseccion = conjunto1 & conjunto2
print('Ejercicio27: Unión: ', union)
print('Ejercicio27: Intersección: ', interseccion)

""" Extrae un elemento específico de una tupla"""

tupla = (10,20,30)
elemento = tupla[1]

print('Ejercicio28: ', elemento)

""" Combina dos listas en pares usando la función zip() """

lista1 = [1,2,3]
lista2 = ['a', 'b', 'c']

pares = list(zip(lista1, lista2))

print('Ejercicio29 : ', pares)


""" Elimina duplicados de una lista """

lista1 = [1,2,2,3,4,4,5]

def sinDuplicado(lista):
    res = list(set(lista))
    return res

res = sinDuplicado(lista1)

print('Ejercicio30: ', res)