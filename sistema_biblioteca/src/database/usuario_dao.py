from database import Database

class Usuarios(object):
    def __init__(self, idUsuario = 0, nome = "", senha = ""):
        self.idUsuario = idUsuario
        self.nome = nome
        self.senha = senha
    
    # Inserir usuário
    def inserirUsuario(self):
        database = Database()
        try: 
            c = database.conexao.cursor()

            c.execute("insert into usuarios (nome, senha) values ('" + self.nome + "', '" + self.senha + "')")

            database.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"
    
    # Atualizar usuário
    def atualizarUsuario(self):
        database = Database()
        try:
            c = database.conexao.cursor()

            c.execute("update usuarios set nome = '" + self.nome + "', senha = '" + self.senha + "' where idUsuario = " + self.idUsuario + " ")

            database.conexao.commit()
            c.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"
    
    # Deletar usuário
    def deletarUsuario(self):
        database = Database()
        try:
            c = database.conexao.cursor()

            c.execute("delete from usuarios where idUsuario = " + self.idUsuario + " ")

            database.conexao.commit()
            c.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro ao excluir o usuário"
    
    # Buscar usuário
    def burcarUsuario(self, idUsuario):
        database = Database()
        try:
            c = database.conexao.cursor()

            c.execute("select * from usuarios where idUsuario = " + idUsuario + "  ")

            for linha in c:
                self.idUsuario = linha[0]
                self.nome = linha[1]
                self.senha = linha[2]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro ao buscar o usuário"