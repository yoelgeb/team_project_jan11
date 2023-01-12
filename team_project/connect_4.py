import sys
import tkinter as tk
import random
import datetime
from c4_board import *


class Connect4:
    output = tk.Label()
    c4_board = C4Board(output)

    game_over = [False, 0]
    turn = 0

    def __init__(self):
        self.output.pack()

    def __str__(self) -> str:
        temp = "\n"
        temp += "1 2 3 4 5 6 7\n"
        temp  += "--------------\n"
        for r in range(self.c4_board.ROW_NUM):
            for c in range(self.c4_board.COL_NUM):
                temp += f"{self.c4_board.game_board[r][c]}" + " "
            temp += "\n"
        return temp

    def start_game(self):
        self.output.config(text=self.__str__(), font=('Aerial 18'), height= 10, width=20)
        player_type = input("Would you like to play with a second player or computer? (c or p) ")
        while self.game_over[0] == False:
            if self.turn % 2 == 0:
                while True:
                    try:
                        drop = int(input("Player 1, make a drop choice (Choose Colunm: 1 - 7) "))
                        if (drop < 1 or drop > 7):
                            raise ValueError
                        self.game_over = self.c4_board.place_piece(drop - 1, 1)
                        self.output["text"] = self.__str__()
                    except ValueError:
                        print("Make a valid choice")
                    else:
                        self.turn += 1
                        break
            elif self.turn % 2 == 1:
                while True:
                    try:
                        if (player_type == 'p'):
                            drop = int(input("Player 2, make a drop choice (Choose Colunm: 1 - 7) "))
                            if (drop < 1 or drop > 7):
                                raise ValueError
                            self.game_over = self.c4_board.place_piece(drop - 1, 2)
                            self.output["text"] = self.__str__()
                        else:
                            random_num = random.randint(1, 7)
                            print(f"Computer chose position {random_num}")
                            self.game_over = self.c4_board.place_piece(random_num - 1, 'c')
                            self.output["text"] = self.__str__()
                    except ValueError:
                        print("Make a valid choice")
                    else:
                        self.turn += 1
                        break
        game_complete = datetime.datetime.now().strftime("%b %d, %I:%M%p")
        with open("connect4_results.txt", "at") as file:
            file.write(f"Winner of {game_complete} Connect4 game was Player {self.game_over[1]}." + 
                f" It took them {self.turn} turns.\n")
        input("Any key to exit.")
        
