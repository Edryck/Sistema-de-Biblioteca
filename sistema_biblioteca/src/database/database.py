import sqlite3

class Database():

    def __init__(self):
        self.conexao = sqlite3.connect('\dados\biblioteca.db')
        self.criarTabela()
    
    def criarTabela(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists usuarios (
                    idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT UNIQUE, 
                    senha TEXT
                    )""")
        
        c.execute("""create table if not exists livros (
                    idLivro INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT, 
                    autor TEXT,
                    isbn TEXT UNIQUE
                    )""")

        self.conexao.commit()
        c.close()
