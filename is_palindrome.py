

def detect_palindrome(input_value):
    rev_input_value = list(reversed(input_value))
    
    if input_value == rev_input_value:
        return True
    else:
        return False
    
    
    
    
    
 
 
input_value = list(input("Enter a string and I will tell you if it is a palindrome.\n"))


if detect_palindrome(input_value) == True:
    print ("This string is a palindrome.")
else:
    print("This string is not a palindrome.")