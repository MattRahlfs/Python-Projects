import os
import json
import time

class task():
    def __init__ (self, description):
        self.description = description
        self.time = str(time.strftime("%H:%M:%S"))
        
    def convertToJSON():
        
        pass
            
def mainMenu():
    
    while True:
        userInput = input("Press 1 to list the tasks\nPress 2 to create a a new task\nPress 3 to update a task\nPress 4 to delete a task\nPress q to quit\nEnter an option: ")
        
        if userInput == '1':
            displayTasks()
        elif userInput == '2':
            createTasks()
        elif userInput == '3':
            taskIndexToUpdate = input("What index would you like to update?  ")
            updateTasks(int(taskIndexToUpdate))
        elif userInput == '4':
            taskIndexToDelete = input("What index would you like to delete?  ")
            deleteTask(int(taskIndexToDelete))
        elif userInput == 'q':
            break
        elif userInput != '1' or '2' or '3' or 'q':
            print("\nEnter a correct value\n")
            mainMenu()
        else:
            break
        
        
def jsonFileIO(data, readOrWrite, fileName):
        
    if readOrWrite == 'r':
        with open (str(fileName), str(readOrWrite)) as fileIO:
            readFile = json.load(fileIO)    
            return readFile
    elif readOrWrite == 'w':
        with open (str(fileName), str(readOrWrite)) as fileIO:
            json.dump(data, fileIO)

        

def createFileStructure():
    currentWorkingDirectory = os.getcwd()
    todoDirectory =  currentWorkingDirectory + '\\todo\\'
    
    
    if not os.path.exists(todoDirectory + 'todo.json'):
        if not os.path.exists(todoDirectory):
            os.mkdir('todo')
            os.chdir(todoDirectory)
            data = {"Tasks":[]} 
            jsonFileIO(data, 'w', 'todo.json')      
        elif os.path.exists(todoDirectory):
            os.chdir(todoDirectory)
            data = {"Tasks":[]} 
            jsonFileIO(data, 'w', 'todo.json') 
    os.chdir(todoDirectory)



def displayTasks():
    
    todoList = jsonFileIO('', 'r', 'todo.json')
    print ('\n','Task:', '               ', 'Time created:', '\n')
    for eachTask in todoList['Tasks']:
        
        print (eachTask['Description'], '               ',eachTask['Time'])
    
    print('\n')
    
    
    
def createTasks():
    taskDetail = input("Enter the task you want to add to the list  ")
    newTask = task(taskDetail)
    
    todoList = jsonFileIO('', 'r', 'todo.json')
    
    todoList['Tasks'].append({'Description': newTask.description, 'Time': newTask.time})
    
    jsonFileIO(todoList, 'w', 'todo.json')
    
    displayTasks()
        

# allow user to update a task
    #find the task based on name and update the description for that particular index  
def updateTasks(taskIndexToUpdate):
    
    todoList = jsonFileIO('', 'r', 'todo.json')
    taskDetail = input("Enter the task description you want to add to the list  ")
    newTask = task(taskDetail)
     
    todoList['Tasks'][taskIndexToUpdate -1]['Description'] = newTask.description
    
    jsonFileIO(todoList,'w','todo.json')
    
    displayTasks()
     
    pass

    
def deleteTask(taskIndexToDelete):
    
    todoList = jsonFileIO('', 'r', 'todo.json')
    
    todoList['Tasks'].pop(taskIndexToDelete -1)
    
    jsonFileIO(todoList, 'w', 'todo.json')
    
    displayTasks()
    
    pass



createFileStructure()
mainMenu()







