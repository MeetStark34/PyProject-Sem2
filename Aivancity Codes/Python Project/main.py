from auth import login, register, reset_password
from utils.menu import game_menu
from games.tic_tac_toe import TicTacToe
from games.battleship import Battleship
from games.wordle import Wordle 

def main():
    while True:
        print("\n🔐 Welcome to the Login System")
        print("1️⃣  Login")
        print("2️⃣  Register")
        print("3️⃣  Reset Password")
        print("4️⃣  Exit")
        
        option = input("Enter Your Choice -> ")
        if option == "1":
            if login.authenticate():
                game_menu()
        elif option == "2":
            register.create_account()
        elif option == "3":
            reset_password.reset_user_password()
        elif option == "4":
            confirm_exit = input("Are You Sure You Want To Leave, \n p.s. You Might Win Another Game? Yes / No: ").strip().lower()
            if confirm_exit == "yes":
                print("👋 Merci, Au revoir, à Bientôt!")
                break
        else:
            print("❌ Invalid Choice. Please Try Again,"
            "I Know You Aren't Blind or Someone whithout the Knowledge of Number Keys: 1, 2, 3, 4")

if __name__ == "__main__":
    main()

#Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force