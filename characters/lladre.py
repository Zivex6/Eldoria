from .character import Character

class Lladre(Character):
    def __init__(self, name):
        super().__init__(name)
        self.agilidad += 5
        self.bonuses = {"agilidad": 5}

    def attack(self):
        return self.fortaleza * 1.5

    def defend(self):
        return self.agilidad * 1.5

    def get_bonus_description(self):
        return f"Bonificación de Lladre: +{self.bonuses['agilidad']} agilidad"