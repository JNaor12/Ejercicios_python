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