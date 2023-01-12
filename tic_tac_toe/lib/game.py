import turn
import player
import board
import random

class Game:
  
  def main_menu(self):
    print("")
    print("-" * 8 + "Main Menu" + "-" * 8)
    print("")
    print("Welcome to Tic Tac Toe!")
    print("Enter 'p' to play. Enter 'q' to quit.")
    print("")
    menu_selection = input("> ").lower()

    while (menu_selection != 'p') and (menu_selection != 'q'):
      print("")
      print("Invalid selection. Enter p or q!")
      menu_selection = input("> ").lower()
      # import pdb; pdb.set_trace()

    if menu_selection == 'p':
      print("")
      print("Enter '1' for 1 player. Enter '2' for 2 players.")
      print("")
      play = input("> ")

      while (play != '1') and (play != '2'):
        print("")
        print("Invalid selection. Enter 1 or 2!")
        print("")
        play = input("> ")
      
      if play == '1':
        self.start_p1_vs_cpu()
      else:
        self.start_p1_vs_p2()

    elif menu_selection == 'q':
      print("")
      print("See you later!")

  def start_p1_vs_cpu(self):
    the_board = board.Board()
    print("")
    p1_name = input("Please enter your name: ")
    player1 = player.Player(p1_name)
    turns = turn.Turn(the_board, player1, player.Player("cpu"))
    print("")
    the_board.make_board()
    print("")
    counter = 0
    while True:
      move = input("Enter your move: ")
      while True:
        if turns.place_x(move):
          counter += 1
          break
        else:
          move = input("Please select again: ")
      if turns.end_of_game(counter):
        break
      print("")
      the_board.make_board()
      print("")
      while True:
        cpu_move = random.sample(['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3'], 1)[0]
        # import pdb; pdb.set_trace()
        if turns.place_o(cpu_move):
          counter += 1
          break
      if turns.end_of_game(counter):
        break
      print("")
      the_board.make_board()
      print("")
    self.game_over(counter, "pvc", player1.name, None, the_board)

  def start_p1_vs_p2(self):
    the_board = board.Board()
    print("")
    p1_name = input("Player 1 enter your name: ")
    player1 = player.Player(p1_name)
    print("")
    p2_name = input("Player 2 enter your name: ")
    player2 = player.Player(p2_name)
    turns = turn.Turn(the_board, player1, player.Player("cpu"))
    print("")
    the_board.make_board()
    print("")
    counter = 0
    while True:
      move = input(f"{player1.name}, enter your move: ")
      while True:
        if turns.place_x(move):
          counter += 1
          break
        else:
          move = input("Please select again: ")
      if turns.end_of_game(counter):
        break
      print("")
      the_board.make_board()
      print("")
      p2_move = input(f"{player2.name}, enter your move: ")
      while True:
        if turns.place_o(p2_move):
          counter += 1
          break
        else:
          p2_move = input("Please select again: ")
      if turns.end_of_game(counter):
        break
      the_board.make_board()
      print("")
    print("")
    the_board.make_board()
    print("")
    self.game_over(counter, "pvp", player1.name, player2.name, the_board)

  def game_over(self, counter, type, p1_name, p2_name, the_board):
    print("")
    the_board.make_board()
    print("")
    if counter == 9:
      print("Draw!!")
      x = "Draw"
    elif (counter % 2 == 0) and (type == "pvc"):
      print("I win!")
      x = "Computer win"
    elif (counter % 2 == 0) and (type == "pvp"):
      print(f"{p2_name} wins!!")
      x = "Player 2 win"
    else:
      print(f"{p1_name} wins!!")
      x = "Player 1 win"
    with open("winners.csv", "at") as file:
      file.write(f"{x}, {counter} moves\n")
    self.main_menu()



