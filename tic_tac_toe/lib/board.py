class Board:
  def __init__(self) -> None:
    self.board = {"row1": [" ","1", " ", "2", " ", "3"],
            "row2": ["a", " ", "|", " ", "|", " "],
            "row3": [" ", "-", "-", "-", "-", "-"],
            "row4": ["b", " ", "|", " ", "|", " "],
            "row5": [" ", "-", "-", "-", "-", "-"],
            "row6": ["c", " ", "|", " ", "|", " "],
            }
  
  def make_board(self):
    print(" ".join(self.board['row1']))
    print(" ".join(self.board['row2']))
    print(" ".join(self.board['row3']))
    print(" ".join(self.board['row4']))
    print(" ".join(self.board['row5']))
    print(" ".join(self.board['row6']))