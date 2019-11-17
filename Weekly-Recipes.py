'''
Created on Jan 6, 2019

@author: Matt
'''
import os
import random
from datetime import date
from distutils.tests.test_register import RawInputs
from __builtin__ import raw_input
from time import sleep



_workingDir = "C:/Program Files (x86)/Weekly-Recipes"



def createWorkingDirs():
    
    _neededDirs = [_workingDir, _workingDir + "/Recipes", _workingDir + "/Lists"]
    
    try:
        
        for _eachDir in _neededDirs:
            if not (os.path.isdir(_eachDir)):
                os.mkdir(_eachDir)     
    except Exception as error:        
        print (error)
        print "Unable to create " + _workingDir
        
    return True

    
def createNewRecipe(_recipeName, _ingredients):
    
    _appendData = open(_workingDir + "/Recipes/" + _recipeName + ".txt", 'w+')
    
    for _ingredient in _ingredients:
        _appendData.write(_ingredient + "\n")
    
    _appendData.close

  
def getRecipeInformation():
    
    _collectedIngredients = []
    
    try:
        
        if not (os.path.isdir(_workingDir + "/Recipes")):
            createWorkingDirs()
        
    except Exception as error:
        print(error)
        
    _recipeName = raw_input("What is the recipe name?\n")
     
    print "\n\nEnter a blank line to continue\n"
    print "Enter the ingredients one per line." 
        
    while True:
        
        _inputFromUser = raw_input()
    
        if _inputFromUser:
            _collectedIngredients.append(_inputFromUser)
        else:
            break
   
    createNewRecipe(_recipeName, _collectedIngredients)
 

def createWeeklyList():
    
    _listofRecipes = []
    
    def getRandomRecipe():
        
        _currentRecipe = random.choice(os.listdir(_workingDir + "/Recipes"))   
        
        if not _currentRecipe in _listofRecipes:
            _listofRecipes.append(_currentRecipe)
        else:
            getRandomRecipe()
    
    try:
        
        os.path.isdir(_workingDir + "/Lists")
        
    except Exception as error:
        print(error)
              
    for _eachRecipe in range(0,5):
        getRandomRecipe()
        
    _appendData = open(_workingDir + "/Lists/" + "Recipes for " + str(date.today()) + ".txt", 'w+')
    for _eachRecipe in _listofRecipes:
        _appendData.write(_eachRecipe[:-4] + ":\n")
        
        _appendIngredients = open(_workingDir + "/Recipes/" + _eachRecipe, "r")
        _appendIngredients = _appendIngredients.readlines()
          
        for _eachIngredient in _appendIngredients:
            _appendData.write(_eachIngredient)
            
        _appendData.write("\n\n")
    
    _appendData.close()
    

    os.system("notepad.exe C:/Program Files (x86)/Weekly-Recipes/Lists/Recipes for " + str(date.today()))
   
        
def initializer():
    
       
    if not(createWorkingDirs()):
        createWorkingDirs()
    
    _chooseFunction = [exit, getRecipeInformation, createWeeklyList,]
    
    print "\nMenu\n\n" + "1. Create a new recipe.\n" + "2. Get a weekly list.\n" + "0. EXIT.\n"
    
    
    try:
        _inputFromUser = int(raw_input("\nChoose your option.\n"))
    except ValueError:
        print "enter a valid option 1,2,0"
        initializer()
     
     
    if (_inputFromUser > 2) or (_inputFromUser < 0) or (isinstance(_inputFromUser, int) == False):
        print "enter a valid option please 1,2,0"
        initializer()
    else:
        _chooseFunction[_inputFromUser]()
    

  
while True:
                  
    initializer()


































