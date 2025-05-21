import random
import tkinter as tk
from tkinter import messagebox

class Combat:
    def __init__(self, jugador, enemic, finestra_combate):
        self.jugador = jugador
        self.enemic = enemic
        self.finestra_combate = finestra_combate
        self.cura_utilitzada = False

    def determinar_iniciativa(self):
        return random.randint(1, 20), random.randint(1, 20)

    def iniciar_combate(self):
        self.finestra_combate.agregar_log(f"¡Comença el combat contra {self.enemic.name}!")
        
        self.finestra_combate.agregar_log("Bonificacions del jugador:")
        if hasattr(self.jugador, 'bonuses'):
            for estat, valor in self.jugador.bonuses.items():
                self.finestra_combate.agregar_log(f"  +{valor} {estat}")
        else:
            self.finestra_combate.agregar_log("  No té bonificacions")
        
        iniciativa_jugador, iniciativa_enemic = self.determinar_iniciativa()
        self.finestra_combate.agregar_log(f"Iniciativa del jugador: {iniciativa_jugador}")
        self.finestra_combate.agregar_log(f"Iniciativa de l'enemic: {iniciativa_enemic}")
        
        if iniciativa_jugador >= iniciativa_enemic:
            self.finestra_combate.agregar_log("El jugador comença primer.")
            self.finestra_combate.activar_botones_jugador()
        else:
            self.finestra_combate.agregar_log("L'enemic comença primer.")
            self.finestra_combate.root.after(1000, self.torn_enemic)

    def torn_jugador(self):
        if self.finestra_combate.ventana_combat.winfo_exists():
            self.finestra_combate.desactivar_botones_jugador()
            damage, numero_aleatori = self.jugador.attack()
            self.enemic.hp = max(0, self.enemic.hp - damage)
            self.finestra_combate.agregar_log(f"{self.jugador.name} ha atacat i ha fet {damage} de punts de daño (Número aleatori: {numero_aleatori}).")
            self.finestra_combate.actualizar_barras_vida()

            if self.enemic.hp <= 0:
                self.finalitzar_combate("Victoria")
            else:
                self.finestra_combate.root.after(1000, self.torn_enemic)

    def torn_enemic(self):
        if self.finestra_combate.ventana_combat.winfo_exists():
            damage, numero_aleatori = self.enemic.attack()
            self.jugador.hp = max(0, self.jugador.hp - damage)
            self.finestra_combate.agregar_log(f"{self.enemic.name} ha atacat i ha fet {damage} de punts de daño (Número aleatori: {numero_aleatori}).")
            self.finestra_combate.actualizar_barras_vida()

            if self.jugador.hp <= 0:
                self.finalitzar_combate("Derrota")
            else:
                self.finestra_combate.activar_botones_jugador()

    def intentar_huir(self):
        if random.random() < 0.15:
            self.finestra_combate.agregar_log("¡Has pogut huir del combat!")
            self.finalitzar_combate("Huida")
        else:
            self.finestra_combate.agregar_log("No has pogut huir. L'enemic ataca.")
            self.torn_enemic()

    def intentar_curar(self):
        if self.cura_utilitzada:
            self.finestra_combate.agregar_log("¡Ja has utilitzat la teva poció de curació en aquest combat!")
            return
            
        if random.random() < 0.2:
            cura_quantitat = 30
            self.jugador.hp = min(self.jugador.hp_max, self.jugador.hp + cura_quantitat)
            self.finestra_combate.agregar_log(f"¡Has curat {cura_quantitat} punts de vida!")
            self.finestra_combate.actualizar_barras_vida()
            self.cura_utilitzada = True
            self.finestra_combate.deshabilitar_boton_curar()
            self.torn_enemic()
        else:
            self.finestra_combate.agregar_log("¡No has pogut curar-te! L'enemic ataca.")
            self.torn_enemic()

    def finalitzar_combate(self, resultat):
        self.finestra_combate.finalizar_combate(resultat)
        self.finestra_combate.desactivar_botones_jugador()
        
        if resultat == "Victoria":
            self.finestra_combate.agregar_log(f"Has guanyat el combat contra {self.enemic.name}.")
        elif resultat == "Derrota":
            self.finestra_combate.agregar_log("Has perdut el combat.")
            self.finestra_combate.root.after(1000, self.mostrar_derrota)
        elif resultat == "Huida":
            self.finestra_combate.agregar_log("Has huido del combat.")
        
        if resultat != "Derrota":
            self.finestra_combate.btn_cerrar.config(command=self.tancar_finestra_combate)
        else:
            self.finestra_combate.btn_cerrar.config(state="disabled")

    def mostrar_derrota(self):
        if self.finestra_combate.ventana_combat.winfo_exists():
            messagebox.showinfo("Derrota", "¡Has perdut el combat!")
            self.redirigir_al_menu_principal()

    def tancar_finestra_combate(self):
        if self.finestra_combate.ventana_combat.winfo_exists():
            self.finestra_combate.ventana_combat.destroy()
        
        if self.jugador.hp <= 0:
            self.redirigir_al_menu_principal()
        else:
            self.finestra_combate.game_map.actualitzar_mapa()

    def redirigir_al_menu_principal(self):
        if self.finestra_combate.ventana_combat.winfo_exists():
            self.finestra_combate.ventana_combat.destroy()
        
        if hasattr(self.finestra_combate.game_map, 'root') and self.finestra_combate.game_map.root.winfo_exists():
            self.finestra_combate.game_map.root.destroy()
        
        try:
            from gui.mainInterface import mainInterface
            root = tk.Tk()
            app = mainInterface(root)
            root.mainloop()
        except Exception as e:
            print(f"Error al carregar el menú principal: {e}")
            if tk._default_root and tk._default_root.winfo_exists():
                tk._default_root.destroy()