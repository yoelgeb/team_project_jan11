import sys
sys.path.append("../lib")
import board

def test_board():
  board = board.Board
  assert isinstance(board, board.Board)