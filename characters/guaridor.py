from .character import Character

class Guaridor(Character):
    def __init__(self, name):
        super().__init__(name)
        self.magia += 3
        self.hp += 20
        self.bonuses = {"magia": 3, "hp": 20}

    def attack(self):
        return self.magia * 1.5

    def defend(self):
        return self.resistencia * 1.2

    def heal_ally(self, ally):
        heal_amount = self.magia * 2
        ally.heal(heal_amount)
        return heal_amount

    def get_bonus_description(self):
        return f"Bonificació del Guaridor: +{self.bonuses['magia']} magia, +{self.bonuses['hp']} HP"