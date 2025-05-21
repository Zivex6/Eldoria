from .character import Character

class Lladre(Character):
    def __init__(self, name):
        # Constructor de la classe Lladre
        super().__init__(name)  # Cridem al constructor de la classe pare (Character)
        self.agilidad += 2  # Els lladres tenen +5 d'agilitat extra
        self.bonuses = {"agilidad": 2}  # Guardem els bonificadors per poder mostrar-los

    def attack(self):
        # Implementació de l'atac del lladre
        # Els lladres fan un dany de força x1.5 (menys que el guerrer però més àgils)
        return self.fortaleza * 1.5

    def defend(self):
        # Implementació de la defensa del lladre
        # Els lladres tenen una defensa basada en agilitat x1.5
        return self.agilidad * 1.5

    def get_bonus_description(self):
        # Retorna una descripció dels bonificadors d'aquesta classe
        return f"Bonificación de Lladre: +{self.bonuses['agilidad']} agilidad"