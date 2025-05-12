import os

FILENAME = 'saved_usernames.py'
FILE_PATH = os.path.join(os.path.dirname(__file__), FILENAME)

def get_usernames():
    try:
        with open(FILE_PATH, 'r') as f:
            content = f.read()
            exec(content, globals())
        return usernames
    except FileNotFoundError:
        return []

def add_username(username):
    names = get_usernames()
    if username not in names:
        names.append(username)
        save_usernames(names)
        print(f"Nombre añadido: {username}")

def save_usernames(names):
    with open(FILE_PATH, 'w') as f:
        f.write("usernames = [\n")
        for name in names:
            f.write(f"    \"{name}\",\n")
        f.write("]\n")

if not os.path.exists(FILE_PATH):
    save_usernames([])

usernames = get_usernames()