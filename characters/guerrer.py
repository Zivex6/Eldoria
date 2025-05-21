from .character import Character

class Guerrer(Character):
    def __init__(self, name):
        super().__init__(name)
        self.fortaleza += 5
        self.bonuses = {"fortaleza": 5}

    def attack(self):
        return self.fortaleza * 2

    def defend(self):
        return self.resistencia * 1.5

    def get_bonus_description(self):
        return f"Bonificación de Guerrer: +{self.bonuses['fortaleza']} fuerza"