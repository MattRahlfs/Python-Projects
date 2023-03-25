import os
import json
import time

class task():
    def __init__ (self, description):
        self.description = description
        self.time = str(time.strftime("%H:%M:%S"))
        
    def convertToJSON():
        
        pass
            

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
    
    for eachTask in todoList['Tasks']:
        
        print (eachTask)
    
    
    
def createTasks():
    taskDetail = input("Enter the task you want to add to the list  ")
    newTask = task(taskDetail)
    
    todoList = jsonFileIO('', 'r', 'todo.json')
    
    todoList['Tasks'].append({'Description': newTask.description, 'Time': newTask.time})
    
    jsonFileIO(todoList, 'w', 'todo.json') 
        

# allow user to update a task
    #find the task based on name and update the description for that particular index  
def updateTasks():
    
    pass


# allow user to delete a task
    #find the task based on name and delete that index
    
def deleteTask():
    pass



createFileStructure()
#createTasks()
displayTasks()





