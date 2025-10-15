class Node:
    def __init__(self,data,nextNode=None, antNode=None):
        self.data = data
        self.nextNode = nextNode
        self.antNode = antNode
