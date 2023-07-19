from tabulate import tabulate
from pyfiglet import Figlet
import sys

figlet = Figlet()
fonts = figlet.getFonts()

class Board:
    def __init__(self):
        self.squares = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    def __str__(self):
        return (tabulate(self.squares, tablefmt='grid'))


def main():
    mode = start_game()


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
    ...

def computer_move():
    ...

def check_wins():
    ...

def check_ties():
    ...

