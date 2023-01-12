# create turn with number of players
# place x or o
# valid move?
# check to see if ttt or draw
# switch to next player
# place x or o
# valid move?
# check to see if ttt or draw
# repeat

import player
import board

class Turn:
  def __init__(self, board, player1, player2) -> None:
    self.board = board
    self.player1 = player1
    self.player2 = player2

  def place_x(self, cell):
    if cell[0] == 'a':
      y = 1
    elif cell[0] == 'b':
      y = 3
    else:
      y = 5
    if cell[1] == '1':
      x = 'row2'
    elif cell[1] == '2':
      x = 'row4'
    else:
      x = 'row6'
    self.board.board[x][y] = "X"

  def place_o(self, cell):
    if cell[0] == 'a':
      y = 1
    elif cell[0] == 'b':
      y = 3
    elif cell[0] == 'c':
      y = 5
    else:
      y = ""
    if cell[1] == '1':
      x = 'row2'
    elif cell[1] == '2':
      x = 'row4'
    elif cell[1] == '3':
      x = 'row6'
    else:
      x = ""
    if self.move_is_valid(cell, x, y):
      self.board.board[x][y] = "O"

  def move_is_valid(self, cell, x, y):
    if (cell[0]in["a", "b", "c"]) and (cell[1]in["1", "2", "3"]):
      if self.board.board[x][y] == " ":
        return True
      else:
        return False
    else:
      return False
