from database import Database

class Livro(object):
    def __init__(self, titulo = "", autor = "", isbn = ""):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    # Inserir livro
    def inserirLivro(self):
        database = Database()
        try: 
            c = database.conexao.cursor()

            c.execute("insert into livros (titulo, autor, isbn) values ('" + self.titulo + "', '" + self.autor + "', '" + self.isbn + "')")

            database.conexao.commit()
            c.close()

            return "Livro cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do livro"
        
    # Atualizar livro
    def atualizarLivro(self):
        database = Database()
        try:
            c = database.conexao.cursor()

            c.execute("update livros set titulo = '" + self.titulo + "', autor = '" + self.autor + "', isbn = '" + self.isbn + "' where idLivro = " + self.idLivro + " ")

            database.conexao.commit()
            c.close()

            return "Livro atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do livro"
    
    # Deletar livro
    def deletarLivro(self):
        database = Database()
        try:
            c = database.conexao.cursor()

            c.execute("delete from livros where idLivro = " + self.idLivro + " ")

            database.conexao.commit()
            c.close()

            return "Livro excluído com sucesso!"
        except:
            return "Ocorreu um erro ao excluir o livro"
    
    # Buscar livro
    def burcarLivro(self, termo):
        database = Database()
        try:
            c = database.conexao.cursor()

            sql = "select * from livros where titulo = ? or autor = ? or isbn = ?"

            c.execute(sql, (termo, termo, termo))

            linha = c.fetchone()

            if linha:
                self.idLivro = linha[0]
                self.titulo = linha[1]
                self.autor = linha[2]
                self.isbn = linha[3]
                c.close()
                return linha
            else:
                c.close()
                return "Não foi encontrado nenhum livro!"
        except:
            return "Ocorreu um erro ao buscar o livro"