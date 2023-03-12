#detect if a user generated value is odd or even

# create a loop to ask for input

while True:
# create a function to detect if the passsed variable is odd or even and output the answer
    def is_even(input_value):
        if input_value % 2 == 0:
            print ("The input is even.")
            return True
        else:
            print ("The input is odd.")
            return False
    
#get input from user
    def get_input():
        
        input_value = 0
        try:
            input_value = int(input("Enter a real number to detect if it is even or odd.\n"))
            
        except ValueError:
            get_input()
        
        return input_value
            
        
        
    is_even(get_input())
    
#do you want to go again? break the loop
    end_game = input(str("Do you want to play again y/n."))
    if end_game == "y":
        continue
    else:
        break
    
print("Thanks for playing")