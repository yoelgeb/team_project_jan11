import sys
sys.path.insert(0, "./tic_tac_toe/lib")
sys.path.insert(0, "./connect_4")
sys.path.insert(0, "./rock_paper_scissor")
import connect_4
import game
import RockPaperSccissor

ttt = game.Game()
c4 = connect_4.Connect4()
rps = RockPaperSccissor.RockPaperScissor()

def main():
    while True:
        try:
            choice = int(input("\n\t1. Rock Paper Scissors\n\t2. Tic-Tac-Toe\n\t3. Connect 4\n\t4. Exit\n\nPick which game you'd like to play (input number): "))
        except:
            print("You did not make a correct choice")
        else:
            
            if choice == 1:
                rps.startgame()
            elif choice == 2:
                ttt.main_menu()
            elif choice == 3:
                c4.start_game()
            elif choice == 4:
                sys.exit()
            # start_over = input("Would you like to play a different game (n to exit)? ").lower()
            # if start_over[0] == 'n':
            #     break


if __name__ == "__main__":
    main()