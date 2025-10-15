# 📚 Sistema de Gerenciamento de Biblioteca

## 🧠 Visão Geral
O **Sistema de Gerenciamento de Biblioteca** é um projeto acadêmico desenvolvido em **Python**, que utiliza **estruturas de dados clássicas** — **Lista Duplamente Encadeada**, **Pilha** e **Fila** — para simular as operações de um sistema de biblioteca real.  

O objetivo é aplicar conceitos de estrutura de dados na prática, criando um sistema funcional capaz de **gerenciar livros, empréstimos, devoluções e reservas** com eficiência.

---

## ⚙️ Funcionalidades Principais

✅ **Gerenciamento de Catálogo (Lista Duplamente Encadeada)**  
- Armazena e organiza os livros da biblioteca.  
- Permite inserção, remoção, busca e navegação eficiente.  
- Cada nó contém: título, autor, ano, editora, cidade, quantidade e status do empréstimo.  

✅ **Histórico de Empréstimos (Pilha)**  
- Registra todas as atividades de cada livro.  
- Cada operação de **empréstimo** ou **devolução** é empilhada, mantendo o histórico sequencial.  
- Permite visualizar a última ação realizada para cada livro.  

✅ **Fila de Espera (Fila)**  
- Gerencia as reservas de livros indisponíveis.  
- Notifica automaticamente o próximo usuário quando um livro é devolvido.  
- Usuário notificado tem **24h para efetuar o empréstimo**.  

        self.nextNode = nextNode
        self.antNode = antNode
