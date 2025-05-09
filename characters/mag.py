from .character import Character

class Mag(Character):
    def __init__(self, name):
        super().__init__(name)
        self.magic += 5  # Mages have extra magic
        self.bonuses = {
            "magic": 5
        }

    def attack(self):
        return self.magic * 2

    def defend(self):
        return self.resistance

    def get_bonus_description(self):
        return f"Bonificación de Mag: +{self.bonuses['magic']} magia"