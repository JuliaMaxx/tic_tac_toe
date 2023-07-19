from tabulate import tabulate
from pyfiglet import Figlet
import sys

figlet = Figlet()
fonts = figlet.getFonts()


class Board:
    def __init__(self):
        self.squares = [
            [1, 2, 3],
            [4, 5, 6], 
            [7, 8, 9]
            ]
    def __str__(self):
        return (tabulate(self.squares, tablefmt='grid'))
    
    def check_wins(self):
        square = self.squares
        for i in range(3):
            # check columns
            if square[0][i] == square[1][i] == square[2][i]:
                return square[0][i]
            # check rows
            if square[i][0] == square[i][1] == square[i][2]:
                return square[i][0]
        # check diagonals
        if square[0][0] == square[1][1] == square[2][2]:
            return square[0][0]
        if square[0][2] == square[1][1] == square[2][0]:
            return square[0][2]
        
    def check_ties(self):
        for row in self.squares:
            # if there are any numbers left - it is not a tie 
            for square in row:
                if str(square).isnumeric():
                    return False
        return True
    
    @property
    def empty(self):
        _empty = []
        for row in self.squares:
            for square in row:
                if str(square).isnumeric():
                    _empty.append(square)
        return _empty
    
                
board = Board()

def main():
    mode = start_game()
    if mode == '1':
        while not board.check_ties() and not board.check_wins():
            print(board)
            player_move()   
        
        print('tie/win')


def start_game():
    # inform the user about the begining of a new game
    figlet.setFont(font='slant')
    print(figlet.renderText('Game started'))
    # prompt the user for a game mode until valid one is imported
    while True:
        mode = input('PICK YOUR GAME MODE: [1] - you vs computer, [2] - two player mode: ')
        if mode in ['1', '2']:
            return mode
        else:
            # remind the user of how to use the program
            print('\nUsage: type 1 or 2 to choose mode')

def player_move():
    global board
    while True:
        move = input("MAKE A MOVE: ")
        if valid_move(move):
            break
        else:
            print('\nInvalid move\n')
        

def valid_move(move):
    try:
        for j, row in enumerate(board.squares):
                for i, square in enumerate(row):
                    if int(move) == square and int(move) in board.empty:
                        board.squares[j][i] = 'O'
                        return True
    except ValueError:
        return False

def computer_move():
    ...


if __name__ == '__main__':
    main()