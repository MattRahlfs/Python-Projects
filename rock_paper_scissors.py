import random

# choose a random number from 0 - 2

while True:
    RPS_number = random.randint(0, 2)

    # associate rock, paper, scissors with a number

    RPS_associations = {
        
        0: "Rock",
        
        1: "Paper",
        
        2: "Scissors"
        
        
    }


    input_value = str(input("\nEnter a choice Rock, Paper, Scissors\n"))


    if input_value == RPS_associations[RPS_number]:
        print("You both chose: " + input_value + " try again.")
        continue
    elif input_value == "Rock" and RPS_associations[RPS_number] == "Scissors":
        print ("\nYou win:  Rock smashes Scissors")
        break
    elif input_value == "Rock" and RPS_associations[RPS_number] == "Paper":
        print ("\nYou lose:  Paper covers Rock")
        break
    elif input_value == "Paper" and RPS_associations[RPS_number] == "Scissors":
        print ("\nYou lose:  Scissors cuts Paper")
        break
    elif input_value == "Paper" and RPS_associations[RPS_number] == "Rock":
        print ("\nYou win:  Paper covers Rock")
        break
    elif input_value == "Scissors" and RPS_associations[RPS_number] == "Rock":
        print ("\nYou lose, Rock Smashes Scissors")
        break
    elif input_value == "Scissors" and RPS_associations[RPS_number] == "Paper":
        print ("\nYou win, Scissors cuts Paper")
        break
    elif input_value != ("Rock", "Paper", "Scissors",):
        continue
    else:
        print (input_value, RPS_associations[RPS_number])
        