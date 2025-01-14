""" Pide un número y verifica si es positivo o negatrivo """

# num = int(input("Ejercicio31: Escribe un número entero: "))

# if num > 0:
#     print('Número Positivo')
# elif num <0:
#     print('Número negativo')
# else:
#     print('El número es 0')


""" Pide un número y comprueba si el número es par o inpar utilixando if y modulo """

# num = int(input("Ejercicio32: Escribe un número entero: "))
# if num % 2 == 0:
#     print('Es número par')
# else:
#     print('Es número inpar')


""" Determina si un año es bisiesto 
    Regla de negocio
        -Divisible entre 4
        -No divisible entre 100
        -Divisible entre 400
"""

age = 2028

if (age % 4 == 0 and age % 100 != 0) or (age % 400 == 0):
    print('Es año bisiesto')
else:
    print('No es año bisiesto')

""" Verifica si una cadena es mayor o igual a 10 caracteres """

cadena = "hola que tal"

if len(cadena) > 10:
    print('Más de 10 carácteres')
elif len(cadena) < 10:
    print('Menos de 10 caracteres')
else:
    print('Tiene 10 carácteres')

""" Comprueba si un número está en el rango de 1 y 100 """

num = 88

if 1 <= num <= 100:
    print('Está entre 1 y 100')
else:
    print('No está entre 1 y 100')