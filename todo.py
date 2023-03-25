import os
import json
import time
import tkinter as tk

class task():
    def __init__ (self, description):
        self.description = description
        self.time = str(time.strftime("%H:%M:%S"))
    
class todo_gui():
    def __init__ (self):

        def updateListBox():
            tasksListBox.delete(0,tk.END)
            todoList = jsonFileIO('', 'r', 'todo.json')
            for eachTask in todoList['Tasks']:
                tasksListBox.insert(tk.END, eachTask['Description'])   
            tasksListBox.pack(pady=10)
            
        def createNewTask():
            if newTaskDescriptionText.get() == '':
                pass
            else:
                taskDetail = newTaskDescriptionText.get()
                newTask = task(taskDetail)
                todoList = jsonFileIO('', 'r', 'todo.json')
                todoList['Tasks'].append({'Description': newTask.description, 'Time': newTask.time})
                jsonFileIO(todoList, 'w', 'todo.json')
                newTaskDescriptionText.delete(0, tk.END)
                updateListBox()
            
        def updateExistingTask():
            if updateTaskDescriptionText.get() == '':
                pass
            else:
                todoList = jsonFileIO('', 'r', 'todo.json')
                todoList['Tasks'][tasksListBox.curselection()[0]]['Description'] = updateTaskDescriptionText.get()
                jsonFileIO(todoList, 'w', 'todo.json')
                updateTaskDescriptionText.delete(0, tk.END)
                updateListBox()
            
            
        def deleteExistingTask():
            try:
                todoList = jsonFileIO('', 'r', 'todo.json')
                todoList['Tasks'].pop(tasksListBox.curselection()[0])
                jsonFileIO(todoList, 'w', 'todo.json')
                updateListBox()
            except IndexError:
                pass
            
            
        def closeTodoList():
            pass
        root = tk.Tk()
        root.title('Todo List')
        root.geometry('400x400')
        root.resizable(False,False)
        root.eval('tk::PlaceWindow . center')
        
        todoList = jsonFileIO('', 'r', 'todo.json')
        listBoxFrame = tk.Frame(root)
        verticalScrollBar = tk.Scrollbar(listBoxFrame, orient=tk.VERTICAL)
        tasksListBox = tk.Listbox(listBoxFrame, width=50, height=10,selectmode=tk.SINGLE, yscrollcommand=verticalScrollBar.set)
        verticalScrollBar.config(command=tasksListBox.yview)
        verticalScrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        listBoxFrame.pack()
        updateListBox()
        
        newTaskLabel = tk.Label(root, text='Enter the description of a new task below')
        newTaskLabel.pack(pady=5)
        newTaskDescriptionText = tk.Entry(root)
        newTaskDescriptionText.pack()
        
        
        createTaskButton = tk.Button(root, text="ADD", command=createNewTask)
        createTaskButton.pack()
        
        deleteTaskButton = tk.Button(root, text="DELETE", command=deleteExistingTask)
        deleteTaskButton.pack(pady=5)
        
        updateTaskLabel = tk.Label(root, text='Enter the new description below')
        updateTaskLabel.pack(pady=5)
        updateTaskDescriptionText = tk.Entry(root)
        updateTaskDescriptionText.pack()
        updateTaskButton = tk.Button(root, text="Update", command=updateExistingTask)
        updateTaskButton.pack(pady=5)
        
        root.mainloop()
                        
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
        
def updateTasks(taskIndexToUpdate):
    todoList = jsonFileIO('', 'r', 'todo.json')
    taskDetail = input("Enter the task description you want to add to the list  ")
    newTask = task(taskDetail)
    todoList['Tasks'][taskIndexToUpdate -1]['Description'] = newTask.description
    jsonFileIO(todoList,'w','todo.json')
    displayTasks()
    
def deleteTask(taskIndexToDelete):
    todoList = jsonFileIO('', 'r', 'todo.json')
    todoList['Tasks'].pop(taskIndexToDelete -1)
    jsonFileIO(todoList, 'w', 'todo.json')
    displayTasks()
    
    
createFileStructure()
todo_gui()
