import time
import random

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

def mineOre(player, typeOfOre):
    requiredLeveltoMineOre = {
        'tin': 1,
        'copper': 5,
        'iron': 10,
        'coal': 15
        
    }
    
    playerMiningLevel = player.stats['Mining']
    
    if playerMiningLevel < requiredLeveltoMineOre[typeOfOre.lower()]:
        print ('You do not meet the level requirment.')
    else:
        counter = 4
        print ('You attempt to mine the ore...')
        while counter >= 0:
            sucessfulMine = random.randint(0, 4)
            if sucessfulMine == 1:
                player.add_to_inventory(typeOfOre)
                print ('You successfully mine the ore')
                player.add_stat('Mining', 1)
                break
            elif counter == 0 and sucessfulMine != 1:
                print ('You failed to mine the ore.')
                
            counter -= 1
        
        
    
    
    


    


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
            'Wisdom': 0,
            'Defence': 0,
            'Mining': 0
                      }
    
    def get_inventory(self):
        return self.inventory
    
    def add_to_inventory(self, item):
        self.inventory.append(item)
        
    def remove_from_inventory(self, item):
        self.inventory.remove(item)
        
    def add_stat(self, stat, value):
        self.stats[stat] += value
        
    def remove_stat(self, stat, value):
        self.stats[stat] -= value
    
    def get_stats(self):
        return self.stats
    
    def attack(self, enemy):
        hit = self.stats['Wisdom'] - enemy.stats['Defence']
        hit = random.randrange(1,hit+1)
        if hit < 1:
            hit = 1
        return hit
        

    
    
class enemy():
    def __init__(self, name, attacktype, health):
        self.name = name
        self.attacktype = attacktype
        self.health = health
        self.stats = {
            'Health': 0,
            'Strength': 0,
            'Wisdom': 0,
            'Defence': 0
                      }
        
    def add_stat(self, stat, value):
        self.stats[stat] += value
        
    def remove_stat(self, stat, value):
        self.stats[stat] -= value
    
    def get_stats(self):
        return self.stats
    
        
        

####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################
 

    
    
    
slow_print(0,["Welcome to  --- GAME ---."])    
slow_print(.8,["Lets create your character... "])


""" name = str(typingInput('What do you want to be named?\n'))
weight = float(typingInput('What is your weight in pounds?\n'))
height = float(typingInput('How tall are you in feet?\n'))
race = str(typingInput('What is your race? (Human, Elf, Dwarf, Orc)\n'))
typeofclass = str(typingInput('What class do you want to be? (Warrior, Priest, Rogue)\n'))
 """
character = adventurer('player1', 150, 6, 'elf', 'warrior')
orc = enemy('orc1', 'melee', 10)

character.add_stat('Mining', 3)


mineOre(character, 'tin')

print(character.get_inventory(), character.get_stats())
 
 
    



