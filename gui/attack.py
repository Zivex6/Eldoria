import tkinter as tk
from tkinter import ttk
from game.combat import Combat

class VentanaCombate:
    def __init__(self, root, jugador, enemigo):
        self.root = root
        self.jugador = jugador
        self.enemigo = enemigo
        
        self.ventana_combat = tk.Toplevel(root)
        self.ventana_combat.title(f"Combate contra {enemigo.name}")
        self.ventana_combat.geometry("500x400")
        self.ventana_combat.configure(bg="#ffb375")
        self.ventana_combat.resizable(False, False)
        
        self.crear_interfaz()
        self.centrar_ventana()
        self.combat = Combat(jugador, enemigo, self)
        self.combat.iniciar_combate()

    def mostrar_info_personajes(self):
        jugador_info = f"{self.jugador.name} - {self.jugador.character.__class__.__name__}\n"
        jugador_info += self.jugador.character.get_bonus_description()
        self.agregar_log(jugador_info)

        enemigo_info = f"{self.enemigo.name}\n"
        if hasattr(self.enemigo, 'get_bonus_description'):
            enemigo_info += self.enemigo.get_bonus_description()
        self.agregar_log(enemigo_info)

    def crear_interfaz(self):
        # Frame para las barras de vida
        frame_vida = tk.Frame(self.ventana_combat, bg="#ffb375")
        frame_vida.pack(pady=10)

        # Barra de vida del jugador
        self.barra_vida_jugador = ttk.Progressbar(frame_vida, length=200, maximum=self.jugador.hp_max)
        self.barra_vida_jugador.grid(row=0, column=0, padx=10)
        self.label_vida_jugador = tk.Label(frame_vida, text=f"{self.jugador.name}: {self.jugador.hp}/{self.jugador.hp_max}", bg="#ffb375", fg="white")
        self.label_vida_jugador.grid(row=1, column=0)

        # Barra de vida del enemigo
        self.barra_vida_enemigo = ttk.Progressbar(frame_vida, length=200, maximum=self.enemigo.hp_max)
        self.barra_vida_enemigo.grid(row=0, column=1, padx=10)
        self.label_vida_enemigo = tk.Label(frame_vida, text=f"{self.enemigo.name}: {self.enemigo.hp}/{self.enemigo.hp_max}", bg="#ffb375", fg="white")
        self.label_vida_enemigo.grid(row=1, column=1)

        # Área de texto para el log de combate
        self.log_combate = tk.Text(self.ventana_combat, height=15, width=50, bg="#9c714e", fg="white")
        self.log_combate.pack(pady=10)

        # Frame para los botones
        frame_botones = tk.Frame(self.ventana_combat, bg="#ffb375")
        frame_botones.pack(pady=10)

        # Botón de atacar
        self.btn_atacar = tk.Button(frame_botones, text="Atacar", bg="#94ff6e", fg="white", width=10, command=self.atacar)
        self.btn_atacar.grid(row=0, column=0, padx=5)

        # Botón de cerrar
        self.btn_cerrar = tk.Button(frame_botones, text="Cerrar", bg="#ff7f6e", fg="white", width=10, command=self.cerrar_ventana, state=tk.DISABLED)
        self.btn_cerrar.grid(row=0, column=1, padx=5)

    def centrar_ventana(self):
        self.ventana_combat.update_idletasks()
        width = self.ventana_combat.winfo_width()
        height = self.ventana_combat.winfo_height()
        x = (self.ventana_combat.winfo_screenwidth() // 2) - (width // 2)
        y = (self.ventana_combat.winfo_screenheight() // 2) - (height // 2)
        self.ventana_combat.geometry(f'{width}x{height}+{x}+{y}')

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

    def finalizar_combate(self, resultado):
        if self.ventana_combat.winfo_exists():
            self.btn_atacar.config(state=tk.DISABLED)
            self.btn_cerrar.config(state=tk.NORMAL)
            self.agregar_log(f"Combate finalizado. Resultado: {resultado}")

    def atacar(self):
        self.combat.turno_jugador()

    def activar_boton_atacar(self):
        if self.ventana_combat.winfo_exists():
            self.btn_atacar.config(state=tk.NORMAL)

    def desactivar_boton_atacar(self):
        if self.ventana_combat.winfo_exists():
            self.btn_atacar.config(state=tk.DISABLED)

    def cerrar_ventana(self):
        if self.ventana_combat.winfo_exists():
            self.ventana_combat.destroy()

if __name__ == "__main__":
    # Código de prueba
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    class MockCharacter:
        def __init__(self, name, hp, hp_max):
            self.name = name
            self.hp = hp
            self.hp_max = hp_max

    jugador = MockCharacter("Héroe", 100, 100)
    enemigo = MockCharacter("Orco", 80, 80)

    ventana_combate = VentanaCombate(root, jugador, enemigo)
    ventana_combate.agregar_log("¡Comienza el combate!")
    ventana_combate.ventana_combat.mainloop()