from .character import Character

class Guaridor(Character):
    def __init__(self, name):
        # Constructor de la classe Guaridor
        super().__init__(name)  # Cridem al constructor de la classe pare (Character)
        self.magia += 1  # Els guaridors tenen +3 de màgia extra
        self.hp += 20  # Els guaridors tenen +20 de vida extra
        self.bonuses = {"magia": 1, "hp": 20}  # Guardem els bonificadors per poder mostrar-los

    def attack(self):
        # Implementació de l'atac del guaridor
        # Els guaridors fan un dany basat en màgia x1.5 (menys que el mag però poden curar)
        return self.magia * 1.5

    def defend(self):
        # Implementació de la defensa del guaridor
        # Els guaridors tenen una defensa basada en resistència x1.2
        return self.resistencia * 1.2

    def heal_ally(self, ally):
        # Habilitat especial del guaridor: curar a un aliat
        heal_amount = self.magia * 2  # Quantitat de curació basada en la màgia
        ally.heal(heal_amount)  # Apliquem la curació a l'aliat
        return heal_amount  # Retornem la quantitat curada

    def get_bonus_description(self):
        # Retorna una descripció dels bonificadors d'aquesta classe
        return f"Bonificació del Guaridor: +{self.bonuses['magia']} magia, +{self.bonuses['hp']} HP"