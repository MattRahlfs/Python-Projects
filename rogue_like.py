import time


class adventurer():
    def __init__(self, name, weight, height, race, typeofclass):
        self.name = name
        self.weight = weight
        self.height = height
        self.race = race
        self.typeofclass = typeofclass
    
    


def slow_print(sleep_time, string_to_print):
    time.sleep(sleep_time)
    for string in string_to_print:
        print (string)
        
def typingPrint(text):
  for character in text:
    print(character, end='')
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    print(character, end='')
    time.sleep(0.05)
  value = input()  
  return value  
  

    
    
    
slow_print(0,["Welcome to  --- GAME ---."])    
slow_print(.8,["Lets create your character... "])

name = str(typingInput('What do you want to be named?\n'))
weight = float(typingInput('What is your weight in pounds?\n'))
height = float(typingInput('How tall are you in feet?\n'))
race = str(typingInput('What is your race? (Human, Elf, Dwarf, Orc)\n'))
typeofclass = str(typingInput('What class do you want to be? (Warrior, Priest, Rogue)\n'))

character = adventurer(name, weight, height, race, typeofclass)

print(character.name, character.race, character.typeofclass)
