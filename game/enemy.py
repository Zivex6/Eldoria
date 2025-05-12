import random
from characters.character import Character

# Lista de nombres de enemigos
NOMBRES_ENEMIGOS = [
    "Troll",
    "Orco",
    "Goblin",
    "Ogro"
]

class Enemigo(Character):
    def __init__(self):
        nombre = random.choice(NOMBRES_ENEMIGOS)
        super().__init__(nombre)
        self.hp = random.randint(50, 100)
        self.hp_max = self.hp
        self.strength = random.randint(5, 15)
        self.agility = random.randint(5, 15)

    def attack(self):
        damage = random.randint(self.strength - 2, self.strength + 2)
        return damage, random.randint(1, 20)  # Devuelve el daño y un número aleatorio

    def defend(self):
        return self.agility

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = max(0, value)  # Asegura que la vida no sea negativa

class Enemics:
    def __init__(self, files, columnes):
        self.enemigos = {}
        self.generar_enemigos(files, columnes)

    def generar_enemigos(self, files, columnes):
        # Genera enemigos aleatoriamente en el mapa
        num_enemigos = (files * columnes) // 10  # Por ejemplo, 10% del mapa
        for _ in range(num_enemigos):
            x = random.randint(0, columnes - 1)
            y = random.randint(0, files - 1)
            # Evita generar un enemigo en la posición (0,0)
            while x == 0 and y == 0:
                x = random.randint(0, columnes - 1)
                y = random.randint(0, files - 1)
            self.enemigos[(x, y)] = Enemigo()

    def hay_enemigo(self, x, y):
        return (x, y) in self.enemigos

    def obtener_enemigo(self, x, y):
        return self.enemigos.get((x, y))

    def obtenir_posicions(self):
        return self.enemigos.keys()

def determinar_iniciativa(jugador, enemigo):
    iniciativa_jugador = random.randint(1, 20)
    iniciativa_enemigo = random.randint(1, 20)
    return (iniciativa_jugador, iniciativa_enemigo)