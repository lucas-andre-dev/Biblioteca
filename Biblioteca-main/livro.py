# Importações necessárias para as estruturas de dados e registos.
from arrayStack import ArrayStack
from vetorCircular import ArrayQueueCircular
from reserva import Reserva
from registro_historico import RegistroHistorico


class Livro:
    """
    Representa um livro no catálogo da biblioteca.

    Esta classe encapsula todos os dados de um livro, bem como as suas
    estruturas de dados associadas: uma pilha para o histórico de atividades
    e uma fila para as reservas.
    """

    def __init__(self, titulo, autor, anoPublicacao, editora, cidade, quantidade, status, indice):
        """
        Construtor da classe Livro.

        Parâmetros de Entrada:
            titulo (str): O título do livro.
            autor (str): O autor do livro.
            anoPublicacao (str): O ano de publicação.
            editora (str): A editora.
            cidade (str): A cidade da editora.
            quantidade (int): A quantidade inicial de exemplares.
            status (str): O status inicial (geralmente 'Disponível').
            indice (int): O índice único do livro no catálogo.
        """
        # -> ALTERADO: Agora armazenamos a quantidade total e a disponível separadamente.
        self.quantidade_total = int(quantidade)  # Quantidade total de cópias que a biblioteca possui. Nunca muda.
        self.quantidade = int(quantidade)  # Quantidade de cópias atualmente disponíveis na prateleira.

        # Estrutura de dados para o histórico permanente de empréstimos e devoluções.
        self.historico = ArrayStack()
        # Estrutura de dados para a fila de espera de reservas.
        self.reserva = ArrayQueueCircular()

        # Atributos de informação do livro.
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao
        self.editora = editora
        self.cidade = cidade
        self.status = status
        self.indice = int(indice)

    def __str__(self):
        """
        Retorna uma representação em string do objeto Livro.
        """
        return (f"---------------------\n"
                f"Título: {self.titulo} - Índice: {self.indice}\n"
                f"Autor: {self.autor}\n"
                f"Quantidade: {self.quantidade} disponível(is) de {self.quantidade_total}\n"
                f"Status: {self.status}\n"
                f"---------------------")

    def emprestar(self, pessoa):
        """
        Processa o empréstimo de um livro para uma pessoa.
        """
        # Verifica se há exemplares disponíveis na prateleira.
        if self.quantidade > 0:
            # Decrementa a quantidade de cópias disponíveis.
            self.quantidade -= 1

            # Cria um novo registo de histórico do tipo "Empréstimo".
            novo_registro = RegistroHistorico("Empréstimo", pessoa)
            # Adiciona o registo à pilha de histórico.
            self.historico.push(novo_registro)

            print(f"\nLIVRO EMPRESTADO COM SUCESSO para {pessoa}!")

            # Se a quantidade disponível chegou a zero, atualiza o status.
            if self.quantidade == 0:
                self.status = "Emprestado"
        else:
            # Se não há exemplares, adiciona a pessoa à fila de reserva.
            print(f"\nLIVRO '{self.titulo}' INDISPONÍVEL!")
            newNodeReserva = Reserva(self.titulo, pessoa, self.indice)
            self.reserva.enqueue(newNodeReserva)
            print(f"{pessoa}, você foi adicionado(a) à fila de reserva.")

    def devolver(self, pessoa):
        """
        Processa a devolução de um livro e retorna o próximo da fila de reserva, se houver.
        """
        # Verifica se a quantidade de cópias disponíveis já é igual ao total de cópias.
        if self.quantidade >= self.quantidade_total:
            # Se for, significa que não há livros emprestados para serem devolvidos.
            print(f"\nOperação inválida. Não há cópias do livro '{self.titulo}' emprestadas para serem devolvidas.")
            # Retorna None para indicar que a operação falhou.
            return None

        # Se a validação passar, incrementa a quantidade de exemplares disponíveis.
        self.quantidade += 1

        # Cria um novo registo de histórico do tipo "Devolução".
        novo_registro = RegistroHistorico("Devolução", pessoa)
        # Adiciona o registo à pilha de histórico.
        self.historico.push(novo_registro)

        # Atualiza o status do livro para "Disponível", pois agora há pelo menos uma cópia.
        self.status = "Disponível"
        print(f"\nLivro '{self.titulo}' devolvido por {pessoa}.")

        # Verifica se há alguém na fila de reserva.
        if not self.reserva.is_empty():
            # Remove o próximo da fila para notificação.
            proxima_reserva = self.reserva.dequeue()
            # Retorna o objeto da reserva para que o 'main' possa lidar com a notificação.
            return proxima_reserva

        # Se não houver ninguém na fila, retorna None.
        return None