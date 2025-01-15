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