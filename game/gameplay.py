from characters.character import Character
from characters.guerrer import Guerrer
from characters.mag import Mag
from characters.arquer import Arquer
from characters.lladre import Lladre
from characters.guaridor import Guaridor
import random

class Jugador:
    def __init__(self, character_type, name):
        self.character = self.create_character(character_type, name)
        self.x_pos = 0
        self.y_pos = 0


    def create_character(self, character_type, name):
        character_classes = {
            "Guerrer": Guerrer,
            "Mag": Mag,
            "Arquer": Arquer,
            "Lladre": Lladre,
            "Guaridor": Guaridor
        }
        
        if character_type in character_classes:
            return character_classes[character_type](name)
        else:
            raise ValueError(f"Tipo de personaje no válido: {character_type}")

    def mover_arriba(self, limite):
        self.y_pos = max(0, self.y_pos - 1)

    def mover_abajo(self, limite):
        self.y_pos = min(limite - 1, self.y_pos + 1)

    def mover_izquierda(self):
        self.x_pos = max(0, self.x_pos - 1)

    def mover_derecha(self, limite):
        self.x_pos = min(limite - 1, self.x_pos + 1)

    def attack(self):
        damage = self.character.attack()
        return damage, random.randint(1, 20)

    def defend(self):
        return self.character.defend()

    def usar_habilidad(self):
        return self.character.usar_habilidad()

    # Método para la curación
    def heal(self, amount):
        self.character.hp = min(self.character.hp_max, self.character.hp + amount)

    @property
    def name(self):
        return self.character.name

    @property
    def hp(self):
        return self.character.hp

    @hp.setter
    def hp(self, value):
        self.character.hp = max(0, value)

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

    # Añadir acceso a bonuses si existen
    @property
    def bonuses(self):
        if hasattr(self.character, 'bonuses'):
            return self.character.bonuses
        return {}

    def __getattr__(self, name):
        if hasattr(self.character, name):
            return getattr(self.character, name)
        raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")