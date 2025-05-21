import tkinter as tk
from tkinter import ttk, messagebox
from game.combat import Combat

class VentanaCombate:
    def __init__(self, root, jugador, enemigo, game_map):
        self.root = root
        self.jugador = jugador
        self.enemigo = enemigo
        self.game_map = game_map
        
        self.ventana_combat = tk.Toplevel(root)
        self.ventana_combat.title(f"Combate contra {enemigo.name}")
        self.ventana_combat.geometry("500x400")
        self.ventana_combat.configure(bg="#ffb375")
        
        self.crear_interfaz()
        self.combat = Combat(jugador, enemigo, self)

    def crear_interfaz(self):
        # Barras de vida
        frame_vida = tk.Frame(self.ventana_combat, bg="#ffb375")
        frame_vida.pack(pady=10)
        
        # Jugador
        self.barra_vida_jugador = ttk.Progressbar(frame_vida, length=200, maximum=self.jugador.hp_max)
        self.barra_vida_jugador.grid(row=0, column=0, padx=10)
        self.label_vida_jugador = tk.Label(frame_vida, text=f"{self.jugador.name}: {self.jugador.hp}/{self.jugador.hp_max}", bg="#ffb375", fg="white")
        self.label_vida_jugador.grid(row=1, column=0)
        
        # Enemigo
        self.barra_vida_enemigo = ttk.Progressbar(frame_vida, length=200, maximum=self.enemigo.hp_max)
        self.barra_vida_enemigo.grid(row=0, column=1, padx=10)
        self.label_vida_enemigo = tk.Label(frame_vida, text=f"{self.enemigo.name}: {self.enemigo.hp}/{self.enemigo.hp_max}", bg="#ffb375", fg="white")
        self.label_vida_enemigo.grid(row=1, column=1)
        
        # Log de combate
        self.log_combate = tk.Text(self.ventana_combat, height=15, width=50, bg="#9c714e", fg="white")
        self.log_combate.pack(pady=10)
        
        # Botones
        frame_botones = tk.Frame(self.ventana_combat, bg="#ffb375")
        frame_botones.pack(pady=10)
        
        self.btn_atacar = tk.Button(frame_botones, text="Atacar", bg="#94ff6e", fg="white", width=10, command=self.atacar)
        self.btn_atacar.grid(row=0, column=0, padx=5)
        
        # Añadimos el botón de curación
        self.btn_curar = tk.Button(frame_botones, text="Curar (10%)", bg="#6edeff", fg="white", width=10, command=self.curar)
        self.btn_curar.grid(row=0, column=1, padx=5)
        
        self.btn_huir = tk.Button(frame_botones, text="Huir (15%)", bg="#ffd16e", fg="white", width=10, command=self.huir)
        self.btn_huir.grid(row=0, column=2, padx=5)
        
        self.btn_cerrar = tk.Button(frame_botones, text="Cerrar", bg="#ff7f6e", fg="white", width=10, command=self.cerrar_ventana, state=tk.DISABLED)
        self.btn_cerrar.grid(row=0, column=3, padx=5)

    def actualizar_barras_vida(self):
        if self.ventana_combat.winfo_exists():
            self.barra_vida_jugador['value'] = self.jugador.hp
            self.label_vida_jugador.config(text=f"{self.jugador.name}: {self.jugador.hp}/{self.jugador.hp_max}")
            
            self.barra_vida_enemigo['value'] = self.enemigo.hp
            self.label_vida_enemigo.config(text=f"{self.enemigo.name}: {self.enemigo.hp}/{self.enemigo.hp_max}")

    def agregar_log(self, mensaje):
        if self.ventana_combat.winfo_exists():
            self.log_combate.insert(tk.END, mensaje + "\n")
            self.log_combate.see(tk.END)
    
    # Alias para mantener compatibilidad con ambos nombres de métodos
    def afegir_log(self, mensaje):
        self.agregar_log(mensaje)

    def finalizar_combate(self, resultado):
        if self.ventana_combat.winfo_exists():
            self.desactivar_botones_jugador()
            self.btn_cerrar.config(state=tk.NORMAL)
            self.agregar_log(f"Combat finalitzat. Resultat: {resultado}")
            if resultado == "Victoria":
                self.game_map.eliminar_enemigo(self.jugador.x_pos, self.jugador.y_pos)

    def atacar(self):
        self.combat.torn_jugador()
        
    def curar(self):
        self.combat.intentar_curar()
        
    def huir(self):
        self.combat.intentar_huir()

    def activar_botones_jugador(self):
        if self.ventana_combat.winfo_exists():
            self.btn_atacar.config(state=tk.NORMAL)
            self.btn_huir.config(state=tk.NORMAL)
            if not self.combat.cura_utilitzada:
                self.btn_curar.config(state=tk.NORMAL)

    def desactivar_botones_jugador(self):
        if self.ventana_combat.winfo_exists():
            self.btn_atacar.config(state=tk.DISABLED)
            self.btn_huir.config(state=tk.DISABLED)
            self.btn_curar.config(state=tk.DISABLED)

    def deshabilitar_boton_curar(self):
        if self.ventana_combat.winfo_exists():
            self.btn_curar.config(state=tk.DISABLED)

    def activar_boton_atacar(self):
        # Método de compatibilidad para código existente
        self.activar_botones_jugador()

    def desactivar_boton_atacar(self):
        # Método de compatibilidad para código existente
        self.desactivar_botones_jugador()

    def cerrar_ventana(self):
        if self.ventana_combat.winfo_exists():
            self.ventana_combat.destroy