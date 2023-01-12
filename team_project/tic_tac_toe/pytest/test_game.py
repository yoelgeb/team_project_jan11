import sys
sys.path.insert(0, "../lib")
from turn import Turn
from player import Player
from board import Board
from game import Game

player1 = Player("Yoel")
player2 = Player("Supriya")
board = Board()
turn = (board, player1, player2)
game = Game(turn)