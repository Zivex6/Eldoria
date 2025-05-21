import random
import tkinter as tk
from tkinter import messagebox

class Combat:
    def __init__(self, jugador, enemic, finestra_combate): # Constructor d'una classe
        # Constructor de la classe Combat
        self.jugador = jugador  # El jugador
        self.enemic = enemic  # L'enemic contra qui lluitem
        self.finestra_combate = finestra_combate  # Referència a la interfície de combat
        self.cura_utilitzada = False  # Controlar si ja s'ha utilitzat la curació

    def determinar_iniciativa(self):
        # Determina qui comença el combat
        # Retorna dos números aleatoris del 1 al 20, un pel jugador i un per l'enemic
        return random.randint(1, 20), random.randint(1, 20)

    def iniciar_combate(self):
        # Inicia el combat
        self.finestra_combate.agregar_log(f"¡Comença el combat contra {self.enemic.name}!")
        
        # Mostrem les bonificacions del jugador
        self.finestra_combate.agregar_log("Bonificacions del jugador:")
        if hasattr(self.jugador, 'bonuses'): # Comprovar si l'objecte jugador té l'atribut bonuses
            for estat, valor in self.jugador.bonuses.items():
                self.finestra_combate.agregar_log(f"  +{valor} {estat}")
        else:
            self.finestra_combate.agregar_log("  No té bonificacions")
        
        # Tirem iniciativa per determinar qui comença
        iniciativa_jugador, iniciativa_enemic = self.determinar_iniciativa()
        self.finestra_combate.agregar_log(f"Iniciativa del jugador: {iniciativa_jugador}")
        self.finestra_combate.agregar_log(f"Iniciativa de l'enemic: {iniciativa_enemic}")
        
        # Decidim qui comença segons la iniciativa
        if iniciativa_jugador >= iniciativa_enemic:
            self.finestra_combate.agregar_log("El jugador comença primer.")
            self.finestra_combate.activar_botones_jugador()  # Activem els botons del jugador
        else:
            self.finestra_combate.agregar_log("L'enemic comença primer.")
            # Programem el torn de l'enemic després d'un segon
            self.finestra_combate.root.after(1000, self.torn_enemic)

    def torn_jugador(self):
        # Torn d'atac del jugador
        if self.finestra_combate.ventana_combat.winfo_exists():
            self.finestra_combate.desactivar_botones_jugador()  # Desactivem botons per evitar clicks múltiples
            damage, numero_aleatori = self.jugador.attack()  # El jugador ataca
            self.enemic.hp = max(0, self.enemic.hp - damage)  # Apliquem el dany
            self.finestra_combate.agregar_log(f"{self.jugador.name} ha atacat i ha fet {damage} de punts de dañ (Número aleatori: {numero_aleatori}).")
            self.finestra_combate.actualizar_barras_vida()  # Actualitzem les barres de vida

            # Comprovem si l'enemic ha mort
            if self.enemic.hp <= 0:
                self.finalitzar_combate("Victoria")
            else:
                # Si l'enemic segueix viu, programem el seu torn després d'un segon
                self.finestra_combate.root.after(1000, self.torn_enemic)

    def torn_enemic(self):
        # Torn d'atac de l'enemic
        if self.finestra_combate.ventana_combat.winfo_exists():
            damage, numero_aleatori = self.enemic.attack()  # L'enemic ataca
            self.jugador.hp = max(0, self.jugador.hp - damage)  # Apliquem el dany
            self.finestra_combate.agregar_log(f"{self.enemic.name} ha atacat i ha fet {damage} de punts de daño (Número aleatori: {numero_aleatori}).")
            self.finestra_combate.actualizar_barras_vida()  # Actualitzem les barres de vida

            # Comprovem si el jugador ha mort
            if self.jugador.hp <= 0:
                self.finalitzar_combate("Derrota")
            else:
                # Si el jugador segueix viu, activem els seus botons per al següent torn
                self.finestra_combate.activar_botones_jugador()

    def intentar_huir(self):
        # Intentar fugir del combat
        if random.random() < 0.15:  # 15% de probabilitat d'èxit
            self.finestra_combate.agregar_log("¡Has pogut fugir del combat!")
            self.finalitzar_combate("Huida")
        else:
            # Si no podem fugir, l'enemic ataca
            self.finestra_combate.agregar_log("No has pogut fugir. L'enemic ataca.")
            self.torn_enemic()

    def intentar_curar(self):
        # Intentar curar-se durant el combat
        if self.cura_utilitzada:
            # Només es pot curar un cop per combat
            self.finestra_combate.agregar_log("¡Ja has utilitzat la teva poció de curació en aquest combat!")
            return
            
        if random.random() < 0.20:  # 20% de probabilitat d'èxit
            cura_quantitat = 60  # Quantitat fixa de curació
            self.jugador.hp = min(self.jugador.hp_max, self.jugador.hp + cura_quantitat)
            self.finestra_combate.agregar_log(f"¡Has curat {cura_quantitat} punts de vida!")
            self.finestra_combate.actualizar_barras_vida()
            self.cura_utilitzada = True  # Marquem que ja s'ha utilitzat la curació
            self.finestra_combate.deshabilitar_boton_curar()  # Desactivem el botó
            self.torn_enemic()  # L'enemic ataca després
        else:
            # Si falla la curació, l'enemic ataca
            self.finestra_combate.agregar_log("¡No has pogut curar-te! L'enemic ataca.")
            self.torn_enemic()

    def finalitzar_combate(self, resultat):
        # Finalitza el combat amb un resultat determinat (Victoria, Derrota, Huida)
        self.finestra_combate.finalizar_combate(resultat)
        self.finestra_combate.desactivar_botones_jugador()
        
        # Mostrem el missatge adequat segons el resultat
        if resultat == "Victoria":
            self.finestra_combate.agregar_log(f"Has guanyat el combat contra {self.enemic.name}.")
        elif resultat == "Derrota":
            self.finestra_combate.agregar_log("Has perdut el combat.")
            # Mostrem el missatge de derrota després d'un segon
            self.finestra_combate.root.after(1000, self.mostrar_derrota)
        elif resultat == "Huida":
            self.finestra_combate.agregar_log("Has fugit del combat.")
        
        # Configurem el comportament del botó tancar segons el resultat
        if resultat != "Derrota":
            self.finestra_combate.btn_cerrar.config(command=self.tancar_finestra_combate)
        else:
            self.finestra_combate.btn_cerrar.config(state="disabled")

    def mostrar_derrota(self):
        # Mostra un missatge de derrota i va al menú principal
        if self.finestra_combate.ventana_combat.winfo_exists():
            messagebox.showinfo("Derrota", "¡Has perdut el combat!")
            self.redirigir_al_menu_principal()

    def tancar_finestra_combate(self):
        # Tanca la finestra de combat i torna al joc si el jugador segueix viu
        if self.finestra_combate.ventana_combat.winfo_exists():
            self.finestra_combate.ventana_combat.destroy()
        
        if self.jugador.hp <= 0:
            self.redirigir_al_menu_principal()
        else:
            self.finestra_combate.game_map.actualitzar_mapa()

    def redirigir_al_menu_principal(self):
        # Torna al menú principal (es crida després d'una derrota)
        if self.finestra_combate.ventana_combat.winfo_exists():
            self.finestra_combate.ventana_combat.destroy()
        
        # Tanquem la finestra del mapa si existeix
        if hasattr(self.finestra_combate.game_map, 'root') and self.finestra_combate.game_map.root.winfo_exists():
            self.finestra_combate.game_map.root.destroy()
        
        try:
            # Intentem carregar el menú principal
            from gui.mainInterface import mainInterface
            root = tk.Tk()
            app = mainInterface(root)
            root.mainloop()
        except Exception as e:
            # Gestionem possibles errors
            print(f"Error al carregar el menú principal: {e}")
            if tk._default_root and tk._default_root.winfo_exists():
                tk._default_root.destroy()