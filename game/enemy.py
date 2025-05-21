import random
from characters.character import Character

nombre_enemigos = ["Troll", "Orco", "Goblin", "Ogro"]

class Enemigo(Character):
    def __init__(self):
        nombre = random.choice(nombre_enemigos)
        super().__init__(nombre)
        self.hp = self.hp_max = random.randint(50, 100)
        self.fortaleza = random.randint(5, 15)
        self.agilidad = random.randint(5, 15)
        self.bonuses = {}

    def attack(self):
        damage = random.randint(self.fortaleza - 2, self.fortaleza + 2)
        return damage, random.randint(1, 20)

    def defend(self):
        return self.agilidad

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, value)

class Enemics:
    def __init__(self, files, columnes):
        self.enemigos = {}
        self.generar_enemigos(files, columnes)

    def generar_enemigos(self, files, columnes):
        num_enemigos = (files * columnes) // 10
        for _ in range(num_enemigos):
            x, y = random.randint(0, columnes - 1), random.randint(0, files - 1)
            while x == 0 and y == 0:
                x, y = random.randint(0, columnes - 1), random.randint(0, files - 1)
            self.enemigos[(x, y)] = Enemigo()

    def hay_enemigo(self, x, y):
        return (x, y) in self.enemigos

    def obtener_enemigo(self, x, y):
        return self.enemigos.get((x, y))

    def obtenir_posicions(self):
        return self.enemigos.keys()

def determinar_iniciativa(jugador, enemigo):
    return random.randint(1, 20), random.randint(1, 20)