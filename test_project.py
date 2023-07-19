from project import Board, check_mode, valid_move, check_int

def test_board_default():
    board = Board()
    assert board.squares == [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    assert board.empty == [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert board.check_wins() == None
    assert board.check_ties() == False

def test_wins():
    board = Board()
    board.squares = [['X','X','X'],[4, 5, 6],[7, 8, 9]]
    assert board.check_wins() == 'X'
    board.squares = [[1,2,'X'],[4, 5, 'X'],[7, 8, 'X']]
    assert board.check_wins() == 'X'
    board.squares = [[1,2,'O'],[4, 'O', 6],['O', 8, 9]]
    assert board.check_wins() == 'O'

def test_ties():
    board = Board()
    board.squares = [['X', 'O', 'X'],['O', 'X', 'O'],['O', 'X', 'O']]
    assert board.check_ties() == True

def test_mode():
    assert check_mode('1') == True
    assert check_mode('3') == False
    assert check_mode('cat') == False


def test_move():
    assert valid_move('1', 'O') == True
    assert valid_move('1', 'X') == None
    assert valid_move('cat', 'X') == None
    assert valid_move('10', 'X') == None

def test_check_int():
    assert check_int('cat') == False
    assert check_int('1') == 1