
#   DIFICIL


#  * EJERCICIO:
#  * ¡La Casa del Dragón ha finalizado y no volverá hasta 2026!
#  * ¿Alguien se entera de todas las relaciones de parentesco
#  * entre personajes que aparecen en la saga?
#  * Desarrolla un árbol genealógico para relacionarlos (o invéntalo).
#  * Requisitos:
#  * 1. Estará formado por personas con las siguientes propiedades:
#  *    - Identificador único (obligatorio)
#  *    - Nombre (obligatorio)
#  *    - Pareja (opcional)
#  *    - Hijos (opcional)
#  * 2. Una persona sólo puede tener una pareja (para simplificarlo).
#  * 3. Las relaciones deben validarse dentro de lo posible.
#  *    Ejemplo: Un hijo no puede tener tres padres.
#  * Acciones:
#  * 1. Crea un programa que permita crear y modificar el árbol.
#  *    - Añadir y eliminar personas
#  *    - Modificar pareja e hijo
#  * 2. Podrás imprimir el árbol (de la manera que consideres).
#  * 
#  * NOTA: Ten en cuenta que la complejidad puede ser alta si
#  * se implementan todas las posibles relaciones. Intenta marcar
#  * tus propias reglas y límites para que te resulte asumible.


class Person:
    """
    Clase que representa una persona en el árbol genealógico.
    """
    def __init__(self, identifier, name):
        """Inicializa una nueva persona con un identificador y un nombre."""
        self.identifier = identifier  # Identificador único de la persona
        self.name = name              # Nombre de la persona
        self.pareja = None           # Pareja de la persona (None por defecto)
        self.hijo = []            # Lista de hijos (vacía por defecto)

    def __repr__(self):
        """Representación legible de la persona para depuración y visualización."""
        return f"{self.name} ({self.identifier})"

class FamilyTree:
    """
    Clase que representa el árbol genealógico.
    """
    def __init__(self):
        """Inicializa el árbol genealógico con un diccionario vacío de personas."""
        self.miembros = {}  # Diccionario con los miembros del árbol (clave: ID, valor: Persona)

    def add_person(self, identifier, name):
        """Añade una nueva persona al árbol genealógico."""
        if identifier in self.miembros:
            print(f"ERROR: Ya existe una persona con el ID {identifier}.")
            return
        self.miembros[identifier] = Person(identifier, name)    # Se crea el objeto

    def remove_person(self, identifier):
        """Elimina una persona del árbol, actualizando relaciones."""
        if identifier not in self.miembros:
            print(f"ERROR: No existe una persona con el ID {identifier}.")
            return

        person = self.miembros[identifier]

        # Elimina la referencia de pareja, si la tiene
        if person.pareja:
            pareja = self.miembros[person.pareja]
            pareja.pareja = None

        # Elimina a la persona como hijo de sus padres
        for member in self.miembros.values():
            if person in member.hijo:
                member.hijo.remove(person)

        # Elimina la persona del árbol
        del self.miembros[identifier]

    def establecer_pareja(self, id1, id2):
        """Establece una relación de pareja entre dos personas."""
        if id1 not in self.miembros or id2 not in self.miembros:
            print("ERROR: Uno o ambos IDs no existen.")
            return

        person1 = self.miembros[id1]
        person2 = self.miembros[id2]

        if person1.pareja or person2.pareja:
            print("ERROR: Una o ambas personas ya tienen pareja.")
            return

        person1.pareja = id2
        person2.pareja = id1

    def add_child(self, parent_id, child_id):
        """Añade un hijo a un padre, asegurándose de que la relación es válida."""
        if parent_id not in self.miembros or child_id not in self.miembros:
            print("ERROR: Uno o ambos IDs no existen.")
            return

        parent = self.miembros[parent_id]
        child = self.miembros[child_id]

        for member in self.miembros.values():
            if child in member.hijo:
                print(f"ERROR: {child.name} ya es hijo de {member.name}.")      #Si comentamos este for se podrá poners más de un padre a una presona
                return

        if child in parent.hijo:
            print("ERROR: Esta relación ya existe.")
            return
        

        parent.hijo.append(child)

    def print_tree(self):
        """Imprime el árbol genealógico de manera legible."""
        for person in self.miembros.values():
            pareja = self.miembros[person.pareja].name if person.pareja else "None"
            hijo = [child.name for child in person.hijo]
            print(f"{person.name} (ID: {person.identifier}) - Pareja: {pareja} - Hijos: {', '.join(hijo) or 'None'}")

# Ejemplo de uso
tree = FamilyTree()

tree.add_person(1, "Rhaenyra")
tree.add_person(2, "Daemon")
tree.add_person(3, "Jacaerys")
tree.add_person(4, "Lucerys")
tree.add_person(5, "Aegon")

tree.establecer_pareja(1, 2)
tree.add_child(1, 3)
tree.add_child(1, 4)
tree.add_child(1, 5)
tree.add_child(2, 5)
tree.add_child(2, 4)


tree.print_tree()