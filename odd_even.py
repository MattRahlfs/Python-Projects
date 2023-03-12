#detect if a user generated value is odd or even




while True:
    input_value=float(0)
    
    if input_value == 0:
        input_value= float(input("Enter a number\n"))
    
    if input_value % 2 == 0:
        print("this number is even")
        
        break
    else:
        print ("this number is odd")
        break
    
    