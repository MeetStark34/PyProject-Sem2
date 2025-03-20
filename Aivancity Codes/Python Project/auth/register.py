import json
from auth.utils import caesar_cipher, load_users, save_users

def create_account():
    users = load_users()
    username = input("Choose a username: ")
    
    if username in users:
        print("❌ Username already taken. Try another.")
        return
    
    password = input("Choose a password: ")
    users[username] = caesar_cipher(password, 6)
    save_users(users)
    print("✅ Account created successfully!")

# Shift Value: 6