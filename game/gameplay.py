from characters.character import Character
from characters.guerrer import Guerrer
from characters.mag import Mag
from characters.arquer import Arquer
from characters.lladre import Lladre
from characters.guaridor import Guaridor
import random

class Jugador:
    def __init__(self, character_type, name):
        # Constructor de la classe Jugador
        # Crea un personatge segons el tipus triat i el nom
        self.character = self.create_character(character_type, name)
        self.x_pos = 0  # Posició inicial X al mapa
        self.y_pos = 0  # Posició inicial Y al mapa


    def create_character(self, character_type, name):
        # Crea una instància del tipus de personatge seleccionat
        character_classes = {
            "Guerrer": Guerrer,
            "Mag": Mag,
            "Arquer": Arquer,
            "Lladre": Lladre,
            "Guaridor": Guaridor
        }
        
        if character_type in character_classes:
            # Si el tipus existeix, creem la instància corresponent
            return character_classes[character_type](name)
        else:
            # Si no existeix, llancem un error
            raise ValueError(f"Tipo de personaje no válido: {character_type}")

    def mover_arriba(self, limite):
        # Mou el jugador cap amunt (disminueix Y)
        self.y_pos = max(0, self.y_pos - 1)  # Assegurem que no surti del mapa

    def mover_abajo(self, limite):
        # Mou el jugador cap avall (augmenta Y)
        self.y_pos = min(limite - 1, self.y_pos + 1)  # Assegurem que no surti del mapa

    def mover_izquierda(self):
        # Mou el jugador cap a l'esquerra (disminueix X)
        self.x_pos = max(0, self.x_pos - 1)  # Assegurem que no surti del mapa

    def mover_derecha(self, limite):
        # Mou el jugador cap a la dreta (augmenta X)
        self.x_pos = min(limite - 1, self.x_pos + 1)  # Assegurem que no surti del mapa

    def attack(self):
        # Implementa l'atac del jugador, delegant al personatge
        damage = self.character.attack()
        # Retornem el dany i un número aleatori entre 1 i 20 (com un d20 en jocs de rol)
        return damage, random.randint(1, 20)

    def defend(self):
        # Implementa la defensa del jugador, delegant al personatge
        return self.character.defend()

    def usar_habilidad(self):
        # Implementa l'ús d'habilitat del jugador, delegant al personatge
        return self.character.usar_habilidad()

    def heal(self, amount):
        # Cura el jugador, delegant al personatge
        self.character.hp = min(self.character.hp_max, self.character.hp + amount)

    # Propietats que redirigeixen als atributs del personatge
    @property
    def name(self):
        return self.character.name

    @property
    def hp(self):
        return self.character.hp

    @hp.setter
    def hp(self, value):
        self.character.hp = max(0, value)  # Assegurem que la vida no baixi de 0

    @property
    def hp_max(self):
        return self.character.hp_max

    @property
    def fortaleza(self):
        return self.character.fortaleza

    @property
    def magia(self):
        return self.character.magia

    @property
    def resistencia(self):
        return self.character.resistencia

    @property
    def exactitud(self):
        return self.character.exactitud

    @property
    def agilidad(self):
        return self.character.agilidad

    # Accés als bonificadors si existeixen
    @property
    def bonuses(self):
        if hasattr(self.character, 'bonuses'):
            return self.character.bonuses
        return {}

    def __getattr__(self, name):
        # Si un atribut no es troba en aquesta classe, ho busquem al personatge
        # Això permet accedir a tots els mètodes del personatge des del jugador
        if hasattr(self.character, name):
            return getattr(self.character, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")