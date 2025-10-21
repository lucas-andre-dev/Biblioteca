from doublyLinkedListIterator import DoublyLinkedListIterator
from livro import Livro


class Catalogo:
    def __init__(self):
        self.livros = DoublyLinkedListIterator()

    def addLivro(self, titulo, autor, anoPublicacao, editora, cidade, quantidade, status):
        self.livros.last_node()
        indice = self.livros.size
        livro = Livro(titulo, autor, anoPublicacao, editora, cidade, quantidade, status, indice)
        self.livros.addNode(livro, indice)

    def listarLivro(self):
        self.livros.printLista()

    def buscar(self, indice):
        self.livros.buscar(indice)

    def get_livro_por_indice(self, indice):
        return self.livros.get_data_by_indice(indice)