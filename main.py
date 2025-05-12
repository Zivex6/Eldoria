import tkinter as tk
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui.mainInterface import mainInterface

if __name__ == "__main__":
    root = tk.Tk()
    app = mainInterface(root)
    root.mainloop()