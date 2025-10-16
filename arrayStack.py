from singlyLinkedListIterator import SinglyLinkedListIterator
class ArrayStack:
    def __init__(self):
        self._data = SinglyLinkedListIterator()

    def __len__(self):
        return self._data.size
    
    def is_empty(self):
        if self._data.size == 0:
            return True
        else:
            return False
        
    def push(self,data):
        self._data.addNode(data)

    def top(self):
        if self._data.size is None:
            return print("Pilha vazia")
        else:
            self._data.last_Node()
            return print(self._data.iterator.data)
    
    def pop(self):
        self._data.last_Node()
        retorno = self._data.iterator.data
        self._data.elimNode()
        return retorno

        


        