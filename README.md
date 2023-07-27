# Colorful Tic Tac Toe Game
## Video Demo: https://www.youtube.com/watch?v=Agwv14lih04
![Screenshot (9)](https://github.com/JuliaMaxy/tic_tac_toe/assets/121096183/a6a16951-8341-4004-a6a6-6a388a89c277)
### Description
A command-line Tic Tac Toe game written exclusively in Python.
### Why Tic Tac Toe?
It seemed like a relatively challenging task with a lot of logic involved and was pretty straightforward in its command line usage.
### How does it work?
- After you run `python3 project.py`, you are prompted to choose a game mode.
- Mode 1 is Player vs Computer.
- Mode 2 is Player vs Other Player.
- The game happens on a 3x3 board, where each square is initially numbered.
- Players take turns inputting their moves.
- A player (or computer) wins if an entire row, column, or diagonal is filled with their symbol (X or O).
- A tie is declared if there are no legal moves available.
- After the game ends, the user is offered to play another one.
## Files
- `project.py`: contains all code needed to execute this program:
    - creates a `Board` class which contains all the related board  functionality.
    - `main`: starts the game in a chosen mode, randomly chooses who gets to play first, after which it goes back and forth between players until the game ends. At the end of the game, a cow from the cowsay module declares a winner or a tie.
    - `start_game`:prints a fancy-looking message using pyfiglet and gets a valid game mode from the user.
    - `check_mode`: is a helper function to `start_game`.
    - player_move: gets a move from the user and validates it with the help of the `valid_move` function.
    - `valid_move`:  checks if a move is a valid number on the board; if so - adds that move to the board with the right symbol color.
    - `computer_move`: randomly chooses an empty square on the board.
- `test_project.py`: functions needed to test `project.py` using pytest.
