import json
from auth.utils import caesar_cipher, load_users

def authenticate():
    users = load_users()
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    encrypted_pass = caesar_cipher(password, 6)
    
    if username in users and users[username] == encrypted_pass:
        print("✅ Login Successful!")
        return True
    else:
        print("❌ Invalid username or password. Try again.")
        return False

# Shift Value: 6
