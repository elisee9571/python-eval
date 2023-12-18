import hashlib
import os

def read_file(file):
    md5_file = file + '.md5'
    if os.path.exists(md5_file):
        with open(md5_file, 'r') as f:
            return f.read().strip()
    return False


def hash_file(file):
    hasher = hashlib.md5()
    with open(file, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()


def save_empreinte(file, empreinte):
    with open(file + '.md5', 'w') as f:
        f.write(empreinte)


def check_file(file):
    empreinte = read_file(file)

    if empreinte:
        empreinte_current = hash_file(file)

        if empreinte_current == empreinte:
            print("Le fichier est intact.")
        else:
            print("Le fichier a été modifié.")
    else:
        print("Aucune empreinte MD5 enregistrée. Enregistrement de l'empreinte MD5.")
        empreinte_current = hash_file(file)
        save_empreinte(file, empreinte_current)


path_file = input("Veuillez spécifier le chemin vers le fichier : ")

if os.path.exists(path_file):
    check_file(path_file)
else:
    print("Le fichier spécifié n'existe pas.")
