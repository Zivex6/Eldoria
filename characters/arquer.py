from .character import Character

class Arquer(Character):
    def __init__(self, name):
        super().__init__(name)
        self.exactitud += 5
        self.bonuses = {"exactitud": 5}

    def attack(self):
        return self.exactitud * 2

    def defend(self):
        return self.agilidad * 1.2

    def get_bonus_description(self):
        return f"Bonificación de Arquer: +{self.bonuses['exactitud']} precisión"