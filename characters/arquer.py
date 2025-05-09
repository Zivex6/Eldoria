from .character import Character

class Arquer(Character):
    def __init__(self, name):
        super().__init__(name)
        self.accuracy += 5  # Archers have extra accuracy
        self.bonuses = {
            "accuracy": 5
        }

    def attack(self):
        return self.accuracy * 2

    def defend(self):
        return self.agility * 1.2

    def get_bonus_description(self):
        return f"Bonificación de Arquer: +{self.bonuses['accuracy']} precisión"