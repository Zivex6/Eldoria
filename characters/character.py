from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name):
        # Constructor de la classe Character
        # Inicialitzem els atributs bàsics que tindrà qualsevol personatge
        self.name = name  # Nom del personatge
        self.hp = self.hp_max = 100  # Vida actual i màxima (començant en 100)
        # Estadístiques base: tots els personatges comencen amb 10 punts en cada estadística
        self.fortaleza = self.magia = self.resistencia = self.exactitud = self.agilidad = 10

    @abstractmethod
    def attack(self):
        # Mètode abstracte: cada subclasse haurà d'implementar la seva pròpia versió
        # Aquest defineix com atacarà cada tipus de personatge
        pass

    @abstractmethod
    def defend(self):
        # Mètode abstracte: cada subclasse haurà d'implementar la seva pròpia versió
        # Aquest defineix com es defensarà cada tipus de personatge
        pass

    def heal(self, amount):
        # Mètode per curar el personatge
        # No pot superar la vida màxima (hp_max)
        self.hp = min(self.hp_max, self.hp + amount)
        return amount  # Retornem la quantitat curada

    def usar_habilidad(self):
        # Mètode genèric per utilitzar una habilitat
        # Cada subclasse podria sobreescriure'l si té habilitats específiques
        return {
            "tipo": "dañ",
            "valor": self.fortaleza,  # Dany basat en la força
            "mensaje": f"{self.name} usa una habilidad bàsica.",
        }