from .character import Character

class Lladre(Character):
    def __init__(self, name):
        super().__init__(name)
        self.agility += 5  # Thieves have extra agility
        self.bonuses = {
            "agility": 5
        }

    def attack(self):
        return self.strength * 1.5

    def defend(self):
        return self.agility * 1.5

    def get_bonus_description(self):
        return f"Bonificación de Lladre: +{self.bonuses['agility']} agilidad"