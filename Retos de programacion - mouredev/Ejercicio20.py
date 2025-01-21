
#   DIFICIL


#  * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
#  * una petición a la web que tú quieras, verifica que dicha petición
#  * fue exitosa y muestra por consola el contenido de la web.


#  * DIFICULTAD EXTRA (opcional):
#  * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
#  * terminal al que le puedas solicitar información de un Pokémon concreto
#  * utilizando su nombre o número.
#  * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
#  * - Muestra el nombre de su cadena de evoluciones
#  * - Muestra los juegos en los que aparece
#  * - Controla posibles errores

import requests

class Pokemon:

    base_url = 'https://pokeapi.co/api/v2/pokemon/'

    def get_Pokemon(self, name: str):

        url = f'{self.base_url}{name}'

        try:
            response = requests.get(url)

            if response.status_code != 200:
                raise Exception(f'Not found Pokemon with {name} name')
            
            pokemon = response.json() # nos devuelve el objeto pokemon

            pokemon_types = pokemon["types"]
            species_url = pokemon["species"]["url"]


            print("\nInformación del Pokémon:")
            print(f"ID: {pokemon['id']}")
            print(f"Nombre: {pokemon['name'].capitalize()}")
            print(f"Peso: {pokemon['weight']} kg")
            print(f"Altura: {pokemon['height']} m")

            str_type = 'Tipo: '
            for type in pokemon_types:
                str_type = str_type + type['type']['name'] + " "
            print(str_type)

            self.get_evolution_chain(species_url)


            name_game = [elemento['version']['name'] for elemento in pokemon['game_indices']]
            print(f"\nAparece en los juegos: {', '.join(name_game).capitalize()}")

            # print("\nJuegos en los que aparece:")
            # for elemento in pokemon['game_indices']:
            #     name_game = elemento['version']['name'].capitalize()          #Mostrarlo en lista
            #     print(f"- {name_game}")

        except Exception as e:
            print(e)


    def get_evolution_chain(self, species_url: str):
          
        try:
            response = requests.get(species_url)

            if response.status_code != 200:
                raise Exception('No se pudo obtener la información de la especie del Pokémon.')
                
            species_data = response.json()
            evolution_chain_url = species_data['evolution_chain']['url']

            # Solicitar la cadena de evoluciones.
            response = requests.get(evolution_chain_url)

            if response.status_code != 200:
                raise Exception('No se pudo obtener la cadena de evoluciones del Pokémon.')
            
            evolution_data = response.json()
            chain = evolution_data['chain']

            # Recorrer la cadena de evoluciones y mostrar las etapas.
            print("\nCadena de evoluciones:")
            self.mostrar_evolution_chain(chain)

        except Exception as e:
                print(e)

    def mostrar_evolution_chain(self, chain: dict):
        
        # Recorre la cadena de evoluciones y muestra cada etapa.
        actual = chain
        while actual:
            name = actual['species']['name'].capitalize()
            print(f"- {name}")
            if actual['evolves_to']:
                actual = actual['evolves_to'][0]  # Continuar con la siguiente evolución.
            else:
                break




client = Pokemon()

name = input("Introduce el pokémon: ")
client.get_Pokemon(name.strip().lower())
