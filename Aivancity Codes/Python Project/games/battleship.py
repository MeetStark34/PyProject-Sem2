class Board:
    """Class to represent a player's board and attacks."""
    
    def __init__(self):
        self.ships = set()
        self.attacks = [" "] * 9

    def display(self) -> None:
        """Display the board."""
        for i in range(3):
            print(f" {self.attacks[i * 3]} | {self.attacks[i * 3 + 1]} | {self.attacks[i * 3 + 2]} ")
            if i < 2:
                print("---+---+---")


class Battleship:
    """3x3 Battleship game with correct board display and attack mechanics."""

    def __init__(self):
        self.grid_size = 3
        self.player1_board = Board()
        self.player2_board = Board()
        self.current_player = 1

    def display_board(self) -> None:
        """Display the combined board showing attacks correctly."""
        print("\nCurrent Board:")

        # Player 1's attacks
        self.player1_board.display()

        print("===========")  # Separator

        # Player 2's attacks
        self.player2_board.display()

        print("\n")

    def display_single_board(self, board: list[str]) -> None:
        """Display a single 3x3 board."""
        for i in range(3):
            print(f" {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} ")
            if i < 2:
                print("---+---+---")

    def place_ships(self, player: int) -> None:
        """Handles ship placement while displaying the board after each placement."""
        board = self.player1_board if player == 1 else self.player2_board
        temp_board = [" "] * 9

        print(f"\n🚢 Player {player}, place your 2 ships (1-9)")
        self.display_single_board(temp_board)

        while len(board.ships) < 2:
            try:
                pos = int(input(f"Enter ship {len(board.ships) + 1}: ")) - 1
                if 0 <= pos < 9 and pos not in board.ships:
                    board.ships.add(pos)
                    temp_board[pos] = "▮"
                    self.display_single_board(temp_board)
                else:
                    print("❌ Invalid position! Try again.")
            except ValueError:
                print("⚠️ Please enter a number between 1-9.")

    def attack_phase(self, attacker: int, defender_board: Board) -> None:
        """Handles attacking logic and updates the attack board."""
        attacker_board = self.player1_board if attacker == 1 else self.player2_board
        while True:
            try:
                pos = int(input(f"Player {attacker} attack (1-9): ")) - 1
                if 0 <= pos < 9:
                    if pos in defender_board.ships:
                        print("💥 Ship Sunk!")
                        attacker_board.attacks[pos] = "💥"
                        defender_board.ships.remove(pos)
                    else:
                        print("❌ Missed!")
                        attacker_board.attacks[pos] = "❌"
                    break
                else:
                    print("❌ Invalid position! Try again.")
            except ValueError:
                print("⚠️ Please enter a number between 1-9.")

    def play(self) -> None:
        """Main game loop handling player turns and attack phases."""
        print("🎮 BATTLESHIP - Place 2 ships each then attack!")

        # Ship placement
        self.place_ships(1)
        self.place_ships(2)

        # Battle phase
        while self.player1_board.ships and self.player2_board.ships:
            print(f"\n🌟 Player {self.current_player}'s Turn")

            if self.current_player == 1:
                self.attack_phase(1, self.player2_board)
            else:
                self.attack_phase(2, self.player1_board)

            self.display_board()
            
            if not self.player2_board.ships:
                print("🏆 Player 1 Wins!")
                break
            if not self.player1_board.ships:
                print("🏆 Player 2 Wins!")
                break

            self.current_player = 2 if self.current_player == 1 else 1


if __name__ == "__main__":
    game = Battleship()
    game.play()
