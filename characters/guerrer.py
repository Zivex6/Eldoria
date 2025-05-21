from .character import Character

class Guerrer(Character):
    def __init__(self, name):
        # Constructor de la classe Guerrer
        super().__init__(name)  # Cridem al constructor de la classe pare (Character)
        self.fortaleza += 3  # Els guerrers tenen +5 de força extra
        self.bonuses = {"fortaleza": 3}  # Guardem els bonificadors per poder mostrar-los

    def attack(self):
        # Implementació de l'atac del guerrer
        # Els guerrers fan el doble de dany segons la seva força
        return self.fortaleza * 2

    def defend(self):
        # Implementació de la defensa del guerrer
        # Els guerrers tenen una defensa basada en resistència x1.5
        return self.resistencia * 1.5

    def get_bonus_description(self):
        # Retorna una descripció dels bonificadors d'aquesta classe
        return f"Bonificación de Guerrer: +{self.bonuses['fortaleza']} fuerza"