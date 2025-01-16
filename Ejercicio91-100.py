""" Filtrar números pares de una lista utilizando filter """

numeros = [1,2,3,4,5,6,7,8]

pares = list(filter(lambda x : x % 2 == 0, numeros))        #Pide una función y un Iterable

print('Ejercicio 91: ')
print(numeros)
print(pares)

""" Filtrar cadenas de longitud mayor que 3 de una lista, usando filter """

lista = ['python', 'ruby', 'php', 'java']

res = list(filter(lambda x : len(x) > 3, lista))

print('Ejercicio 92: ')
print(res)


""" Filtra números negativos de una lista utilizando filter """

numeros = [-3, 1, -5, 5, -45]

negativos = list(filter(lambda x : x < 0, numeros))

print('Ejercicio 93: ')
print(numeros)
print(negativos)

""" Filtrar cadenas que contienen un carácter específico usando filter """

lista = ['apple', 'python', 'hola']
caracter = 'a'

con_a = list(filter(lambda x : caracter in x, lista ))

print('Ejercicio 94: ')
print(lista)
print(con_a)

""" Filtrar elementos que son listas """

lista = [1, 2, [3,4], ['a','b'], 5]

tipoListas = list(filter(lambda x : isinstance(x, list), lista))   #isinstance es una función que comprueba (en este caso) si "x" es de tipo "list"

print('Ejercicio 95: ')
print(lista)
print(tipoListas)

