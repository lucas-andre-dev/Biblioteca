from doublyListNode import Node

class DoublyLinkedListIterator:
    def __init__(self):
        self.firstNode = None   # Ponteiro para o primeiro nó
        self.lastNode = None    # Ponteiro para o último nó
        self.iterator = None    # Ponteiro para o nó atual (iterador)
        self.size = 0           # Número de elementos na lista

    # ------------------------------------------------------
    # Adiciona um novo nó DEPOIS do iterador atual
    # ------------------------------------------------------
    def addNode(self, data):
        newNode = Node(data)

        if self.firstNode is None:  # Lista vazia
            self.firstNode = newNode
            self.lastNode = newNode
            self.iterator = newNode
        else:
            if self.iterator is None:
                self.iterator = self.lastNode

            newNode.antNode = self.iterator
            newNode.nextNode = self.iterator.nextNode

            if self.iterator.nextNode:
                self.iterator.nextNode.antNode = newNode
            else:
                self.lastNode = newNode  # Atualiza último nó

            self.iterator.nextNode = newNode
            self.iterator = newNode

        self.size += 1

    # ------------------------------------------------------
    # Insere um novo nó ANTES do iterador atual
    # ------------------------------------------------------
    def insNode(self, data):
        newNode = Node(data)

        if self.firstNode is None:  # Lista vazia
            self.firstNode = newNode
            self.lastNode = newNode
            self.iterator = newNode
        else:
            if self.iterator is None:
                self.iterator = self.firstNode

            newNode.nextNode = self.iterator
            newNode.antNode = self.iterator.antNode

            if self.iterator.antNode:
                self.iterator.antNode.nextNode = newNode
            else:
                self.firstNode = newNode  # Atualiza primeiro nó

            self.iterator.antNode = newNode
            self.iterator = newNode

        self.size += 1

    # ------------------------------------------------------
    # Remove o nó sob o iterador e move o iterador para o próximo
    # ------------------------------------------------------
    def elimNode(self):
        if self.iterator is None:
            print("Iterador indefinido.")
            return

        prev = self.iterator.antNode
        nxt = self.iterator.nextNode

        if prev:
            prev.nextNode = nxt
        else:
            self.firstNode = nxt  # Removendo o primeiro nó

        if nxt:
            nxt.antNode = prev
        else:
            self.lastNode = prev  # Removendo o último nó

        self.iterator = nxt
        self.size -= 1

    # ------------------------------------------------------
    # Move o iterador para o primeiro nó
    # ------------------------------------------------------
    def first_node(self):
        self.iterator = self.firstNode

    # ------------------------------------------------------
    # Move o iterador para o último nó
    # ------------------------------------------------------
    def last_node(self):
        self.iterator = self.lastNode

    # ------------------------------------------------------
    # Avança o iterador uma posição à frente
    # ------------------------------------------------------
    def nextNode(self):
        if self.iterator is not None:
            self.iterator = self.iterator.nextNode

    # ------------------------------------------------------
    # Retrocede o iterador uma posição
    # ------------------------------------------------------
    def antNode(self):
        if self.iterator is not None:
            self.iterator = self.iterator.antNode

    # ------------------------------------------------------
    # Verifica se o iterador está indefinido (None)
    # ------------------------------------------------------
    def undefinedIterator(self):
        return self.iterator is None

    # ------------------------------------------------------
    # Exibe todos os elementos da lista
    # ------------------------------------------------------
    def printLista(self):
        lista = self.firstNode
        print("Lista de elementos:")
        while lista is not None:
            print(lista.data)
            lista = lista.nextNode
        print(f"Total de elementos: {self.size}")
