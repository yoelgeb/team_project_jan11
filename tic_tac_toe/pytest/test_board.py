import sys
sys.path.insert(0, "../lib")
from board import Board

def test_board():
  tic_tac_toe = Board()
  assert isinstance(tic_tac_toe, Board)