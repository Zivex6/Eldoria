import os
import json

nombre_archivo = 'usuaris.json'
FILE_PATH = os.path.join(os.path.dirname(__file__), nombre_archivo)

def get_usernames():
    try:
        with open(FILE_PATH, 'r') as f:  # Obrir fitxer per llegir
            return json.load(f)  # Carregar les dades en format JSON
    except (FileNotFoundError, json.JSONDecodeError):  # Si no es pot llegir, tornar llista buida
        return []

def add_username(username):
    names = get_usernames()  # Obtenir llista de noms
    if username not in names:  # Si el nom no existeix
        names.append(username)  # Afegir-lo a la llista
        save_usernames(names)  # Guardar llista actualitzada
        print(f"Nom afegit: {username}")

def save_usernames(names):
    with open(FILE_PATH, 'w') as f:  # Obrir fitxer per escriure
        json.dump(names, f, indent=4)  # Guardar llista com JSON

if not os.path.exists(FILE_PATH):  # Si el fitxer no existeix
    save_usernames([])  # Crear fitxer amb llista buida

usernames = get_usernames()  # Carregar els noms dels usuaris