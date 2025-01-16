""" Crear una clase Rectangulo con los siguientes atributos:
        base : base del rectangulo        
        altura : altura del rectangulo

    La clase debe tener los siguientes métodos:
    ** __init__(self, base, altura): inicializada

    Los atributos de la clase:
    ** calcular_area(self): calcula y devuelve el área del rectangulo
    ** calcular_perimetro(self): calcula y devuelve el perimetro del rectangulo

 """

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return (self.base + self.altura) * 2
    
rec1 = Rectangulo(5,3)
rec2 = Rectangulo(2,4)
print('Ejercicio 71: ')
print(f'El primer rectángulo tiene un área de : {rec1.calcular_area()}')
print(f'El primer rectángulo tiene un perímetro de : {rec1.calcular_perimetro()}')
print(f'El segundo rectángulo tiene un área de : {rec2.calcular_area()}')
print(f'El segundo rectángulo tiene un perímetro de : {rec2.calcular_perimetro()}')

""" Crea una clase Circulo con los siguientes atributos:
        radio :radio del circulo
    La clase debe de tener los siguientes métodos:
    ** __init__(self,radio): Inicializa los atributos de la clase
    **calcular_area(self): calcula y devuelve el área del circulo
    **calcular_perimetro(self): calcula y devuelve el perímetro del circulo

 """
import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
circuloRojo = Circulo(5)
circuloAzul = Circulo(2)
print('Ejercicio 72: ')
print(f'El circulo rojo  tiene un área de : {circuloRojo.calcular_area()}')
print(f'El circulo rojo tiene un perímetro de : {circuloRojo.calcular_perimetro()}')
print(f'El circulo azul tiene un área de : {circuloAzul.calcular_area()}')
print(f'El circulo azul tiene un perímetro de : {circuloAzul.calcular_perimetro()}')

""" Crea una clase Libro
    atributos: titulo, autor, editorial, año de publicacion
    métodos: constructor 
 """

class Libro:
    def __init__(self, titulo, autor, editorial, año_publi):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.año_publi = año_publi

mi_libro = Libro("Platero y yo", "Juan Ramón Jimenez", "Alizana editorial", 1914)

print(f'Ejercicio 73: {mi_libro.__dict__}')     #Convierto en diccionario el objeto mi_libro para mostrar el contenido del objeto


""" Crea una clase persona con los atributo:
        nombre
        edad
        dni
    Con los métodos:
        init()
        es_mayor_de_edad() este retorna True si es mayor de edad     
"""

class Persona:
    def __init__(self, nombre, edad ,dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
        
aser = Persona('Aser',28,'12345678V')
bruno = Persona('Bruno',18,'87456123W')
pepe = Persona('Pepe',15,'98765432H')

print('Ejercicio 74: ')

print(f'El nombre de Persona1 es: {aser.nombre}')
if aser.es_mayor_de_edad():
    print('Es mayor de edad')
else:
    print('Es menor de edad')

print(f'El nombre de Persona2 es: {bruno.nombre}')
if bruno.es_mayor_de_edad():
    print('Es mayor de edad')
else:
    print('Es menor de edad')

print(f'El nombre de Persona3 es: {pepe.nombre}')
if pepe.es_mayor_de_edad():
    print('Es mayor de edad')
else:
    print('Es menor de edad')

""" Crear una clase Coche con los atributos: 
        marca, modelo, matricula, km
    con los métodos:
    init()
    avanzar(km) este aumenta el valor de km en la cantidad
"""

class Coche:
    def __init__(self, marca, modelo, matricula, km):
        self.marca = marca
        self.modelo = modelo
        self.matricla = matricula
        self.km = km
    
    def avanzar(self, km):
        self.km += km

coche1 = Coche('ford', 'fiesta', '123 ABC', 5000)

print('Ejercicio 75: ')
print(coche1.__dict__)
coche1.avanzar(3000)
print(coche1.__dict__)

""" Crea una clase animal con los atributos:
        especie
        nombre
    La calse debe tener los métodos:
    init()
    hablar()
    el método hablar nos retorna una palabra según la interpretación sdel sonido como un perro sería "guau"
"""
print('Ejercicio 76: ')
class Animal:
    def __init__(self, especie, name):
        self.especie = especie
        self.name = name
    
    def hablar(self):
        if self.especie.lower() == 'perro':
            print('guau')
        elif self.especie.lower() == 'gato':
            print('Miau')
        else:
            print(f'No se que sonido hace un {self.especie}')
    
perro = Animal('perro', 'Iron')

gato = Animal('gato', 'Felipe')

perro.hablar()
gato.hablar()

print(perro.__dict__)
print(gato.__dict__)

""" Crea una lista llamada Persona.
    con los atributos: nombre ,dad
    **Un constructor, donde los datos pueden estar vacíos
    **Setters y getters para cada atributo
    **mostrar(): Muestra los datos de la persona
    **esMayorDeEdad(): Devuelve un valor lógico indicando si es o no mayor de edad
"""
print('Ejercicio 77:')
class Persona:
    def __init__(self, nombre=None, edad=None):     #El =None es oara que puedan estar vacíos los parametros
        self._nombre = nombre       #al poner self._nombre el _ es un modificador de acceso
        self._edad = edad
    
    @property                       #Decorador property
    def nombre(self):
        return self._nombre            #getter
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre    #setter

    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    def mostrar(self):
        print(self.__dict__)

    def mayor_edad(self):
        if self._edad >= 18:
            return True
        else:
            return False

bruno = Persona('Bruno')
bruno.mostrar()

aser = Persona('Aser',28)
print(aser.mayor_edad())
aser.mayor_edad()
aser.mostrar()

""" Crea una clase Persona y otra clase Estudiante
    La clase Persona tiene el atributo nombre y el método mostrarNombre()
    La clase Estudiante debe heredar de la clase Persona y utilizar el método mostrar_nombre() de la clase Persona
"""

print('Ejercicio 78: ')

class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def mostrar_nombre(self):
        print(f'El nombre es: {self.nombre}')
    
class Estudiante(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)
    
estudiante1 = Estudiante('Jorge')
estudiante1.mostrar_nombre()


""" Representa una cuenta bancaria con deposito y retiro debe haber un titular y un saldo 
    Usa POO
"""

class Cuenta:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, cantidad):
        cantidad = float(input("Cantidad que desee depositar: "))
        self.saldo += cantidad
        print(f'Se ha depositado {cantidad} €')
        print(f'Saldo actual: {self.saldo} €')
    
    def retirar(self, cantidad):
        cantidad = float(input("Cantidad que desee retirar: "))
        self.saldo -= cantidad
        print(f'Se ha retirado {cantidad} €')
        print(f'Saldo actual: {self.saldo} €')

    def mostrar(self):
        print(self.__dict__)


cuenta1 = Cuenta('Iván', 500)
print('Ejercicio 79: ')
cuenta1.mostrar()
cuenta1.depositar(1000)
cuenta1.retirar(300)

""" Obtener la cantidad de memoria ram en mi pc 
    pip install psutil      Libreria externa
"""

import psutil

def obtener_ram():
    memoria = psutil.virtual_memory()
    memoria_total = memoria.total / (1024 ** 3)
    return memoria_total

memoria = obtener_ram()

print('Ejercicio 80: ')
print(f'Total de memoria ram = {memoria} GB')