
from .character import Character

class Mag(Character):
    def __init__(self, name):
        super().__init__(name)
        self.magia += 5
        self.bonuses = {"magia": 5}

    def attack(self):
        return self.magia * 2

    def defend(self):
        return self.resistencia

    def get_bonus_description(self):
        return f"Bonificación de Mag: +{self.bonuses['magia']} magia"