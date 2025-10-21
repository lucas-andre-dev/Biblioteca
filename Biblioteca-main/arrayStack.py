from singlyLinkedListIterator import SinglyLinkedListIterator

class ArrayStack:
    def __init__(self):
        self._data = SinglyLinkedListIterator()

    def __len__(self):
        return self._data.size

    def is_empty(self):
        return self._data.size == 0

    def push(self, data):
        # empilha no final (padrão da lista)
        self._data.addNode(data)

    def top(self):
        # verifica se a pilha está vazia
        if self.is_empty():
            print("Pilha vazia.")
            return None

        # posiciona no último nó e retorna o dado
        self._data.last_Node()
        return self._data.iterator.data

    def pop(self):
        # verifica se está vazia
        if self.is_empty():
            print("Pilha vazia, nada para remover.")
            return None

        # vai até o topo
        self._data.last_Node()
        retorno = self._data.iterator.data
        self._data.elimNode()
        return retorno
