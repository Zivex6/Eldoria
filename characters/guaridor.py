from .character import Character

class Guaridor(Character):
    def __init__(self, name):
        super().__init__(name)
        self.magic += 3  # Healers have extra magic
        self.hp += 20  # Healers have extra HP
        self.bonuses = {
            "magic": 3,
            "hp": 20
        }

    def attack(self):
        return self.magic * 1.5

    def defend(self):
        return self.resistance * 1.2

    def heal_ally(self, ally):
        heal_amount = self.magic * 2
        ally.heal(heal_amount)
        return heal_amount

    def get_bonus_description(self):
        return f"Bonificación de Guaridor: +{self.bonuses['magic']} magia, +{self.bonuses['hp']} HP"