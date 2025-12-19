from sistema_biblioteca.src.controller import usuario_controller
from sistema_biblioteca.src.model.usuario import Usuario

class Leitor (Usuario):
    def __init__(self):
        super()

    def emprestarLivro(self, isbn):
        sucesso = usuario_controller.emprestarLivro(isbn)
        if sucesso:
            return True
        return False

    def devolverLivro(self, isbn):
        sucesso = usuario_controller.devolverLivro(isbn)
        if sucesso:
            return True
        return False