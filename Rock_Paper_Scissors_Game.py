import random

def get_choices():
  player_choice = input("Enter a choice ( rock , paper , scissors) ")
  options = ["rock ", "paper" , "scissors"]
  computer_choice = random.choice(options)
  return {"player":player_choice,"computer":computer_choice}


def check_win(player,computer):
    print(f"you chose {player}, computer chose {computer}")
    if player == computer:
      return "its a Tie!"
    
    elif player == "rock" :
      if computer == "scissors":
        print("Rock smashes scissors ! You Win")
      else:
       print("Paper covers Rock ! You Lose")

    elif player == "paper" :
      if computer == "rock":
        print("Paper cover Rock ! You Win")
      else:
       print("Scissors cuts Paoper! You Lose")    
    elif player == "scissors" :
      if computer == "paper":
        print("Scissors cut paper ! You Win")
    else:
       print("Rock smashes Scissors! You Lose")    
   
       
choices = get_choices()
result = check_win(choices["player"],choices["computer"])
print(result)    

 

