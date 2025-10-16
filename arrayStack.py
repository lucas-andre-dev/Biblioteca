from linglyListNode import ListNode
class ArrayStack:
    def __init__(self,topo = None,size = 0):
        self.topo = topo
        self.size = size
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        if self.size == 0:
            return True

    def push(self,data):
        newNode = ListNode(data)

        if self.topo is None:
            self.topo = newNode
            newNode.nextNode = None
            self.size += 1
        
        else:
            newNode.nextNode = self.topo
            self.topo = newNode
            self.size += 1

    def top(self):
        if self.topo is None:
            return print("Pilha vazia")
        return  print(self.topo.data)
    
    def pop(self):
        delete = self.topo
        retorno =self.topo.data
        self.topo = self.topo.nextNode
        delete = None
        return retorno


        