class Board:
  def __init__(self) -> None:
    self.board = {"row1": [" ","a", " ", "b", " ", "c"],
            "row2": ["1", " ", "|", " ", "|", " "],
            "row3": [" ", "-", "-", "-", "-", "-"],
            "row4": ["2", " ", "|", " ", "|", " "],
            "row5": [" ", "-", "-", "-", "-", "-"],
            "row6": ["3", " ", "|", " ", "|", " "],
            }
  
  def make_board(self):
    print(" ".join(self.board['row1']))
    print(" ".join(self.board['row2']))
    print(" ".join(self.board['row3']))
    print(" ".join(self.board['row4']))
    print(" ".join(self.board['row5']))
    print(" ".join(self.board['row6']))

# board = Board()

# import pdb; pdb.set_trace()

# board.make_board()