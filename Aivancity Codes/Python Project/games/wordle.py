import random

# 1;32 HEX - Green 
# # 4;33 HEX - Yellow Underline 
# # 9;31 HEX - Red Strikethrough

words = [
    "FLAME", "BRAVE", "SLIDE", "CHAIR", "SWIFT", "GLASS", "MARCH", "STORM", "BREAD", "QUILT",
    "DREAM", "FLARE", "HAPPY", "TIGER", "CRANE", "LUNCH", "SOLID", "NOBLE", "FERRY", "VITAL",
    "BRICK", "SHARP", "CLOUD", "GRAVE", "PLANT", "CRISP", "TREND", "BLUSH", "FROST", "WHEEL"
]

class Wordle:
    def __init__(self):
        self.secret_word = random.choice(words)
        self.used_letters = set()
        self.correct_letters = {}
        self.misplaced_letters = set()

    def display_status(self, guesses, words_guessed):
        print("\n".join(f"YOUR WORD: {word}\n{' '.join(guess)}" for word, guess in zip(words_guessed, guesses)))
        print("_ _ _ _ _\n" * (6 - len(guesses)))
        print("Available Letters:")
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            if letter in self.correct_letters.values():
                print(f"\033[1;32m{letter}\033[0m", end=" ")  
            elif letter in self.misplaced_letters:
                print(f"\033[4;33m{letter}\033[0m", end=" ")  
            elif letter in self.used_letters:
                print(f"\033[9;31m{letter}\033[0m", end=" ")  
            else:
                print(letter, end=" ")
        print("\n")

    def get_feedback(self, guess):
        feedback = []
        temp_word = list(self.secret_word)
        for i, letter in enumerate(guess):
            if letter == self.secret_word[i]:
                feedback.append("🟩")
                self.correct_letters[i] = letter
            elif letter in self.secret_word and guess.count(letter) <= temp_word.count(letter):
                feedback.append("🟨")
                self.misplaced_letters.add(letter)
            else:
                feedback.append("🔲")
                self.used_letters.add(letter)
        return feedback

    def play(self):
        print("🎮 Welcome to Wordle! You have 6 attempts to guess the 5-letter word.")
        attempts, words_guessed = [], []
        while len(attempts) < 6:
            guess = input(f"Attempt {len(attempts)+1}/6: ").upper()
            if len(guess) != 5 or not guess.isalpha() or guess in words_guessed:
                print("❌ Invalid input! Enter a new 5-letter word.")
                continue
            
            feedback = self.get_feedback(guess)
            attempts.append(feedback)
            words_guessed.append(guess)
            self.display_status(attempts, words_guessed)
            
            if feedback == ["🟩"] * 5:
                print("🎉 You guessed the word! 🎉")
                break
        else:
            print(f"😞 Out of attempts! The correct word was: {self.secret_word}")

if __name__ == "__main__":
    game = Wordle()
    game.play()
