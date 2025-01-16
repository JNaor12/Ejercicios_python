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

""" Crear una excepción que me ayude a determinar si el índice de una lista esta fuera de rango """

lista = [1,2,3]

print('Ejercicio 96: ')

rango = int(input("¿Que índice quieres ver? "))

try:
    if rango != 0:
        print(lista[rango-1])
    else:
        print("Error, el índice no existe")
except IndexError:
    print("Error, el índice no existe")


""" Hacer una función para crear un archivo de texto plano """

nombre = input('Escribe el nombre del archivo con su extensión (Ejemplo: index.html): ')

def crear_archivo(nombre_archivo):
    with open(nombre_archivo, 'w'):      # w-> lectura y escritura
        pass

crear_archivo(nombre)
print('Ejercicio 97: Archivo creado con éxito')

""" Escribir en un archivo html: Hola que tal ? """

def escribir(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)

escribir('francia.html', 'Hola que tal ?')

""" Crea un programa que me permita crear, leer y agregar información en un archivo .txt """

print('Ejercicio 99: ')
class Archivo:

    def __init__(self):
        self.nombre_archivo = ""
        self.contenido = ""
    
    def set_nombre_archivo(self, nombre):
        self.nombre_archivo = nombre
    
    def set_contenido(self, contenido):
        self.contenido = contenido
    
    def crear_archivo(self):
        with open(self.nombre_archivo, 'w'):
            pass
    
    def escribir(self):
        with open(self.nombre_archivo, 'w') as archivo:
            archivo.write(self.contenido)
    
    def leer(self):
        with open(self.nombre_archivo, 'r') as archivo:
            info = archivo.read()
        return info

file = Archivo()
file.set_nombre_archivo('index.txt')
file.set_contenido('Hola que tal')
file.crear_archivo()
file.escribir()

print(file.leer())

""" Conectarte a una base de datos mysql, hacer una consulta a una tabla y mostrar la información en la consola 
    
    pip install mysql-connector-python 
"""
import mysql.connector

class Conexion:
    def conectar(self):
        conexion = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'visitas'
        )
        return conexion

class Visitas(Conexion):
    def consulta_select(self):
        conexion = self.conectar()
        sql = "SELECT id, paterno FROM t_visitas"
        cursor = conexion.cursor()
        cursor.execute(sql)
        registros = cursor.fetchall()
        cursor.close()
        conexion.close()
        return registros

    def imprimir_datos(self):
        datos = self.consulta_select()
        for fila in datos:
            print(fila)

visita = Visitas()
visita.imprimir_datos()

