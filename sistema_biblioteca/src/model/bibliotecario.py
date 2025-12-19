from xmlrpc.client import FastParser

from sistema_biblioteca.src.controller import livro_controller
from sistema_biblioteca.src.model.usuario import Usuario
from sistema_biblioteca.src.controller.livro_controller import LivroDAO


class Bibliotecario (Usuario):
    def __init__(self):
        super()

    def cadastrarLivro(self, titulo, autor, isbn):
        sucesso = livro_controller.cadastrarLivro(titulo, autor, isbn, disponivel = True)
        if sucesso:
            return True
        return False

    def deletarLivro(self, isbn):
        sucesso = livro_controller.deletarLivro(isbn)
        if sucesso:
            return True
        return False

    def alterarLivro(self, titulo, autor, isbn):
        sucesso = livro_controller.editarLivro(titulo, autor, isbn)
        if sucesso:
            return True
        return False

    def alterarUsuario(self, nome, senha, idUsuario):
        sucesso = usuario_controller.alterarUsuario(nome, senha, idUsuario)
        if sucesso:
            return True
        return False

    def deletarUsuario(self, idUsuario):
        sucesso = usuario_controller.deletarUsuario(idUsuario)
        if sucesso:
            return True
        return False