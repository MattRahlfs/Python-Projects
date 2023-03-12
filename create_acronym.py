import re

input_value = str(input("Enter a series of words to get an acronym\n"))

def get_fletter(input_value):
    
    # split words by spaces
    input_value = re.sub('[^a-zA-Z ]', '', input_value)
    input_value =  input_value.split(" ")
    input_value = [x for x in input_value if x != '']
    
    final_list = []
    for x in input_value:
        
        final_list.append(x[0])
    
    result = ''.join(final_list)    
    print (result.upper())
    

get_fletter(input_value)
