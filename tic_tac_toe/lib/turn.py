import player
import board

class Turn:
  def __init__(self, board, player1, player2) -> None:
    self.board = board
    self.player1 = player1
    self.player2 = player2

  def place_x(self, cell):
    if cell[0] == 'a':
      x = 'row2'
    elif cell[0] == 'b':
      x = 'row4'
    else:
      x = 'row6'
    if cell[1] == '1':
      y = 1
    elif cell[1] == '2':
      y = 3
    else:
      y = 5
    if self.move_is_valid(cell, x, y):
      self.board.board[x][y] = "X"
      return True
    else:
      raise Exception

  def place_o(self, cell):
    if cell[0] == 'a':
      x = 'row2'
    elif cell[0] == 'b':
      x = 'row4'
    else:
      x = 'row6'
    if cell[1] == '1':
      y = 1
    elif cell[1] == '2':
      y = 3
    else:
      y = 5
    if self.move_is_valid(cell, x, y):
      self.board.board[x][y] = "O"
      return True
    else:
      raise Exception

  def move_is_valid(self, cell, x, y):
    if (cell[0]in["a", "b", "c"]) and (cell[1]in["1", "2", "3"]):
      if self.board.board[x][y] == " ":
        return True
      else:
        return False
    else:
      return False

  def end_of_game(self, counter):
    if counter < 9:
      if (self.board.board['row2'][1] == "X") and (self.board.board['row4'][1] == "X") and (self.board.board['row6'][1] == "X"):
        return True
      elif (self.board.board['row2'][1] == "O") and (self.board.board['row4'][1] == "O") and (self.board.board['row6'][1] == "O"):
        return True
      elif (self.board.board['row2'][3] == "O") and (self.board.board['row4'][3] == "O") and (self.board.board['row6'][3] == "O"):
        return True
      elif (self.board.board['row2'][3] == "X") and (self.board.board['row4'][3] == "X") and (self.board.board['row6'][3] == "X"):
        return True
      elif (self.board.board['row2'][5] == "O") and (self.board.board['row4'][5] == "O") and (self.board.board['row6'][5] == "O"):
        return True
      elif (self.board.board['row2'][5] == "X") and (self.board.board['row4'][5] == "X") and (self.board.board['row6'][5] == "X"):
        return True
      elif (self.board.board['row2'][1] == "X") and (self.board.board['row2'][3] == "X") and (self.board.board['row2'][5] == "X"):
        return True
      elif (self.board.board['row2'][1] == "O") and (self.board.board['row2'][3] == "O") and (self.board.board['row2'][5] == "O"):
        return True
      elif (self.board.board['row4'][1] == "X") and (self.board.board['row4'][3] == "X") and (self.board.board['row4'][5] == "X"):
        return True
      elif (self.board.board['row4'][1] == "O") and (self.board.board['row4'][3] == "O") and (self.board.board['row4'][5] == "O"):
        return True
      elif (self.board.board['row6'][1] == "X") and (self.board.board['row6'][3] == "X") and (self.board.board['row6'][5] == "X"):
        return True
      elif (self.board.board['row6'][1] == "O") and (self.board.board['row6'][3] == "O") and (self.board.board['row6'][5] == "O"):
        return True
      elif (self.board.board['row2'][1] == "X") and (self.board.board['row4'][3] == "X") and (self.board.board['row6'][5] == "X"):
        return True
      elif (self.board.board['row2'][1] == "O") and (self.board.board['row4'][3] == "O") and (self.board.board['row6'][5] == "O"):
        return True
      elif (self.board.board['row2'][5] == "X") and (self.board.board['row4'][3] == "X") and (self.board.board['row6'][1] == "X"):
        return True
      elif (self.board.board['row2'][5] == "O") and (self.board.board['row4'][3] == "O") and (self.board.board['row6'][1] == "O"):
        return True
      else:
        return False
    else:
      return True
