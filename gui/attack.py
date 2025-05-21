import tkinter as tk
from tkinter import ttk, messagebox
from game.combat import Combat

class VentanaCombate:
    def __init__(self, root, jugador, enemigo, game_map):
        # Inicialitzem la finestra del combat
        self.root = root
        self.jugador = jugador
        self.enemigo = enemigo
        self.game_map = game_map
        
        # Creem una finestra flotant per al combat
        self.ventana_combat = tk.Toplevel(root)
        self.ventana_combat.title(f"Combate contra {enemigo.name}")  # Títol de la finestra
        self.ventana_combat.geometry("500x400")  # Mida de la finestra
        self.ventana_combat.configure(bg="#ffb375")  # Color de fons de la finestra
        
        # Creem la interfície gràfica per al combat
        self.crear_interfaz()

        # Creem l'objecte Combat que gestiona la lògica del combat
        self.combat = Combat(jugador, enemigo, self)

    def crear_interfaz(self):
        # Creem un frame per a les barres de vida
        frame_vida = tk.Frame(self.ventana_combat, bg="#ffb375")
        frame_vida.pack(pady=10)
        
        # Jugador
        # Barra de vida del jugador
        self.barra_vida_jugador = ttk.Progressbar(frame_vida, length=200, maximum=self.jugador.hp_max)
        self.barra_vida_jugador.grid(row=0, column=0, padx=10)
        self.label_vida_jugador = tk.Label(frame_vida, text=f"{self.jugador.name}: {self.jugador.hp}/{self.jugador.hp_max}", bg="#ffb375", fg="white")
        self.label_vida_jugador.grid(row=1, column=0)
        
        # Enemigo
        # Barra de vida de l'enemic
        self.barra_vida_enemigo = ttk.Progressbar(frame_vida, length=200, maximum=self.enemigo.hp_max)
        self.barra_vida_enemigo.grid(row=0, column=1, padx=10)
        self.label_vida_enemigo = tk.Label(frame_vida, text=f"{self.enemigo.name}: {self.enemigo.hp}/{self.enemigo.hp_max}", bg="#ffb375", fg="white")
        self.label_vida_enemigo.grid(row=1, column=1)
        
        # Log de combat
        # Text per mostrar l'historial de l'acció del combat
        self.log_combate = tk.Text(self.ventana_combat, height=15, width=50, bg="#9c714e", fg="white")
        self.log_combate.pack(pady=10)
        
        # Botons per les accions del jugador
        frame_botones = tk.Frame(self.ventana_combat, bg="#ffb375")
        frame_botones.pack(pady=10)
        
        # Botó per atacar
        self.btn_atacar = tk.Button(frame_botones, text="Atacar", bg="#94ff6e", fg="white", width=10, command=self.atacar)
        self.btn_atacar.grid(row=0, column=0, padx=5)
        
        # Botó per curar
        self.btn_curar = tk.Button(frame_botones, text="Curar (10%)", bg="#6edeff", fg="white", width=10, command=self.curar)
        self.btn_curar.grid(row=0, column=1, padx=5)
        
        # Botó per fugir
        self.btn_fugir = tk.Button(frame_botones, text="Fugir (15%)", bg="#ffd16e", fg="white", width=10, command=self.huir)
        self.btn_fugir.grid(row=0, column=2, padx=5)
        
        # Botó per tancar la finestra de combat (inicialment desactivat)
        self.btn_cerrar = tk.Button(frame_botones, text="Cerrar", bg="#ff7f6e", fg="white", width=10, command=self.cerrar_ventana, state=tk.DISABLED)
        self.btn_cerrar.grid(row=0, column=3, padx=5)

    def actualizar_barras_vida(self):
        # Actualitza les barres de vida del jugador i l'enemic
        if self.ventana_combat.winfo_exists():
            # Actualitza la barra de vida del jugador
            self.barra_vida_jugador['value'] = self.jugador.hp
            self.label_vida_jugador.config(text=f"{self.jugador.name}: {self.jugador.hp}/{self.jugador.hp_max}")
            
            # Actualitza la barra de vida de l'enemic
            self.barra_vida_enemigo['value'] = self.enemigo.hp
            self.label_vida_enemigo.config(text=f"{self.enemigo.name}: {self.enemigo.hp}/{self.enemigo.hp_max}")

    def agregar_log(self, mensaje):
        # Afegeix un missatge al log del combat
        if self.ventana_combat.winfo_exists():
            self.log_combate.insert(tk.END, mensaje + "\n")  # Afegeix el missatge al final del log
            self.log_combate.see(tk.END)  # Desplaça el text per veure el missatge més recent
    
    # Alias per compatibilitat amb el mètode en català
    def afegir_log(self, mensaje):
        self.agregar_log(mensaje)

    def finalizar_combate(self, resultado):
        # Finalitza el combat, mostrant el resultat i desactivant els botons
        if self.ventana_combat.winfo_exists():
            self.desactivar_botones_jugador()  # Desactiva els botons del jugador
            self.btn_cerrar.config(state=tk.NORMAL)  # Activa el botó de tancar finestra
            self.agregar_log(f"Combat finalitzat. Resultat: {resultado}")  # Afegeix missatge de finalització del combat
            if resultado == "Victoria":  # Si el jugador guanya, eliminen l'enemic
                self.game_map.eliminar_enemigo(self.jugador.x_pos, self.jugador.y_pos)

    def atacar(self):
        # Realitza un atac durant el torn del jugador
        self.combat.torn_jugador()

    def curar(self):
        # Intenta curar al jugador (10% de salut)
        self.combat.intentar_curar()

    def huir(self):
        # Intenta que el jugador fugi del combat (15% de probabilitats d'èxit)
        self.combat.intentar_huir()

    def activar_botones_jugador(self):
        # Activa els botons per a les accions del jugador
        if self.ventana_combat.winfo_exists():
            self.btn_atacar.config(state=tk.NORMAL)  # Activa el botó d'atacar
            self.btn_fugir.config(state=tk.NORMAL)    # Activa el botó de fugir
            if not self.combat.cura_utilitzada:  # Activa el botó de curar només si no s'ha utilitzat
                self.btn_curar.config(state=tk.NORMAL)

    def desactivar_botones_jugador(self):
        # Desactiva els botons de les accions del jugador després de cada torn
        if self.ventana_combat.winfo_exists():
            self.btn_atacar.config(state=tk.DISABLED)
            self.btn_fugir.config(state=tk.DISABLED)
            self.btn_curar.config(state=tk.DISABLED)

    def deshabilitar_boton_curar(self):
        # Desactiva el botó de curar
        if self.ventana_combat.winfo_exists():
            self.btn_curar.config(state=tk.DISABLED)

    def activar_boton_atacar(self):
        # Mètode de compatibilitat per a l'activació del botó d'atacar
        self.activar_botones_jugador()

    def desactivar_boton_atacar(self):
        # Mètode de compatibilitat per a la desactivació del botó d'atacar
        self.desactivar_botones_jugador()

    def cerrar_ventana(self):
        # Tanca la finestra del combat
        if self.ventana_combat.winfo_exists():
            self.ventana_combat.destroy()