from tabulate import tabulate
from pyfiglet import Figlet
import random
import cowsay
from colorama import Fore, Style, init

# initialize colorama
init(autoreset=True)

# create figlet object
figlet = Figlet()


class Board:
    def __init__(self):
        self.squares = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def __str__(self):
        return tabulate(self.squares, tablefmt="grid")

    def check_wins(self):
        square = self.squares
        for i in range(3):
            # check for column wins
            if square[0][i] == square[1][i] == square[2][i]:
                return square[0][i]

            # check for row wins
            if square[i][0] == square[i][1] == square[i][2]:
                return square[i][0]

        # check for diagonal wins
        if square[0][0] == square[1][1] == square[2][2]:
            return square[0][0]
        if square[0][2] == square[1][1] == square[2][0]:
            return square[0][2]

    def check_ties(self):
        for row in self.squares:
            # if there are numbers left - it is not a tie
            for square in row:
                if str(square).isnumeric():
                    return False
        return True

    @property
    def empty(self):
        _empty = []
        # any square that is a number is assumed empty
        for row in self.squares:
            for square in row:
                if str(square).isnumeric():
                    _empty.append(square)
        return _empty


# create a board object
board = Board()


def main():
    try_again = "y"
    # keep playing the game until user doesn't want to play anymore
    while try_again == "y":
        # initialize an empty board with each new game
        board.squares = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # get the game mode
        mode = start_game()
        last_move = "X"
        # keep making moves until there is a tie or a win
        while not board.check_ties() and not board.check_wins():
            print(board)
            # itetare moves based on who made the last move
            if last_move == "X":
                player_move("O")
                last_move = "O"
            else:
                # based on the mode, next move belongs either to next player or to computer
                if mode == "1":
                    computer_move()
                else:
                    player_move("X")
                last_move = "X"
        print(board)
        # announce the winner if there is one
        if winner := board.check_wins():
            cowsay.cow(f"\n{winner} WON THE GAME !!!\n")
        # declare a tie
        else:
            cowsay.cow("\nTHAT'S A TIE!!!\n")
        # prompt the user to play again until thay input 'y' or 'n'
        while True:
            answ = input(Fore.GREEN + "\nTRY AGAIN? [y/n]: ")
            print()
            if answ in ["y", "n"]:
                try_again = answ
                break


def start_game():
    # inform the user about the begining of a new game
    figlet.setFont(font="slant")
    print(figlet.renderText("Game started"))
    # prompt the user for a game mode until valid one is imported
    while True:
        mode = input(
            "PICK YOUR GAME MODE: [1] - you vs computer, [2] - two player mode: "
        )
        if check_mode(mode):
            return mode
        else:
            # remind the user of how to use the program
            print(Fore.RED + "\nUsage: type 1 or 2 to choose mode\n")


def check_mode(mode):
    return mode in ["1", "2"]


def player_move(player):
    # prompt the user for a move until they input a valid one
    while True:
        move = input(Fore.GREEN + f"\n'{player}' MAKES A MOVE: ")
        print()
        if valid_move(move, player):
            break
        else:
            print(Fore.RED + "\nInvalid move\n")


def valid_move(move, player):
    # check if move is an integer
    if move := check_int(move):
        for j, row in enumerate(board.squares):
            for i, square in enumerate(row):
                # check if move is a valid empty square on the board
                if move == square and move in board.empty:
                    # based on the player add symbol of a different color
                    if player == "X":
                        board.squares[j][i] = Fore.CYAN + player + Style.RESET_ALL
                    else:
                        board.squares[j][i] = Fore.YELLOW + player + Style.RESET_ALL
                    return True


def check_int(move):
    try:
        return int(move)
    except ValueError:
        return False


def computer_move():
    # randomly choose a square from the empty ones
    move = random.choice(board.empty)
    print(Fore.GREEN + f"\nCOMPUTER CHOSE {move}\n")
    valid_move(move, "X")


if __name__ == "__main__":
    main()
