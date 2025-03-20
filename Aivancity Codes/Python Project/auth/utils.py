import json
import os

FICHIER_UTILISATEUR = "users.json"

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            Originale = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - Originale + shift) % 26 + Originale)
        else:
            result += char
    return result

def load_users():
    if os.path.exists(FICHIER_UTILISATEUR):
        with open(FICHIER_UTILISATEUR, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(FICHIER_UTILISATEUR, "w") as f:
        json.dump(users, f, indent=4)


# A -> 65 and a -> 97
# IF B -> 66 
# B - A + Shift % 26 + A
# 66 - 65 + 3 % 26 + 65
# 1 + 3 % 26 + 65
# 4 % 26 + 65
# 4 + 65
# 69
#UNICODE VS ASCII