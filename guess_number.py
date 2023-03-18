
import random


Guess_number = random.randint(0, 10)
#print (Guess_number)

def get_input():
    input_value = 0
    
    while True:
        try:
            input_value = int(input("Enter your choice. \n"))
            return input_value
            break            
        except ValueError:
            continue
        
        
def start(userorcomputer):
    
    attempt_counter = 1
    if userorcomputer == 0:
        while True:
            input_value = get_input()
            
            if input_value == Guess_number:
                print ("You win and it only took: " + str(attempt_counter) + " attempts to get it right!")
                break
            elif input_value != Guess_number:
                attempt_counter +=1
                
                if str(input("That is not correct, do you want to keep trying? y/n \n")) == 'y':
                    continue
                else:
                    break
    elif userorcomputer == 1:
        valtoguess =  int(input('Enter the number you want to computer to guess (it must be between 0 an 10) '))
        computerguess = 0
        while computerguess != valtoguess:
            
            if computerguess != valtoguess:
                computerguess = random.randint(0,10)
                attempt_counter +=1
                print('The computer guess is ' + str(computerguess))
            
        print('It took the Computer ' + str(attempt_counter) + ' tries to get the correct number')
    else:
        return None
            
userorcomputer = int(input("Press 0 if you want to guess the number, or press 1 to have the computers guess your number "))     
       

start(userorcomputer)

