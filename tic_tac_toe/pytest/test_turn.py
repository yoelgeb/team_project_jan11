import sys
sys.path.insert(0, "../lib")
from turn import Turn
from player import Player
from board import Board

def test_turn_exists():
  board = Board()
  joseph = Player("Joseph")
  supriya = Player("Supriya")
  turn = Turn(board, joseph, supriya)
  assert isinstance(turn, Turn)

def test_players():
  board = Board()
  joseph = Player("Joseph")
  supriya = Player("Supriya")
  turn = Turn(board, joseph, supriya)
  assert turn.player1.name == "Joseph"
  assert turn.player2.name == "Supriya"
  
def test_place_x():
  cell = 'b2'
  board = Board()
  joseph = Player("Joseph")
  supriya = Player("Supriya")
  turn = Turn(board, joseph, supriya)
  turn.place_x(cell)
  assert board.board['row4'][3] == "X"

def test_place_o():
  cell = 'b2'
  board = Board()
  joseph = Player("Joseph")
  supriya = Player("Supriya")
  turn = Turn(board, joseph, supriya)
  turn.place_o(cell)
  assert board.board['row4'][3] == "O"

def test_move_is_valid_true():
  cell = 'b2'
  board = Board()
  joseph = Player("Joseph")
  supriya = Player("Supriya")
  turn = Turn(board, joseph, supriya)
  assert turn.move_is_valid(cell, 'row4', 3) == True

def test_move_is_valid_false():
  board = Board()
  joseph = Player("Joseph")
  supriya = Player("Supriya")
  turn = Turn(board, joseph, supriya)
  turn.place_o('b2')
  assert turn.move_is_valid('b2', 'row4', 3) == False
  assert turn.move_is_valid('r3', "", "") == False

def test_end_of_game_vertical():
  board = Board()
  joseph = Player("Joseph")
  supriya = Player("Supriya")
  turn = Turn(board, joseph, supriya)
  turn.place_o('b2')
  turn.place_o('b1')
  turn.place_o('b3')
  assert turn.end_of_game == True