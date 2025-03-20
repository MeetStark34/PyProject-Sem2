import json
from auth.utils import caesar_cipher, load_users, save_users

def reset_user_password():
    users = load_users()
    username = input("Enter Your Username: ")
    
    if username in users:
        NewPass = input("Enter a Brand New Password Which You have Never Used Before: ")
        users[username] = caesar_cipher(NewPass, 6)
        save_users(users)
        print("✅ Password reset successful!")
    else:
        print("❌ Username not found!")

# Shift Value: 6