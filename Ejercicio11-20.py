""" Calcula el área de un rectángulo Y pide bvase y altura al usuario """

# base = int(input("Ingresa la base: "))
# altura = int(input("Ingresa la altura: "))

# area = base*altura

# print('Ejercicio11: ', area)

""" Convierte un número entero a cadena """
num=12
print('Ejercicio12: ', type(num))
def parse(num):
    return str(num)

res= parse(num)
print('Ejercicio12: ', type(res))

""" Reemplaza un caracter en una cadena """

def reemplazar(palabra):
    return palabra.replace("o","x")
res = reemplazar('Python')

print('Ejercicio13: ', res)

""" Pasa una cadéna de Mayus a Minus """

def Minus(cadena):
    return cadena.lower()

res = Minus('PYTHON')
print('Ejercicio14: ', res)

""" Ordena una lista de números de menor a mayor """

def OrdenarMenos(lista):
    lista.sort()
    return lista

listaa=[7,2,5,1,9]
res = OrdenarMenos(listaa)
print('Ejercicio15: ', res)

""" Calcula 2 elevado a 4 sin usar ** """

def potencia (num):
    return pow(num, 4)

res = potencia(2)
print("Ejercicio16 :", res)

""" Extrae una subcadena de una cadena dada """

cadena= 'hola'
subcadena = cadena[0:2]
print("Ejercicio17 :",subcadena)

"""Convierte un número decimal a uno entero"""

def parseInt(num):
    num = int(num)
    return num
res = parseInt(8.55)

print('Ejercicio18: ', res)


"""Cuenta las ocurrencias de un carácter específico en una cadena """

def busca(cadena):
    return cadena.count('a')

res = busca('programacion')
print('Ejercicio19: ', res)

""" Encuentra y muestra el último caracter de una cadena """

def ultimoCaracter(cadena):
    return cadena[-1]

res= ultimoCaracter('python')

print('Ejercicio20: ', res)
