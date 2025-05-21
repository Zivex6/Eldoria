import tkinter as tk  # Importa la biblioteca tkinter per crear interfícies gràfiques
import os  # Importa el mòdul os per interactuar amb el sistema operatiu
import sys  # Importa el mòdul sys per manipular l'entorn del sistema

# Afegeix el directori actual al sistema de rutes de cerca de mòduls
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importa la classe 'mainInterface' des del fitxer 'mainInterface' que es troba al directori 'gui'
from gui.mainInterface import mainInterface

# Aquesta secció assegura que el bloc de codi s'executi només quan s'executa aquest fitxer directament,
# i no quan es importa com a mòdul en un altre script
if __name__ == "__main__":
    # Crea una finestra principal utilitzant tkinter
    root = tk.Tk()
    
    # Crea una instància de la classe 'mainInterface' i li passa la finestra 'root'
    app = mainInterface(root)
    
    # Comença el bucle principal d'esdeveniments de tkinter, que manté la finestra oberta
    root.mainloop()