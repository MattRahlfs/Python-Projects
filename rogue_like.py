import time
import random
import json
import os

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
            'Wisdom': 0,
            'Defence': 0,
            'Mining': 0
                      }
    
    def get_inventory(self):
        return self.inventory
    
    def add_to_inventory(self, *args):
        
        for item in args:
            self.inventory.append(item)
        
    def remove_from_inventory(self, *args):
        self.inventory.remove(*args)
        
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
  
def updatePersistantCharacterFile(character):
    data = {
        'Character':{
            'name': character.name,
            'weight': character.weight,
            'height': character.height,
            'race': character.race,
            'class': character.typeofclass,
            'inventory': character.inventory,
            'stats': character.stats,
            
        }
        
    }
    
    with open (str(character.name) + '.json', 'w') as writeToFile:
        json.dump(data, writeToFile)
     
def getPersistantCharacterFile(character):
           
    with open(str(character) + '.json', 'r') as readFile:
        data = json.load(readFile)
        return data
    
def generateNewCharacterObject(character):
    data = getPersistantCharacterFile(character)
    
    character = adventurer(
        data['Character']['name'],
        data['Character']['weight'], 
        data['Character']['height'], 
        data['Character']['race'],
        data['Character']['class']
        )
    
    return character
    
    
    
    
        
def createNewCharacter():
    name = str(typingInput('What do you want to be named?\n'))
    weight = float(typingInput('What is your weight in pounds?\n'))
    height = float(typingInput('How tall are you in feet?\n'))
    race = str(typingInput('What is your race? (Human, Elf, Dwarf, Orc)\n'))
    typeofclass = str(typingInput('What class do you want to be? (Warrior, Priest, Rogue)\n'))
    
    character = adventurer(name, weight, height, race, typeofclass)
    
    updatePersistantCharacterFile(character)
    return character
 

def mineOre(player, typeOfOre):
    requiredLeveltoMineOre = {
        'tin': 1,
        'copper': 5,
        'iron': 10,
        'coal': 15,
        'mithril': 20,
        'gold': 40,
        'adamant': 50,
        'rune': 60

        }

    playerMiningLevel = player.stats['Mining']
    levelDifference = playerMiningLevel - requiredLeveltoMineOre[typeOfOre.lower()] 
    levelModifier = ((levelDifference // 5) + ((levelDifference // 10) * 2))



    if playerMiningLevel < requiredLeveltoMineOre[typeOfOre.lower()]:
        print ('You do not meet the level requirment.')
    else:
        counter = 4
        print ('You attempt to mine the ore...')
        while counter >= 0:
            sucessfulMine = random.randint(0, 100)
            print(sucessfulMine, levelModifier, sucessfulMine - levelModifier)
            if (sucessfulMine - levelModifier) < 25:
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

slow_print(0,["Welcome to  --- GAME ---."])    
#slow_print(.8,["Lets create your character... "])

chooseCharacter = (str(input('Do you already have a chacter? (y/n)    ')))

if(chooseCharacter.lower() == 'y'):
    whatCharacter = str(input('Enter the character name.    '))
    character = generateNewCharacterObject(whatCharacter)
else:
    character = createNewCharacter()


print (character)


#print(character.get_inventory(), character.get_stats())
 
 
    



