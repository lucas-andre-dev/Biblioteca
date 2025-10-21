class ArrayQueueCircular:
    def __init__(self, max_size=100):
        self._data = [None] * max_size
        self._max = max_size
        self._primeiro = 0
        self._ultimo = 0

    def is_empty(self):
        return self._primeiro == self._ultimo

    def is_full(self):
        return (self._ultimo + 1) % self._max == self._primeiro

    def enqueue(self, valor):
        if self.is_full():
            raise Exception("Fila cheia")
        self._data[self._ultimo] = valor
        self._ultimo = (self._ultimo + 1) % self._max

    def dequeue(self):
        if self.is_empty():
            raise Exception("Fila vazia")
        valor = self._data[self._primeiro]
        self._data[self._primeiro] = None
        self._primeiro = (self._primeiro + 1) % self._max
        return valor

    def first(self):
        if self.is_empty():
            raise Exception("Fila vazia")
        return self._data[self._primeiro]
