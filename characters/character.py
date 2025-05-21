from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name):
        self.name = name
        self.hp = self.hp_max = 100
        self.fortaleza = self.magia = self.resistencia = self.exactitud = self.agilidad = 10

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

    def heal(self, amount):
        self.hp = min(self.hp_max, self.hp + amount)
        return amount

    def usar_habilidad(self):
        return {
            "tipo": "dañ",
            "valor": self.fortaleza,
            "mensaje": f"{self.name} usa una habilidad bàsica.",
        }