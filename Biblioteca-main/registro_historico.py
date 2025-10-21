# Importa o módulo datetime para trabalhar com datas e horas.
import datetime

# Define a classe que representa um único registo no histórico de um livro.
class RegistroHistorico:
    """
    Representa um evento no histórico de um livro (Empréstimo ou Devolução).
    """
    def __init__(self, tipo_evento, utilizador):
        """
        Construtor da classe RegistroHistorico.

        Parâmetros de Entrada:
            tipo_evento (str): O tipo de evento ('Empréstimo' ou 'Devolução').
            utilizador (str): O nome do utilizador que realizou a ação.
        """
        # Armazena o tipo de evento.
        self.tipo_evento = tipo_evento
        # Armazena o nome do utilizador.
        self.utilizador = utilizador
        # Captura e armazena a data e hora exatas em que o registo foi criado.
        self.data = datetime.datetime.now()

    def __str__(self):
        """
        Retorna uma representação em string do registo.
        """
        # Formata a data para um formato legível antes de retornar a string.
        data_formatada = self.data.strftime("%d/%m/%Y às %H:%M:%S")
        # Retorna a string formatada.
        return f"Evento: {self.tipo_evento}, Utilizador: {self.utilizador}, Data: {data_formatada}"