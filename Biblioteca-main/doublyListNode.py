class Node:
    def __init__(self,data,indice,nextNode=None, antNode=None):
        self.data = data
        self.indice = indice
        self.nextNode = nextNode
        self.antNode = antNode
