import time

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
 

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


    


####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
  
  

class adventurer():
    def __init__(self, name, weight, height, race, typeofclass):
        self.name = name
        self.weight = weight
        self.height = height
        self.race = race
        self.typeofclass = typeofclass
        self.inventory = []
        self.stats = {
            'Health': 0,
            'Strength': 0,
            'Wisdom': 0
                      }
    
    def get_inventory(self):
        return self.inventory
    
    def add_to_inventory(self, item):
        self.inventory.extend(item)
        
    def remove_from_inventory(self, item):
        self.inventory.remove(item)
        
    def add_stat(self, stat, value):
        self.stats[stat] += value
        
    def remove_stat(self, stat, value):
        self.stats[stat] -= value
    
    def get_stats(self):
        return self.stats
    
    
class enemy():
    def __init__(self, name, attacktype, health):
        self.name = name
        self.attacktype = attacktype
        self.health = health
        
    

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
 

    
    
    
slow_print(0,["Welcome to  --- GAME ---."])    
slow_print(.8,["Lets create your character... "])


name = str(typingInput('What do you want to be named?\n'))
weight = float(typingInput('What is your weight in pounds?\n'))
height = float(typingInput('How tall are you in feet?\n'))
race = str(typingInput('What is your race? (Human, Elf, Dwarf, Orc)\n'))
typeofclass = str(typingInput('What class do you want to be? (Warrior, Priest, Rogue)\n'))

character = adventurer(name, weight, height, race, typeofclass)



if character.typeofclass.lower() == 'priest':
    character.add_stat('Health', 10)
    character.add_stat('Strength', 3)
    character.add_stat('Wisdom', 15)
    

print(character.get_stats())


