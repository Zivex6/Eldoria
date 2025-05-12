import random

class Combat:
    def __init__(self, jugador, enemigo, ventana_combate):
        self.jugador = jugador
        self.enemigo = enemigo
        self.ventana_combate = ventana_combate

    def iniciar_combate(self):
        self.ventana_combate.agregar_log(f"¡Comienza el combate contra {self.enemigo.name}!")
        
        # Mostrar bonuses del jugador
        self.ventana_combate.agregar_log("Bonuses del jugador:")
        if hasattr(self.jugador, 'bonuses'):
            for stat, value in self.jugador.bonuses.items():
                self.ventana_combate.agregar_log(f"  +{value} {stat}")
        else:
            self.ventana_combate.agregar_log("  No tiene bonuses")
        
        # Mostrar bonuses del enemigo
        self.ventana_combate.agregar_log("Bonuses del enemigo:")
        if hasattr(self.enemigo, 'bonuses'):
            for stat, value in self.enemigo.bonuses.items():
                self.ventana_combate.agregar_log(f"  +{value} {stat}")
        else:
            self.ventana_combate.agregar_log("  No tiene bonuses")
        
        iniciativa_jugador, iniciativa_enemigo = self.determinar_iniciativa()
        self.ventana_combate.agregar_log(f"Iniciativa del jugador: {iniciativa_jugador}")
        self.ventana_combate.agregar_log(f"Iniciativa del enemigo: {iniciativa_enemigo}")
        
        if iniciativa_jugador >= iniciativa_enemigo:
            self.ventana_combate.agregar_log("El jugador empieza primero.")
            self.ventana_combate.activar_boton_atacar()
        else:
            self.ventana_combate.agregar_log("El enemigo empieza primero.")
            self.ventana_combate.root.after(1000, self.turno_enemigo)

    def determinar_iniciativa(self):
        return random.randint(1, 20), random.randint(1, 20)

    def turno_jugador(self):
        if self.ventana_combate.ventana_combat.winfo_exists():
            self.ventana_combate.desactivar_boton_atacar()
            damage, random_number = self.jugador.attack()
            self.enemigo.hp = max(0, self.enemigo.hp - damage)  # Asegura que la vida no sea negativa
            self.ventana_combate.agregar_log(f"{self.jugador.name} ha atacado y ha hecho {damage} de daño (Número aleatorio: {random_number}).")
            self.ventana_combate.actualizar_barras_vida()

            if self.enemigo.hp <= 0:
                self.finalizar_combate("Victoria")
            else:
                self.ventana_combate.root.after(1000, self.turno_enemigo)

    def turno_enemigo(self):
        if self.ventana_combate.ventana_combat.winfo_exists():
            damage, random_number = self.enemigo.attack()
            self.jugador.hp = max(0, self.jugador.hp - damage)  # Asegura que la vida no sea negativa
            self.ventana_combate.agregar_log(f"{self.enemigo.name} ha atacado y ha hecho {damage} de daño (Número aleatorio: {random_number}).")
            self.ventana_combate.actualizar_barras_vida()

            if self.jugador.hp <= 0:
                self.finalizar_combate("Derrota")
                self.ventana_combate.root.after(2000, self.cerrar_ventana_combate)  # Cierra la ventana después de 2 segundos
            else:
                self.ventana_combate.activar_boton_atacar()

    def intentar_huir(self):
        if random.random() < 0.5:  # 50% de probabilidad de huir
            self.ventana_combate.agregar_log("Has logrado huir del combate.")
            self.finalizar_combate("Huida")
        else:
            self.ventana_combate.agregar_log("No has podido huir. El enemigo ataca.")
            self.turno_enemigo()

    def finalizar_combate(self, resultado):
        self.ventana_combate.finalizar_combate(resultado)
        self.ventana_combate.desactivar_boton_atacar()
        if resultado == "Victoria":
            self.ventana_combate.agregar_log(f"Has derrotado a {self.enemigo.name}.")
        elif resultado == "Derrota":
            self.ventana_combate.agregar_log("Has sido derrotado.")
        
        if resultado != "Derrota":
            self.ventana_combate.btn_cerrar.config(command=self.cerrar_ventana_combate)
        else:
            self.ventana_combate.btn_cerrar.config(state="disabled")  # Deshabilita el botón de cerrar en caso de derrota

    def cerrar_ventana_combate(self):
        if self.ventana_combate.ventana_combat.winfo_exists():
            self.ventana_combate.ventana_combat.destroy()
        
        # Si el jugador ha sido derrotado, cerrar también la ventana del mapa
        if self.jugador.hp <= 0:
            self.ventana_combate.game_map.root.destroy()
        else:
            # Actualizar el mapa si el jugador ha ganado o huido
            self.ventana_combate.game_map.actualitzar_mapa()