#!python3

class Usuario:
    def __init__(self, nome, senha):
        self.__nome = nome
        self.__senha = senha
    

    # Getters e Setters
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def senha(self):
        return self.__senha
    
    @nome.setter
    def senha(self, nova_senha):
        self.__senha = nova_senha