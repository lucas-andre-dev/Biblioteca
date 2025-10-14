from node import Node
class DoublyLinkedListIterator:
    def __init__(self):
        self.firstNode = None
        self.lastNode = None
        self.iterator = None
        self.size = None

    def addNode(self,data):
        newNode = Node(data,None,None)
        if self.firstNode is None:
            self.firstNode = newNode
            self.lastNode = newNode
            self.iterator = newNode
            self.size = 1
        else:
            newNode.antNode = self.iterator
            self.iterator.nextNode = newNode
            self.iterator = newNode
            self.size += 1

    def insNode(self,data):
        newNode = Node(data,None,None)
        if self.firstNode is None:
            self.firstNode = newNode
            self.lastNode = newNode
            self.iterator = newNode
        else:
            self.iterator.antNode = newNode
            self.iterator = newNode
            

    def nextNode(self):
        if self.iterator.nextNode is not None:
            self.iterator = self.iterator.nextNode
    
    def undefinedIterator(self):
        if self.iterator is None:
            return True
        else:
            return False

    def printLista(self):
        self.iterator = self.firstNode
        while self.iterator is not None:
            print(self.iterator.data)
            self.iterator = self.iterator.nextNode
        
