from games.tic_tac_toe import TicTacToe
from games.battleship import Battleship
from games.wordle import Wordle

def game_menu():
    while True:
        print("\n🎮 Game Menu:")
        print("1️⃣  Play Tic-Tac-Toe")
        print("2️⃣  Play Battleship")
        print("3️⃣  Play Wordle")
        print("4️⃣  Logout")
        
        choice = input("Entrez Votre Choix: ")
        if choice == "1":
            game = TicTacToe()
            game.play()
        elif choice == "2":
            game = Battleship()
            game.play()
        elif choice == "3":
            game = Wordle() 
            game.play()
        elif choice == "4":
            print("👋 Logging out...")
            break
        else:
            print("❌ Invalid choice. Please try again.")
