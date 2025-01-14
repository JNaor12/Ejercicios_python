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
    print('Ejercicio33: Es año bisiesto')
else:
    print('Ejercicio33: No es año bisiesto')

""" Verifica si una cadena es mayor o igual a 10 caracteres """

cadena = "hola que tal"

if len(cadena) > 10:
    print('Ejercicio34: Más de 10 carácteres')
elif len(cadena) < 10:
    print('Ejercicio34: Menos de 10 caracteres')
else:
    print('Ejercicio34: Tiene 10 carácteres')

""" Comprueba si un número está en el rango de 1 y 100 """

num = 88

if 1 <= num <= 100:
    print('Ejercicio35: Está entre 1 y 100')
else:
    print('Ejercicio35: No está entre 1 y 100')

""" Pide un carácter y Determina si es un vocal """

caracter = input("Escríbe un carácter: ")

vocales = ['a', 'e', 'i', 'o' ,'u']

if caracter.lower() in vocales:
    print("Ejercicio36: Es una vocal")
else:
    print("Ejercicio36: No es una vocal")

""" Calcula el máximo de tres números """

num1 = 8
num2 = 5
num3 = 9

maximo = max(num1,num2,num3)

print(f'Ejercicio37: El número mas alto es: {maximo}')

""" Determina si un número es divisible entre 5 y 7 """

num = 35

if num % 5 == 0 and num % 7 == 0:
    print('Ejercicio38: Es divisible entre 5 y 7')
else:
    print('Ejercicio38: No es divisible entre 5 y 7')

""" Verifica si la pablabra ingresada es "python" """

palabra = input('Escribe la palabra: python -> ')

if palabra.lower() == 'python':
    print('Ejercicio39: Gracias!')
else:
    print('Ejercicio39: Por que no me haces caso?' )

""" Calcula el ICM e intrepretalo """

peso = 75
altura = 1.75

imc = peso / (altura**2)
print(f'Ejercicio40: {imc}')

if imc < 18.5:
    print('Bajo peso')
elif imc < 25:
    print('Peso Normal')
elif  imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obesidad grado I')
elif imc < 40:
    print('Obesidad grado II')
else:
    print('Obesidad grado III')
