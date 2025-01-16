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
