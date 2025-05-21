from .character import Character

class Mag(Character):
    def __init__(self, name):
        # Constructor de la classe Mag
        super().__init__(name)  # Cridem al constructor de la classe pare (Character)
        self.magia += 1  # Els mags tenen +5 de màgia extra
        self.bonuses = {"magia": 1}  # Guardem els bonificadors per poder mostrar-los

    def attack(self):
        # Implementació de l'atac del mag
        # Els mags fan el doble de dany segons la seva màgia
        return self.magia * 2

    def defend(self):
        # Implementació de la defensa del mag
        # Els mags tenen una defensa basada només en resistència (sense multiplicador)
        return self.resistencia

    def get_bonus_description(self):
        # Retorna una descripció dels bonificadors d'aquesta classe
        return f"Bonificación de Mag: +{self.bonuses['magia']} magia"