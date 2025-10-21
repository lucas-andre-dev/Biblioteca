from singlyListNode import ListNode


class SinglyLinkedListIterator:

    def __init__(self, firstNode=None):
        self.firstNode = firstNode
        self.lastNode  = firstNode
        self.iterator  = firstNode
        self.size = 0

    # ------------------------------------------------------
    # Adiciona um nó DEPOIS do iterador e move o iterador para ele
    # ------------------------------------------------------
    def addNode(self, data):
        newNode = ListNode(data)
        if self.size == 0:  # lista vazia
            self.firstNode = self.lastNode = self.iterator = newNode
        elif self.iterator == self.lastNode:  # iterador no último nó
            self.lastNode.nextNode = newNode
            self.iterator = self.lastNode = newNode
        else:  # iterador em nó intermediário
            newNode.nextNode = self.iterator.nextNode
            self.iterator.nextNode = newNode
            self.iterator = newNode
        self.size += 1
        return True

    # ------------------------------------------------------
    # Insere um nó ANTES do iterador e move o iterador para ele
    # ------------------------------------------------------
    def insNode(self, data):
        newNode = ListNode(data)
        if self.size == 0:  # lista vazia
            self.firstNode = self.lastNode = self.iterator = newNode
        elif self.iterator == self.firstNode:  # iterador no primeiro nó
            newNode.nextNode = self.firstNode
            self.firstNode = self.iterator = newNode
        else:  # iterador em nó intermediário
            currentNode = self.firstNode
            while currentNode.nextNode != self.iterator:
                currentNode = currentNode.nextNode
            newNode.nextNode = self.iterator
            currentNode.nextNode = newNode
            self.iterator = newNode
        self.size += 1
        return True

    # ------------------------------------------------------
    # Remove o nó sob o iterador e avança para o próximo
    # ------------------------------------------------------
    def elimNode(self):
        if self.iterator is None:
            return False
        if self.iterator == self.firstNode:
            if self.firstNode == self.lastNode:  # só um nó
                self.firstNode = self.lastNode = self.iterator = None
            else:
                self.firstNode = self.iterator.nextNode
                self.iterator.nextNode = None
                self.iterator = self.firstNode
        else:
            currentNode = self.firstNode
            while currentNode.nextNode != self.iterator:
                currentNode = currentNode.nextNode
            if self.iterator == self.lastNode:  # iterador no último nó
                self.lastNode = currentNode
                currentNode.nextNode = None
                self.iterator = None
            else:  # nó intermediário
                currentNode.nextNode = self.iterator.nextNode
                self.iterator.nextNode = None
                self.iterator = currentNode.nextNode
        self.size -= 1
        return True

    # ------------------------------------------------------
    # Posiciona o iterador no primeiro nó
    # ------------------------------------------------------
    def first_Node(self):
        self.iterator = self.firstNode
        return True

    # ------------------------------------------------------
    # Posiciona o iterador no último nó
    # ------------------------------------------------------
    def last_Node(self):
        self.iterator = self.lastNode
        return True

    # ------------------------------------------------------
    # Avança o iterador uma posição
    # ------------------------------------------------------
    def nextNode(self):
        if self.iterator:
            self.iterator = self.iterator.nextNode
        return True

    # ------------------------------------------------------
    # Posiciona o iterador em uma posição específica (1-based)
    # ------------------------------------------------------
    def posNode(self, position):
        if position < 1 or position > self.size:
            self.iterator = None
            return False
        self.iterator = self.firstNode
        for _ in range(1, position):
            self.iterator = self.iterator.nextNode
        return True

    # ------------------------------------------------------
    # Retorna True se o iterador estiver indefinido
    # ------------------------------------------------------
    def isUndefinedIterator(self):
        return self.iterator is None


    # ------------------------------------------------------
    # Imprime todos os elementos da lista
    # ------------------------------------------------------
    def printList(self):
        lista = self.firstNode
        print("Lista de elementos:")
        while lista:
            print(lista.data)
            lista = lista.nextNode
        print(f"Total de elementos: {self.size}")

    def printNode(self):
        return print(self.iterator.data)