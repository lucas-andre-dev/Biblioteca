# Importa a classe Node do ficheiro doublyListNode para ser usada como elemento da lista.
from doublyListNode import Node


# Definição da classe que representa uma Lista Duplamente Encadeada com um iterador.
class DoublyLinkedListIterator:
    """
    Representa uma Lista Duplamente Encadeada.

    Esta estrutura de dados permite armazenar uma coleção de elementos (nós),
    onde cada nó tem uma referência para o nó anterior e para o próximo,
    permitindo a travessia em ambas as direções. Um iterador interno
    aponta para um nó atual na lista para facilitar operações.
    """

    def __init__(self):
        """
        Construtor da classe DoublyLinkedListIterator.

        Inicializa uma lista vazia, definindo todos os ponteiros internos como None
        e o tamanho como 0.

        Parâmetros de Entrada:
            Nenhum.

        Retorno:
            Nenhum.
        """
        # Ponteiro para o primeiro nó da lista. Começa como None.
        self.firstNode = None
        # Ponteiro para o último nó da lista. Começa como None.
        self.lastNode = None
        # Ponteiro (iterador) que aponta para o nó atual. Começa como None.
        self.iterator = None
        # Inteiro que armazena o número de nós na lista. Começa como 0.
        self.size = 0

    def addNode(self, data, indice):
        """
        Adiciona um novo nó DEPOIS da posição atual do iterador.

        Cria um novo nó com os dados fornecidos e o insere após o nó
        apontado pelo iterador. O iterador é movido para o novo nó criado.

        Parâmetros de Entrada:
            data: O dado a ser armazenado no novo nó (ex: um objeto Livro).
            indice: Um identificador para o dado (ex: o ID do livro).

        Retorno:
            Nenhum.
        """
        # Cria uma nova instância de Node com os dados e o índice.
        newNode = Node(data, indice)

        # Verifica se a lista está vazia.
        if self.firstNode is None:
            # Se estiver vazia, o novo nó é o primeiro, o último e o iterador.
            self.firstNode = newNode
            self.lastNode = newNode
            self.iterator = newNode
        else:
            # Se a lista não estiver vazia:
            # Se o iterador não aponta para lugar nenhum, posiciona-o no último nó por padrão.
            if self.iterator is None:
                self.iterator = self.lastNode

            # Define o nó anterior do novo nó como o nó do iterador.
            newNode.antNode = self.iterator
            # Define o próximo nó do novo nó como o próximo do iterador.
            newNode.nextNode = self.iterator.nextNode

            # Se havia um nó após o iterador, atualiza o seu ponteiro 'anterior'.
            if self.iterator.nextNode:
                self.iterator.nextNode.antNode = newNode
            else:
                # Se não havia, o novo nó é o novo último nó da lista.
                self.lastNode = newNode

            # Define o próximo do iterador como o novo nó.
            self.iterator.nextNode = newNode
            # Move o iterador para o novo nó recém-adicionado.
            self.iterator = newNode

        # Incrementa o contador de tamanho da lista.
        self.size += 1

    def insNode(self, data, indice):
        """
        Insere um novo nó ANTES da posição atual do iterador.

        Cria um novo nó com os dados fornecidos e o insere antes do nó
        apontado pelo iterador. O iterador é movido para o novo nó criado.

        Parâmetros de Entrada:
            data: O dado a ser armazenado no novo nó.
            indice: Um identificador para o dado.

        Retorno:
            Nenhum.
        """
        # Cria uma nova instância de Node com os dados e o índice.
        newNode = Node(data, indice)

        # Verifica se a lista está vazia.
        if self.firstNode is None:
            # Se estiver vazia, o novo nó torna-se o primeiro, o último e o iterador.
            self.firstNode = newNode
            self.lastNode = newNode
            self.iterator = newNode
        else:
            # Se a lista não estiver vazia:
            # Se o iterador for nulo, posiciona-o no primeiro nó.
            if self.iterator is None:
                self.iterator = self.firstNode

            # Define o próximo nó do novo nó como o nó do iterador.
            newNode.nextNode = self.iterator
            # Define o nó anterior do novo nó como o anterior do iterador.
            newNode.antNode = self.iterator.antNode

            # Se havia um nó antes do iterador, atualiza o seu ponteiro 'próximo'.
            if self.iterator.antNode:
                self.iterator.antNode.nextNode = newNode
            else:
                # Se não havia, o novo nó é o novo primeiro nó da lista.
                self.firstNode = newNode

            # Define o anterior do iterador como o novo nó.
            self.iterator.antNode = newNode
            # Move o iterador para o novo nó recém-inserido.
            self.iterator = newNode

        # Incrementa o contador de tamanho da lista.
        self.size += 1

    def elimNode(self):
        """
        Elimina o nó sob a posição atual do iterador.

        Remove o nó atualmente apontado pelo iterador. O iterador é movido
        para o próximo nó da lista.

        Parâmetros de Entrada:
            Nenhum.

        Retorno:
            Nenhum.
        """
        # Verifica se o iterador está definido (apontando para um nó).
        if self.iterator is None:
            # Se não estiver, imprime uma mensagem e encerra a função.
            print("Iterador indefinido. Nenhuma ação realizada.")
            return

        # Guarda a referência para o nó anterior ao do iterador.
        prev = self.iterator.antNode
        # Guarda a referência para o nó seguinte ao do iterador.
        nxt = self.iterator.nextNode

        # Se existe um nó anterior, atualiza o seu ponteiro 'próximo' para pular o nó atual.
        if prev:
            prev.nextNode = nxt
        else:
            # Se não há anterior, significa que estamos a remover o primeiro nó. O 'firstNode' passa a ser o próximo.
            self.firstNode = nxt

        # Se existe um nó seguinte, atualiza o seu ponteiro 'anterior' para pular o nó atual.
        if nxt:
            nxt.antNode = prev
        else:
            # Se não há seguinte, significa que estamos a remover o último nó. O 'lastNode' passa a ser o anterior.
            self.lastNode = prev

        # Move o iterador para o próximo nó da lista.
        self.iterator = nxt
        # Decrementa o contador de tamanho da lista.
        self.size -= 1

    def first_node(self):
        """
        Posiciona o iterador no primeiro nó da lista.

        Parâmetros de Entrada:
            Nenhum.

        Retorno:
            Nenhum.
        """
        # Move o iterador para apontar para o primeiro nó da lista.
        self.iterator = self.firstNode

    def last_node(self):
        """
        Posiciona o iterador no último nó da lista.

        Parâmetros de Entrada:
            Nenhum.

        Retorno:
            Nenhum.
        """
        # Move o iterador para apontar para o último nó da lista.
        self.iterator = self.lastNode

    def nextNode(self):
        """
        Avança o iterador uma posição para a frente.

        Se o iterador estiver no último nó, ele se tornará None.

        Parâmetros de Entrada:
            Nenhum.

        Retorno:
            Nenhum.
        """
        # Verifica se o iterador está atualmente a apontar para um nó.
        if self.iterator is not None:
            # Move o iterador para o próximo nó na sequência.
            self.iterator = self.iterator.nextNode

    def antNode(self):
        """
        Retrocede o iterador uma posição para trás.

        Se o iterador estiver no primeiro nó, ele se tornará None.

        Parâmetros de Entrada:
            Nenhum.

        Retorno:
            Nenhum.
        """
        # Verifica se o iterador está atualmente a apontar para um nó.
        if self.iterator is not None:
            # Move o iterador para o nó anterior na sequência.
            self.iterator = self.iterator.antNode

    def undefinedIterator(self):
        """
        Verifica se o iterador está indefinido (None).

        Parâmetros de Entrada:
            Nenhum.

        Retorno:
            (bool): True se o iterador for None, False caso contrário.
        """
        # Retorna o resultado da comparação do iterador com None.
        return self.iterator is None

    def printLista(self):
        """
        Imprime todos os dados dos nós da lista no console.

        Percorre a lista desde o primeiro nó até o último, imprimindo
        o conteúdo de cada nó.

        Parâmetros de Entrada:
            Nenhum.

        Retorno:
            Nenhum.
        """
        # Verifica se a lista não tem elementos.
        if self.size == 0:
            # Informa ao utilizador que o catálogo está vazio.
            print("O catálogo está vazio.")
            # Encerra a função.
            return

        # Cria uma variável temporária para percorrer a lista, começando pelo primeiro nó.
        currentNode = self.firstNode
        # Imprime um cabeçalho para a listagem.
        print("Lista de Livros no Catálogo:")
        # Loop que continua enquanto o nó atual não for None.
        while currentNode is not None:
            # Imprime os dados do nó atual (que é um objeto Livro e usará seu método __str__).
            print(currentNode.data)
            # Move a variável para o próximo nó da lista.
            currentNode = currentNode.nextNode
        # Ao final, imprime o número total de livros no catálogo.
        print(f"Total de livros: {self.size}")

    def buscar(self, elem):
        """
        Busca e imprime um nó na lista com base no seu índice.

        Parâmetros de Entrada:
            elem (int): O índice do elemento a ser procurado.

        Retorno:
            Nenhum.
        """
        # Posiciona o iterador no início da lista para começar a busca.
        self.iterator = self.firstNode
        # Variável para controlar se o livro foi encontrado.
        encontrado = False
        # Percorre a lista enquanto o iterador não for nulo.
        while self.iterator is not None:
            # Compara o índice do nó atual com o elemento procurado.
            if self.iterator.indice == elem:
                # Se encontrar, imprime os dados do livro.
                print(self.iterator.data)
                # Define a flag como True.
                encontrado = True
                # Interrompe o loop, pois o livro já foi encontrado.
                break
            # Avança o iterador para o próximo nó.
            self.iterator = self.iterator.nextNode
        # Se o loop terminar e o livro não for encontrado, exibe uma mensagem.
        if not encontrado:
            print(f"Nenhum livro encontrado com o índice {elem}.")

    def get_data_by_indice(self, indice):
        """
        Busca um nó pelo seu índice e retorna o objeto de dados contido nele.

        Parâmetros de Entrada:
            indice (int): O índice do nó a ser procurado.

        Retorno:
            (object): O dado armazenado no nó (ex: objeto Livro) ou None se não for encontrado.
        """
        # Começa a busca a partir do primeiro nó.
        currentNode = self.firstNode
        # Percorre a lista.
        while currentNode is not None:
            # Verifica se o índice do nó atual corresponde ao índice procurado.
            if currentNode.indice == indice:
                # Se encontrar, retorna o objeto de dados armazenado no nó.
                return currentNode.data
            # Move para o próximo nó.
            currentNode = currentNode.nextNode
        # Se o loop terminar sem encontrar o nó, retorna None.
        return None