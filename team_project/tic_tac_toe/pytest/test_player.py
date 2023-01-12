import sys
sys.path.insert(0, "../lib")
from player import Player

def test_player_exists():
  player1 = Player("Yoel")
  assert isinstance(player1, Player)

def test_player_has_name():
  player1 = Player("Yoel")
  assert player1.name == "Yoel"