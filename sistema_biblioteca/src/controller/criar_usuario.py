from sistema_biblioteca.src.dao import usuario_dao
from sistema_biblioteca.src.dao.usuario_dao import UsuariosDAO
from sistema_biblioteca.src.model.usuario import Usuario


def cadastrar_usuario(nome, senha):
    dao = UsuariosDAO()
    dao.nome = nome
    dao.senha = senha

    sucesso = dao.inserirUsuario(nome, senha)
    if sucesso:
        return sucesso
    else:
        return False