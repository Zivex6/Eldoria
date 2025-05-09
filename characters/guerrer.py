from .character import Character

class Guerrer(Character):
    def __init__(self, name):
        super().__init__(name)
        self.strength += 5  # Warriors have extra strength
        self.bonuses = {
            "strength": 5
        }

    def attack(self):
        return self.strength * 2

    def defend(self):
        return self.resistance * 1.5

    def get_bonus_description(self):
        return f"Bonificación de Guerrer: +{self.bonuses['strength']} fuerza"