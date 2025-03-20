# 🎮 Python Game Suite

Welcome to the Python Game Suite! This project includes a collection of classic games implemented in Python, along with a simple authentication system.

## 📋 Table of Contents

- [Games](#games)
  - [Tic-Tac-Toe](#tic-tac-toe)
  - [Battleship](#battleship)
  - [Wordle](#wordle)
- [Authentication](#authentication)
  - [Login](#login)
  - [Register](#register)
  - [Reset Password](#reset-password)
- [Usage](#usage)

## 📂 Folder Structure

The project directory structure is as follows:

```
Python Project/
├── auth/
│   ├── __init__.py
│   ├── login.py
│   ├── register.py
│   └── reset_password.py
├── games/
│   ├── __init__.py
│   ├── tic_tac_toe.py
│   ├── battleship.py
│   └── wordle.py
├── utils/
│   ├── __init__.py
│   └── menu.py
├── main.py
└── README.md
```

- `auth/`: Contains modules related to authentication, such as login, register, and reset password functionalities.
- `games/`: Contains modules for different games, such as Tic-Tac-Toe, Battleship, and Wordle.
- `utils/`: Contains utility modules, such as the menu module.
- `main.py`: The main script that runs the application.
- `README.md`: The README file with project information and instructions.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code follows the project's coding standards and includes appropriate tests.

## 🎲 Games

### 🕹️ Tic-Tac-Toe

A simple Tic-Tac-Toe game using OOP principles. Players take turns to place their marks (X or O) on a 3x3 grid. The first player to align three marks horizontally, vertically, or diagonally wins.

### 🚢 Battleship

A 3x3 Battleship game where players place their ships and take turns to attack each other's ships. The first player to sink both of the opponent's ships wins.

### 🔤 Wordle

A word-guessing game where players have six attempts to guess a secret 5-letter word. Feedback is provided for each guess to indicate correct, misplaced, and incorrect letters.

## 🔐 Authentication

### 🔑 Login

Users can log in with their username and password. Passwords are encrypted using a Caesar cipher with a shift value of 6.

### 📝 Register

New users can create an account by choosing a unique username and password. The password is encrypted using a Caesar cipher with a shift value of 6.

### 🔄 Reset Password

Users can reset their password by providing their username and a new password. The new password is encrypted using a Caesar cipher with a shift value of 6.

## 🚀 Usage

1. Clone the repository:
    ```sh
    git clone https://github.com/MeetStark34/PyProject-Sem2
    cd PyProject-Sem2
    ```

2. Run the main script:
    ```sh
    python main.py
    ```

3. Follow the on-screen instructions to log in, register, or reset your password. Once authenticated, you can choose to play any of the available games.
