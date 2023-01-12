import random
class RockPaperScissor:
    def __init__(self) -> None:
        pass
   
    def startgame(self):
       x=0 
       y=0
       z=0
       while True:
        try:
         play1 = str(input("Enter Rock, Paper, Scissor: ")).lower()
         if   play1.lower() == "rock" or play1.lower() == "paper" or play1.lower() == "scissor":
              play2 = random.randint(1,3)
         else: 
            raise Exception
         if   play2 == 1:
              play2 = "rock"
         elif play2 == 2:
              play2 ="paper" 
         elif play2 == 3:
              play2 = "scissor"
         print("You choose: " +play1)    
         print("Computer choose: " +play2)
         if  play1 == play2:
            print("Its Tie")
            z += 1
         elif play1 == "rock" and play2 =="scissor":
            print("You win, Computer lose")
            x += 1
         elif play1 == "paper" and play2 =="rock":
            print("You win, Computer lose")
            x += 1
         elif play1 == "scissor" and play2 == "paper":
           print("You win, Computer lose")
           x += 1
         else:   
           print("You lose, Computer win")
           y += 1
        except:
          print("Please select  between rock,  paper or scissors")
        else:
         play_again = input("Do  you want Play again : yes/no: ").lower()
         if play_again == "no":
          print("Thanks for playing!!") 
          break 
         
       with open("rpc_result.txt","at") as text_file:
            text_file.write(f"player1 won the game {x} times and player2/computer won {y}  game tied {z} times \n")
