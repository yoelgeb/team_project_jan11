
class C4Board:
    ROW_NUM = 6
    COL_NUM = 7

    def __init__(self, output):
        temp = []
        for r in range(self.ROW_NUM):
            temp.append([0, 0, 0, 0, 0, 0, 0])
        self.game_board = temp
        self.output = output

    def place_piece(self, col, player):
        if self.game_board[0][col] != 0:
            print("Bad Placement! Next Player")
            return [False]
        for x in range(self.ROW_NUM):
            if self.game_board[x][col] != 0:
                self.game_board[x - 1][col] = player
                return self.__check_win(x - 1, col, player)
        self.game_board[x][col] = player
        return self.__check_win(x, col, player)


    def __check_win(self, row, col, player):
        if (self.__check_horizontal(row, col, player) or 
        self.__check_vertical(row, col, player)):
            if (player != 'c'):
                print(f"Player {player} Wins!")
            else:
                print("Computer Wins!")
            self.output.config(background="gold")
            return [True, player]
        return [False, 0]
    
    def __check_vertical(self, row, col, player):
        if row < 3:
            if (self.game_board[row + 1][col] == player and 
            self.game_board[row + 2][col] == player and 
            self.game_board[row + 3][col] == player):
                return True
        elif row > 2:
            if (self.game_board[row - 1][col] == player and 
            self.game_board[row - 2][col] == player and 
            self.game_board[row - 3][col] == player):
                return True
        return False
    
    def __check_horizontal(self, row, col, player):
        if col < 4:
            if (self.game_board[row][col + 1] == player and 
            self.game_board[row][col + 2] == player and 
            self.game_board[row][col + 3] == player):
                return True

        if col > 2:
            if (self.game_board[row][col - 1] == player and 
            self.game_board[row][col - 2] == player and 
            self.game_board[row][col - 3] == player):
                return True
        return False
    
    def __check_diag(self, row, col, player):
        if col < 4 and row < 4:
            if (self.game_board[row + 1][col + 1] == player and
            self.game_board[row + 2][col + 2] == player and
            self.game_board[row + 3][col + 3] == player):
                return True
        

