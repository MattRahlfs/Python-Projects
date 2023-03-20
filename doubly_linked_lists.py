class Node():
   def __init__ (self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous
        
        
class DoublyLinkedList():
    def __init__ (self):
            self.head = None
    
    def prepend(self, data):
        newNode = Node(data)
        
        if self.head is None:
            self.head = newNode
        else:
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode     
    
    def append(self, data):
        newNode = Node(data)
        
        if self.head == None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            
            currentNode.next = newNode
            newNode.previous = currentNode
            newNode.next  = None
        
    def print_List(self):
        currentNode = self.head
        
        while currentNode:
            print (currentNode.data)
            currentNode = currentNode.next
            
    def create_Array_Of_List(self):
        currentNode = self.head
        arrayOfNodes = []
        
        while currentNode:
            arrayOfNodes.append(currentNode.data)
            currentNode = currentNode.next
        return arrayOfNodes
    
    def print_Head(self):
        print(self.head.data)
            
            

dll = DoublyLinkedList()

dll.prepend(0)
dll.append(1)
dll.append('things')
dll.append(2)
dll.append(3)
dll.prepend(65)
dll.append('dsf')
dll.append(['a','b','c'])

items = dll.create_Array_Of_List()
print(items)
dll.print_List()


for index, eachitem in enumerate(items):
    print (items[index])
 
















