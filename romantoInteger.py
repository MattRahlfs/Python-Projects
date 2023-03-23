
def romanToInteger(inputString):
    
    romanNumerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000, 
    
}
    result = 0
    
    inputString = inputString.replace('IV', 'III')
    inputString = inputString.replace('IX', 'VIIII')
    inputString = inputString.replace('XL', 'XXXX')
    inputString = inputString.replace('XC', 'LXXXX')
    inputString = inputString.replace('CD', 'CCCC')
    inputString = inputString.replace('CM', 'DCCCC')
        
    for letter in list(inputString):
        
        result += romanNumerals[letter]
    
    return result



print(romanToInteger('MCMXCIV'))