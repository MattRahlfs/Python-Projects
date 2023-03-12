
import random


Guess_number = random.randint(0, 10)
print (Guess_number)

def get_input():
    input_value = 0
    
    while True:
        try:
            input_value = int(input("Enter your choice. \n"))
            return input_value
            break            
        except ValueError:
            continue
        
        
def start():
    
    attempt_counter = 1

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
            
        
start()
    