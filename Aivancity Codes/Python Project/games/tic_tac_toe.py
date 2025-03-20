class TicTacToe:
    """A simple Tic Tac Toe game using OOP principles."""

    def __init__(self):
        # Initialize a 3x3 board as a list of 9 spaces
        self.board = [" "] * 9
        # X always starts
        self.current_player = "X"

    def display_board(self):
        """Print the current game board in a 3x3 grid."""
        print("\n")
        for i in range(0, 9, 3):
            print(f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} ")
            if i < 6:
                print("---+---+---")
        print("\n")

    def make_move(self):
        """
        Ask the current player for a position (1-9).
        Update the board if valid; otherwise keep asking.
        """
        while True:
            try:
                choice = int(input(f"Player {self.current_player}, choose a square (1-9): "))
                index = choice - 1  # Convert human-friendly input (1-9) to list index (0-8)

                if 0 <= index < 9 and self.board[index] == " ":
                    self.board[index] = self.current_player
                    break
                else:
                    print("❌ Invalid move! That square is either out of range or already taken.")
            except ValueError:
                print("⚠️ Please enter a valid number (1-9).")

    def check_winner(self):
        """Return 'X' or 'O' if a winner is found, otherwise return None."""
        winning_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]
        for a, b, c in winning_positions:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        return None

    def check_tie(self):
        """Check if all squares are filled and there's no winner."""
        return " " not in self.board

    def switch_player(self):
        """Switch current player from X to O or O to X."""
        self.current_player = "O" if self.current_player == "X" else "X"

    def play(self):
        """Main game loop: display board, make a move, check status, switch player."""
        print("🎮 Welcome to Tic Tac Toe!")
        self.display_board()

        while True:
            self.make_move()
            self.display_board()

            winner = self.check_winner()
            if winner:
                print(f"🎉 Player {winner} wins! Congratulations! 🏆")
                break

            if self.check_tie():
                print("😲 It's a tie! No more squares left.")
                break

            self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()

