import re


def count_words(input_value):
    
    input_value = re.sub('[^a-zA-Z ]', '', input_value)
    input_value =  input_value.split(" ")
    input_value = [x for x in input_value if x != '']
    print ('The word count for that sentance is ' + str(len(input_value)))
    

input_value  = input(str("Enter a sentance to get a word count.\n"))


count_words(input_value)













