from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.hp_max = 100
        self.strength = 10
        self.magic = 10
        self.resistance = 10
        self.accuracy = 10
        self.agility = 10
        self.x_pos = 0  # Añade esta línea
        self.y_pos = 0  # Añade esta línea

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

    def usar_habilidad(self):
        return {
            'tipo': 'daño',
            'valor': self.strength,
            'mensaje': f"{self.name} usa una habilidad básica."
        }