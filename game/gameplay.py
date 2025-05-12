
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

    @property
    def name(self):
        return self.character.name

    @property
    def hp(self):
        return self.character.hp

    @hp.setter
    def hp(self, value):
        self.character.hp = max(0, value)  # Asegura que la vida no sea negativa

    @property
    def hp_max(self):
        return self.character.hp_max

    @property
    def strength(self):
        return self.character.strength

    @property
    def magic(self):
        return self.character.magic

    @property
    def resistance(self):
        return self.character.resistance

    @property
    def accuracy(self):
        return self.character.accuracy

    @property
    def agility(self):
        return self.character.agility

    def __getattr__(self, name):
        return getattr(self.character, name)
