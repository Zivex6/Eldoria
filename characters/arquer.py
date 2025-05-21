from .character import Character

class Arquer(Character):
    def __init__(self, name):
        # Constructor de la classe Arquer
        super().__init__(name)  # Cridem al constructor de la classe pare (Character)
        self.exactitud += 2  # Els arquers tenen +5 de precisió extra
        self.bonuses = {"exactitud": 2}  # Guardem els bonificadors per poder mostrar-los

    def attack(self):
        # Implementació de l'atac de l'arquer
        # Els arquers fan el doble de dany segons la seva precisió
        return self.exactitud * 2

    def defend(self):
        # Implementació de la defensa de l'arquer
        # Els arquers tenen una defensa basada en agilitat x1.2
        return self.agilidad * 1.2

    def get_bonus_description(self):
        # Retorna una descripció dels bonificadors d'aquesta classe
        return f"Bonificació de l'arquer: +{self.bonuses['exactitud']} precisió"